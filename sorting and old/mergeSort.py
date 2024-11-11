
def mergeProcedure(arr, i , mid, j):
    ## n1 and n2 is the number of elements in the LSA AND RSA 
    
    n1 = mid - i + 1
    n2 = j - mid
    left_SubArray = [0]*n1
    right_SubArray = [0]*n2
    
    ## copying the element is LSA and RSA 
    
    for m in range(n1):
        left_SubArray[m] = arr[i+m]
    
    for n in range(n2):
        right_SubArray[n] = arr[mid+1+n]

    p = 0
    q = 0
    k = i

    while p < n1 and q < n2 :
        if left_SubArray[p] <= right_SubArray[q]:
            arr[k] = left_SubArray[p]
            p+=1
        else:
            arr[k] = right_SubArray[q]
            q+=1
        k+=1
    ## ye code tab chalega jab kisi ek side ke elemnts in array khatam hojayenge 
    while p<n1:
        arr[k] = left_SubArray[p]
        p+=1
        k+=1
        
    while q<n2:
        arr[k] = right_SubArray[q]
        q+=1
        k+=1
# this function is the merge sort function 
def mergeSort(arr, i, j):
    if i < j:
        mid = (i)+( j-i)// 2
        mergeSort(arr, i, mid)
        mergeSort(arr, mid + 1, j)
        mergeProcedure(arr, i, mid, j)
    return arr

# driver code
arr = [50,70,65,13,80,62,98,27]
i = 0
j = len(arr) - 1
result = mergeSort(arr, i ,j) 
print(result)