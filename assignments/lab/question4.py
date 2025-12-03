# Write a python program that prints the Fibonacci series up to n terms.

def fibonnaci(n):
    if(n <= 1):
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

while True:
    try:
        a = int(input("Enter a number: "))
        if(a.is_integer() and a >= 0):
            break
    except :
        print("Please enter a integer")


# // khali, Exception, ValueError
i = 0



while True:
    val = fibonnaci(i)
    if(val > a):
        break
    print(val)
    i += 1


