# fibonacci generator 
def fib(n): 
    
    # 1, 1, 2, 3, 5 ... 
    counter, a, b = 0, 1, 1

    while True:
       # print(counter) 
        if counter > n: 
            return 
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == "__main__": 
    (x) = list(fib(4))
    print(x)