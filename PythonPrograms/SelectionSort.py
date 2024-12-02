#For Ascending Order
def selectionSort(arr):
    n = len(arr)
    print(n)
    for i in range(0, n-1):
        minIndex=i
        for j in range(i+1,n):
            if arr[j]< arr[minIndex]:
                #chnage the min Index 
                minIndex=j
                   
    arr[i],arr[minIndex] = arr[minIndex],arr[i]
    
  
arr = [24,41,33,42, 17]
print("Before Sorting Array is :",arr)      
selectionSort(arr)             
print("After Sorting Array is :",arr) 
    
    
    