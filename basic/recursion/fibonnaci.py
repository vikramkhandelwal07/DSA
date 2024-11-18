def fibonnaci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonnaci(num-1)+ fibonnaci(num-2)
    
    

print(fibonnaci(5))