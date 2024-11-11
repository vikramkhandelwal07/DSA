# function defination

def findPowerOfElement(a,n):
    # small problem
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        # big problem 
        # use divide and conquer
        # 1. divide 
        mid = n//2
        # 2. conquer
        b = findPowerOfElement(a, mid)
        # 3. combine
        result = b*b
        if n%2 == 0:
            return result
        else:
            return result*a
# driver code

a = int(input("enter the number"))
n = int(input("enter the power"))

# function calling

result = findPowerOfElement(a,n)
print("the power of the element is: ",result)
    