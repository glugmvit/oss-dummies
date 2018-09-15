import add

def adder(x,y):
    if add.foo(x,y) == (x+y):
        print("Looks good")
    else:
        print("Something wrong")

def main():
    x=int(input("Enter a number:\t"))
    y=int(input("Enter another one:\t"))
    adder(x,y)

main()