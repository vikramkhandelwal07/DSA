     
def findSum(A,N):         
    min = 100
    max = -100
    for  j in range(0,len(A)):
        if A[j] < min:
            min = A[j]
        if A[j] > max:
            max = A[j]   
    return min+max
    
    
N = int(input())
A =[]   
for i in range(0,N):
    ele = int(input(" "))
    A.append(ele) 
x = findSum(A,N)
print(x)