def fibonacci(n:int)->int:
    """ return series at nth value to the user """
    f0=0
    f1=1
    print(f0)
    print(f1)
    for i in range(n):
        f=f0+f1
        f0=f1
        f1=f
        print(f,"\t")
fibonacci(23)
