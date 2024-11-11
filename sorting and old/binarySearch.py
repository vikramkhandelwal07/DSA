# Binary Search
# recurrence relation T(n) = T(n/2) + c
# time complexity O(logn)
# space complexity O(1)




# fun defination
def binarySearch(arr, intial,end , x):
    while intial<=end: 
        # middle value of the array 
        mid = intial+(end-intial)//2; 
        
        
        # If element is present at the middle itself   
        if arr[mid] == x:
                return mid;
     
        # If element is bigger than mid, then it can only
        # be present in right subarray
        elif arr[mid]>x:
            return binarySearch(arr, intial, mid - 1, x);
        
        else :
            return binarySearch(arr, intial+1, mid, x);
                
    return -1;
            
# driver code
arr = [10 , 20, 30, 40, 50, 60, 70 ,80, 90];
intial = 0;
end = len(arr);
x= int(input("enter the value you want to search: "));

# fun calling....
result = binarySearch(arr, intial,len(arr)-1 , x);
print("Searching element is present at index: ", result)


