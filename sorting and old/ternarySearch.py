# function defination
def ternarySearch(arr ,  i, j , key):
    mid1 = i + (j-i)//3;
    mid2 = j - (j-i)//3;
    
    while i<=j:
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        
        elif key < arr[mid1]:
            return ternarySearch(arr , mid1 -1, j , key)
        
        elif key > arr[mid2]:
            return ternarySearch(arr ,  i , mid2 - 1 , key)

        else :
             return ternarySearch(arr ,  mid1+1 , mid2 - 1 , key)
         
    return -1
     



# driver code 
arr = [ 20, 25, 47, 56, 59, 63, 65, 79, 82]
i = 0;
j = len(arr)-1;
key = int(input("enter the number you want to search:"))
result = ternarySearch(arr, i , j,  key)
print("the number is at index :" , result);
