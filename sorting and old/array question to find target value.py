# here a 2d array is given and u have to find the targeted value.
# time complexity O(logm*n)

# function defination
def search_2D_Array(arr, target):
    m = len(arr)
    if m == 0:
        return False
    # number of columns
    n = len(arr[0])
    left, right = 0 , m*n-1
    # concept of binary search
    
    while left<=right:

        mid = left+(right - left)//2  
        # row Number --> mid // n
        #  col number --> mid % n
        mid_element = arr[mid//n][mid%n]
        if mid_element == target:
            return True
        elif mid_element > target:
            right = mid-1
        else :
            left = mid +1
    return False


# driver code

arr = [[1,3,5,7],[10, 11, 16,20], [23,30,34,60]]
target = 36
result = search_2D_Array(arr , target);
print(result)
