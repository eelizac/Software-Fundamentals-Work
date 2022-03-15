def divisors(n):
    '''
    Given some number n, return a set of all the numbers that divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    if type(n) is not int and n <= 0: 
        raise ValueError("n is not ap positive integer")

    a = 1
    while True:
        if a > n: 
            return 
        if n % a == 0:
            yield a 
        a = a + 1

if __name__ == "__main__": 
    print(set(divisors(-2)))