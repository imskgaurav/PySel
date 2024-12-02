import math
x ='Vanshita'
print(x)

y=x+"8"
print(y)

print(math.pi)
print(math.sin(45))

data = [1,2]
data2= [4,7]
data.extend([3,7,11,13])
print(data)
print(type(data))

#print List 

for x in ['apple', 'banana', 'cherry']:
    print(x)
    
#append TWO list

list1 = ["x", "y","z"]
list2= [1,3,5]
list3 = list1+list2
print(list3)
#using Append 
list1.append(list2)
print(list1)
## Appned method for individual Eleme
l1 = ['a', 'e', 'i', 'o', 'u']
l2= [2,4,6]
for x in l2:
    l1.append(x)
    
print(l1)    

