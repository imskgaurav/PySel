
num = int(input("Enter ur Number"))
print('The User input Number is',num)

count=0
while(num>0):
    r=num%10
    count+=1
    num=num//10
print("Count is", count)