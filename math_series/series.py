
""" This function calculates the fibboanncci
 numbers based on the N parameter recursively
"""
def fib(n):
    if n <= 0:
        print('Invalid input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

""" This function essentailly does the same as fib but 
starting with the lucas numbers"""
def lucas(n):
    if n <=0:
        print('Invalid Input')
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))

""" This functions 
calculates math series depending 
on what you enter for the parameters giving it its two 
starting numbers
"""
def sum_series(n,x=0,y=1):
    if ( x == 0 and y == 1 ):
        if n <= 0:
            print('Invalid input')
        elif n == 1:
            return x
        elif n == 2:
            return y
        else:
            return sum_series(n - 1,x,y) + sum_series(n - 2, x,y)
    else:
           if n <=0:
            print('Invalid Input')
           elif n == 1:
               return 2
           elif n == 2:
               return 1
           else:
               return (lucas(n-1) + lucas(n-2))

        
    

