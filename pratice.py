#Q1
"""
a=int(input("enter firt number:"))
b=int(input("enter second number:"))
c=a+b
print("sum of two numbers is:",c)"""
#Q2
"""
a=int(input("enter the number:"))
if a%2==0:
    print("number is even")
else:
    print("number is odd") """
#Q3\
"""
a=int(input("enter the number:"))
c=1
while a>0:
    c=c*a
    a=a-1
print("factorial",c)  """

#Q4
"""
n=input("enter your name:")
print("hello",n) """

#Q5 Write a program that takes a string input from the user and writes it to a text file
"""
n=input("enter the string:")
f=open("file.txt","w")
f.write(n)
f.close()  """

#Q6 Write a program that reads the content of a text file and prints it to the console
"""
f=open("file.txt","r")
print(f.read())
f.close()  """

#Q7 Write a python program that takes a string as input and returns its length
"""
n=input("enter the string :")
print("length of string is:",len(n)) """

#Q8 Write a python program that concatenates two strings and returns the results
"""
n="hello"
m="world"
print("concatenated string is:",n+m) """

#Q9 Write a python program that checks if a substring is present in a given string
"""
n="mynameisreena"
m="name"
if m in n :
    print("substring is present")
else:
    print("substring is not present")  """

#Q10 Write a python program that converts a given string to uppercase
"""
n=input("enter a string :")
print("uppercase string is:",n.upper()) """

#Q11 Write a python program that generates the first n numbers in the Write a python program that generates the first n number in the fabonacci series
"""
n=int(input("enter the number of terms"))
a=0
b=1
print(a,end=" ")
for i in range(1,n+1):
    c=a+b
    print(c,end=" ")
    b=a
    a=c  """
#Q12 Write a python program that calculates the sum of the digits of a given number
"""
n=int(input("enter the no."))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("sum of digit is ",sum) """

#Q13 Write a program that asks the user for their birth year and calculates their age
"""
n=int(input("enter the birth year"))
age=2024-n
print("your age is",age) """

#Q14 write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
""" lines = []
print("Enter lines of text (an empty line to finish):")

while True:
    line = input()  
    if line == "":  # Checks if the input is an empty line
        break
    lines.append(line)  # Adds the input line to the list

print("\nYou entered:")  # Prints a separator for clarity
for line in lines:  # Iterates over the list of lines
    print(line)  # Prints each line
"""


#Q15 Write a program that reads data from a CSV file and prints it to the console
"""
f=open("file.txt","r")
for line in f:
    print(line)
f.close()  """

#Q16 Write a program in python that counts the frequency of each character in a string
"""
n=input("enter a string :")
d={}
for i in n :
    if i in d :
        d[i]=d[i]+1
    else:
        d[i]=1
print(d) """

#Q17 Write a program in python that converts a given string to title case (first letter of each word capitalized). 
"""
n=input("enter a strings :")
print(n.title())  """

#Q18 Write a python program that checks if two strings are anagrams of each other.
"""
n=input("enter first string ")
m=input("enter second string :")
c=1
for i in n:
    if i in m:
        c=1
    else:
        c=0
        print("it is not anagram")
        break
if c==1:
    print("it is anagram") """

#Q19 Write a python program that removes all punctuation from a given string.
"""
n=input("enter a string ")
for i in n:
    if i in '''!()-[]{};:'"\,<>./?@#$%^&*_~''' :
        n=n.replace(i,"")
print(n)  """

#Q20 Write a python program that takes a list of numbers and returns their sum. 
"""
l=[1,2,4,2,8,9]
print(sum(l))  """

#Q21 Write a python program that counts the occurrences of a specific element in a list
"""
l=[1,2,4,2,8,2,9,2]
print("count of 2 in list :",l.count(2)) """

#Q22 Write a python program that returns the minimum and maximum values in list of number
"""
l=[1,2,4,2,8,2,9,2]
print("minimum value in list is",min(l))
print("maximum value in list is",max(l)) """

#Q23 Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
"""
n=int(input("enter 1: for celsius to Fahrenheit /n enter 2: for celsius to Fahrenheit ")) 
if(n==1):
    c=float(input("enter temperature in celsius :"))
    f=(c*9/5)+32
    print("temperature in Fahrenheit is",f)
elif(n==2):
    f=float(input("enter temperature in Fahrenheit :"))
    c=(f-32)*5/9
    print("temperature in celsius is",c)
else:
    print("invalid choice")  """

#Q24 Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
"""
a=int(input("enter first no:"))
b=int(input("enter second no:"))
c=input("enter the opertor +, -, *, / ")
if c=='+':
    print("result is",a+b)
elif c=='-':
    print("result is",a-b)
elif c=='*':
    print("result is",a*b)
elif c=='/':
    print("result is",a/b)
else:
    print("invalid choice") """

#Q25 Write a program that copies the contents of one text file to another. 
"""
f=open("file.txt","r")
g=open("file2.txt","w")
g.write(f.read())
f.close()
g.close() """

#Q26 Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
"""
a=input("enter a string")
prefix=input("enter prefix")
suffix=input("enter suffix")
if a.startswith(prefix):
    print("string starts with prefix")
elif a.endwith(suffix):
    print("string ends with suffix")
else:
    print("not suffix nor prefix") """

#Q27 Write a program in python that converts a string into a list of its characters.
"""
a=input("enter the string :")
b=list(a)
print(b)
"""

 



