# Initialize a dictionary 'sum_cache' with the base case value for memoization
sum_cache = {0: 0}

# Define a recursive function 'number_sum' to calculate the sum of the first n numbers
def number_sum(n):
    '''Returns the sum of the first n numbers'''
    assert(n >= 0), 'n must be >= 0'
    if n in sum_cache:
        return sum_cache[n]

    res = n + number_sum(n-1)
    sum_cache[n] = res

    return res


if __name__ == '__main__':
    from timeit import Timer
    
    # Create a Timer object to measure the execution time of 'number_sum(300)'
    t = Timer('number_sum(300)', 'from __main__ import number_sum')
    
    print('Time: ', t.timeit())
