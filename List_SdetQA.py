#Declare list 
list1 = list()
print(list1)
print(type(list1))
list2 = []
print(type(list2))
#Creat with Elemenet
l3 = list([3,4,55,99])
print(l3)
#
'''If you pass String argument without square Bracket. 
list will consider each Chatracter as items of List'''

l4= list("Python")

print(l4)

ll= [4,9,0,0, 98,45]
print(ll[0])

#Method in list, #len min, max , sum 
print('Check len, Min , Max, Sum method of List')
print(len(ll))
print(max(ll))
print(min(ll))
print(sum(ll))
#Access list using for loop 
for i in ll :
    print(i)
    
print(4 in ll)

#Count ,append ,sort , pop , remove, index 
print('Count Sort pop and Remove')
print(ll.count(0))
print(ll.remove(0))
print(ll)
print(ll.count(0))
ll.sort()
print(ll)
ll.append(-99)
print(ll)
print(ll.index(-99))
    
