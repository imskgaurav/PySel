# Bubble sort in Python
def bubbleSort(array):
    for i in range(len(array)):
        print("Value for I is:", i)
        for j in range(0, len(array)-i-1):
            print("J value is",j)
            if array[j] >array[j+1]:
                 array[j], array[j+1]= array[j+1],array[j]
    print("Sorted Asending Order :", array)      

data = [2, 6, 1, 0, -5, 88]
print("Before Sorting :",data)
bubbleSort(data)