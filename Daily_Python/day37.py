""" Retry Decorator with Exponential Backoff

Difficulty: Intermediate

Challenge Description: Implement a decorator @retry that retries a function call when it raises a specified exception. Parameters:

exceptions: a single Exception type or tuple of types to catch (default: Exception)

max_attempts: int > 0 (default: 3)

base_delay: float seconds for the first delay (default: 0.1)

factor: multiplier applied to the delay after each failure (default: 2.0)

jitter: optional float added/subtracted uniformly at random in [-jitter, +jitter] to each delay (default: 0.0)
Behavior:

On failure, sleep for delay seconds, then retry. Delay grows as base_delay * (factor ** (attempt - 1)), plus jitter if provided.

If all attempts fail, re-raise the last exception.

Preserve the wrapped function’s name and doc.

Do not import any third-party packages. """

def _self_test_no_sleep():
    """Quick self-test that avoids real sleeping by patching time.sleep."""
    calls = {"n": 0}
    slept = {"calls": 0}
    orig_sleep = time.sleep
    try:
        time.sleep = lambda s: slept.__setitem__("calls", slept["calls"] + 1)
        @retry(exceptions=ValueError, max_attempts=4, base_delay=0.001, factor=2.0, jitter=0.0)
        def f():
            calls["n"] += 1
            if calls["n"] < 3:
                raise ValueError("boom")
            return calls["n"]
        assert f() == 3
        assert calls["n"] == 3
        assert slept["calls"] == 2  # slept after each of the two failures
    finally:
        time.sleep = orig_sleep