from array import *

def fibo():
    f = array('i',[0,1])
    n = int(input('Enter the number of terms:'))
    if n == 1:
            print(f[0])
    elif n == 2:
        for i in range(2):
            print(f[i])
    else:
        for i in range(3,n+1):
            f.append(f[i-3]+f[i-2])
        for i in f:
            print(i)

fibo()
        
    