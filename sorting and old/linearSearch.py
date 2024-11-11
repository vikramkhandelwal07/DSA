# function defination
# time complexity is O(n)
# space complexity is O(1)

def linearSearch(arr , x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
        
    return -1

# driver code 
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
x = int(input("enter the value you want to search from the array:"));
result = linearSearch(arr , x);
print("searching element is present at index :", result);