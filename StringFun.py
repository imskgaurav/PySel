#https://www.youtube.com/watch?v=LU2hvZUkt0I&t=1814s
s= "Python9"
#isalphanum()
print(s.isalnum())
# isalpha()
s1='pyhton11'
print(s1.isalpha())
#isdigit 
s2= '786'
print(s2.isdigit())
#isIdentifier
"""A string is considered a valid identifier if it only contains
alphanumeric letters (a-z) and (0-9), or underscores (_). 
A valid identifier cannot start with a number, 
or contain any spaces."""
print("Check Identifier")
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
e='_joyFul_'
xx= 'PANDA'
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
#Lower upper .isSpace
print(" ".isspace())
print(d.islower())
print(xx.isupper())