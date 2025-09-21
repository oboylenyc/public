""" Decorator with Arguments: Average Runtime Timer

Difficulty: Intermediate

Challenge Description:
Create a decorator factory average_time(runs: int = 5) that returns a decorator. When applied to a function, the decorated function should execute the original function runs times, measure each execution using time.perf_counter(), and return a tuple: (original_result, average_seconds). Use functools.wraps to preserve the original function’s metadata. Constraints: runs must be a positive integer; raise ValueError for invalid runs. """

from functools import wraps
from time import perf_counter
from statistics import mean, stdev
from typing import Any, Callable, Tuple, Dict


def average_time(runs: int = 5) -> Callable[[Callable[..., Any]], Callable[..., Tuple[Any, float, Dict[str, float]]]]:
    if not isinstance(runs, int) or runs <= 0:
        raise ValueError("runs must be a positive integer")

    def decorator(func: Callable[..., Any]) -> Callable[..., Tuple[Any, float, Dict[str, float]]]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Tuple[Any, float, Dict[str, float]]:
            times: list[float] = []
            result: Any = None

            for _ in range(runs):
                start = perf_counter()
                result = func(*args, **kwargs)
                times.append(perf_counter() - start)

            avg = mean(times)
            # Bonus stats
            stats = {
                "min": min(times),
                "max": max(times),
                "stddev": stdev(times) if len(times) > 1 else 0.0,
            }
            return result, avg, stats

        return wrapper

    return decorator


# --- Example usage ---
if __name__ == "__main__":
    from time import sleep

    @average_time(runs=3)
    def slow_add(a, b):
        sleep(0.01)
        return a + b

    result, avg, stats = slow_add(2, 3)
    print(result)               # 5
    print(round(avg, 4))        # ~0.01
    print({k: round(v, 4) for k, v in stats.items()})
    # e.g., {'min': 0.01, 'max': 0.0112, 'stddev': 0.0005}
