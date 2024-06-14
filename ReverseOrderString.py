
str1 = "Python is an interpreted language"
str2 ='the source code of a Python program is converted into bytecode that is then executedby the Python virtual machine'
print(type(str1))
print(str1[0:len(str1)])
#Immutable 
#https://www.youtube.com/watch?v=LU2hvZUkt0I
s1= "Python"
s2= "Python"
print(id(s1), id(s2))
if(s1==s2):
    print('same String')
    
s1+'programming'
print(s1)   

s1 = s1+'programming'
print(s1) 

name1 = str("welcome Shashi")
print(name1)
# + And * 
print(name1*3)
#Slicing in Python 
ss = "Welcome"
print(ss[:])
print(ss[:6]) #Start from 0 to Till n-1 (5)
print(ss[0:]) # Start from 0 And till last char of String
#Ord and chr Fucntion 
print(ord('A'))# Print Ascii Value of A 
print(chr(65))# Print Char Against the Ascill value

#Max Min Function of str class 
print(max("abc"))
print(min("abc"))
#in And not in operator 
str3= "python"
print('py' in str3) # True if Found
print('thon' not in str3)

#Comparing the String 
print("Python" =="java")
print("Python" == "Python")
print('freedom' >'free') # comparing String lexiocographically i e using Ascii value
print('freedom' != 'free')
#Ascii vale of A is 65 while a is 97 
print("python" >"PYTHON")
#iTERATING STRING in python
