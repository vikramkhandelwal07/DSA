# function defination
def getSum(arr, target):
    i = 0;
    j = len(arr)- 1;
    while i<=j:
        if (arr[i] + arr[j] == target):
            return i , j ;
        elif (arr[i] + arr[j] < target): 
            i +=1;
        else :
            j -=1;
    return -1 -1;
    

# driver code 
arr = [20, 40, 60, 80, 90, 120, 240];
target = 210;
ans = getSum(arr, target);
print("the numbers for the given target is :",ans);
