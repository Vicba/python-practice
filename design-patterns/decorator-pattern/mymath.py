import functools

def memoize(fn):
    cache = dict()

    # Use the functools.wraps decorator to update the wrapper function's metadata
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    
    return memoizer

# Apply the memoize decorator to the 'number_sum' function
@memoize
def number_sum(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be greater than or equal to 0'
    return 0 if n == 0 else n + number_sum(n - 1)

# Apply the memoize decorator to the 'fibonacci' function
@memoize
def fibonacci(n):
    """Returns the nth number of the Fibonacci sequence"""
    assert (n >= 0), 'n must be greater than or equal to 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


def main():
    from timeit import Timer

    # List of functions and corresponding Timer objects for execution and timing
    to_execute = [
        (number_sum, 
         Timer('number_sum(300)', 'from __main__ import number_sum')),
        (fibonacci, 
         Timer('fibonacci(100)', 'from __main__ import fibonacci'))    
    ]
    
    # Iterate through the list of functions and timers
    for item in to_execute:
        # Extract function and timer from the tuple
        fn = item[0]
        t = item[1]

        # Print function name and docstring
        print(f'Function "{fn.__name__}": {fn.__doc__}')
        # Print the execution time using the Timer object
        print(f'Time: {t.timeit()}')
        print()


if __name__ == '__main__':
    main()
