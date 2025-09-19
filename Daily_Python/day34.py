""" Build a Simple Memoization Decorator

Difficulty: Intermediate

Challenge Description: Implement a decorator memoize that caches a function’s return value based on its arguments. Use a dictionary for the cache with keys derived from (args, sorted kwargs). Requirements:

Use functools.wraps to preserve metadata.

Cache only when all arguments are hashable; if not hashable, call the function without caching (no error).

Support both positional and keyword arguments.

Expose wrapper.cache_size() → int to report the number of cached entries.

Expose wrapper.clear_cache() to empty the cache.

Do not cache exceptions (if the wrapped function raises, nothing should be stored) """

import time
import functools

def memoize(func=None, *, ttl=None):
    """
    Usage:
      @memoize
      def f(...): ...

      @memoize(ttl=2.5)
      def g(...): ...
    """
    if func is None:
        return lambda real_func: memoize(real_func, ttl=ttl)

    cache = {}  # key -> (value, expires_at or None)

    def _now():
        return time.monotonic()

    def _expired(expires_at):
        return expires_at is not None and _now() >= expires_at

    def _purge_expired():
        if ttl is None:
            return
        to_delete = [k for k, (_, exp) in cache.items() if _expired(exp)]
        for k in to_delete:
            cache.pop(k, None)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Build a cache key and verify it's hashable (including kwarg values)
        try:
            key = (args, tuple(sorted(kwargs.items())))
            hash(key)  # raises TypeError if any component is unhashable
        except TypeError:
            # Unhashable → no caching
            return func(*args, **kwargs)

        _purge_expired()

        if key in cache:
            value, expires_at = cache[key]
            if not _expired(expires_at):
                return value
            # expired → fall through to recompute & refresh

        try:
            result = func(*args, **kwargs)
        except Exception:
            # Do not cache exceptions
            raise
        else:
            expires_at = (_now() + ttl) if ttl is not None else None
            cache[key] = (result, expires_at)
            return result

    # Introspection helpers
    def cache_size():
        _purge_expired()
        return len(cache)

    def clear_cache():
        cache.clear()

    wrapper.cache_size = cache_size
    wrapper.clear_cache = clear_cache
    wrapper._cache = cache  # optional: exposed for debugging/tests
    return wrapper


# -------------------------
# Example usage & quick test
# -------------------------
def slow_square(n):
    for _ in range(1_000_00):
        pass
    return n * n

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@memoize(ttl=1.0)  # BONUS: entries expire after 1 second
def power(base, exp=2):
    return base ** exp

if __name__ == "__main__":
    print(power(3))            # 9
    print(power(3))            # cache hit → 9
    print(power(3, exp=3))     # 27
    print(fib(10))             # 55
    print(power.cache_size())  # 2
    power.clear_cache()
    print(power.cache_size())  # 0

    # TTL demo (optional):
    print(power(4))            # computes 16
    time.sleep(1.1)
    print(power(4))            # recomputes after expiry → 16