print('hello world')
x=5
y=6
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
x=1j
print(type(x))
x=2
print(type(x))
x='ranee'
print(print(type(x)))
x=0
print(bool(x))
x=''
print(bool(x))
x=3
print(bool(x))
fruits=['apple','banana','cherry']
x,y,z=fruits
print(x)
x=y=z=fruits
print(y)
x,y,z='30','40','50'
print(x)
x='30','40','50'
print(x)
print("this is python")
if 5>2:
    print('five is greater than two')
x=4.6
print(type(x))
my_var=40
print(my_var)
fruits=[2,4,8,34,50]
print(type(fruits))
#x=9
x='good'
def my_function():
    print('python is ' + x )
my_function
def my_function():
    globalx
    x='good'
    my_function()
list=[1,2,3]
print(len(list))
list=[1,2,3,4,4,4,5,6,7]
for x in list:
    print(x)
my_list=['apple','banana',1,3,5,7]
my_list[2:5]='abc'
print(my_list)
my_list=[1,2,4,5,6]
my_list.insert(2,3)
print(my_list)
my_list.insert(2,'svchm')
print(my_list)
my_list.append('ksbckj')
print(my_list)
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
list1=[1,2,3,'apple',4,5,6]
list1.remove('apple')
print(list1)
list1.pop(3)
print(list1)
list1=[1,2,3,4,5,6]
list1.append('apple')
print(list1)
list1.insert(7,'banana')
print(list1)
list2=[9,0]
list1.extend(list2)
list1.remove('banana')
print(list1)
list1.pop(7)
print(list1)
list1.pop(6)
print(list1)
list1.remove(0)
print(list1)
list1.clear()
print(list1)
list1=[]
list1.append(1)
print(list1)
list1[0]='hello'
print(list1)
list1=[1,2,3,4,4,4,5,6]
for x in list1:
    print(x)
list=[2,5,1,4,8]
list.sort()
print(list)
list.sort(reverse=True)
text='hello'
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace('hello','World'))
print(text.split())
x=4
y='name'
print(x,y)
print('i am {} years old and name is {}'.format(x,y))
print('i am (4) years old and name is (name)')
x=5
x+=3
print(x)
y=10
y*=2
print(y)
x=2
x*=8
print(x)
x/=9
print(x)
x**=3
print(x)
x%=4
print(x)
x//=9
print(x)
x=10
y=7
print(x>y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
print(x>=y)
print(x<y)
print(x>3 and x<10)
print(x>10 or x<=10)
print(x is not y)
print(x is y)
number=(1,2,3,4,5)
print(number)
print(number[0])
print(number[-1])
sinle=(10,)
print(sinle)
for num in number:
    print(num)
colours={'red','green'}
print(colours)
colours.add('yellow')
print(colours)
colours.remove('green')
print(colours)
for color in colours:
    print(color)
student={
    'name':'victoria secret',
    'age':100,
    'grade':'F'
}
print(student)
print(student['name'])
print(student.get('age'))
print(student)
student['age']=101
student['city']='delhi'
print(student)
student.pop('grade')
del student['city']
print(student)
for key,value in student.items():
    print(key,'.',value)
age=20
if age>18:
    print('you are eligible to vote.')
elif age==18:
    print('you are teen')
else:
    print('you are not eligibble')
marks=85
if marks>=90:
    print('grade:A+')
elif marks>=75:
    print('grade:A')
elif marks>=60:
    print('grade:B')
else:
    print('grade:C') 
x=15
if x>10:
    print('x is greater than 10')
    if x>20:
        print('x is also greater than 20')
    else:
        print('x is not greater than 20')     
x=15
if x%2==0:
    print('x is even')
else:
    print('x is odd')
fruits=['apple','banana','cherry']
for fruit in fruits :
    print(fruit)
word='Python'
for x in word:
    print(x)
for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(1,4):
    for j in range(1,3):
        print(f"i={i},j={j}")
for i in range(1,6):
    if i==4:
        break
    print(i)
for i in range(1,6):
    if i==3:
        continue
    print(i)
for i in range(1,4):
    print(i)
else:
    print('loop is finished')
for i in range(0,21):
    print(i)
for i in range(2,30,2):
    print(i)
colour=['red','blue','green','yellow']
for i in colour:
    print(i)
for i in range(3):
    for j in range(3):
        print(f'({i},{j})',end='')
    print()
def function_name():
    print('HAKUNA MATaTA:)')
function_name()
def greet(name):
    print(f'HELLO,{name}!')
greet('taylor')
greet('swift')
def add(a,b):
    return a+b
result=add(5,3)
print(result)
def greet(name='student'):
    print(f'Hello,{name}!')
greet()
def sub(a,b):
    return a-b
result=sub(5,3)
print(result)
def div(a,b):
    return a/b
result=div(5,3)
print(result)
def mul(a,b):
    return a*b
result=mul(5,3)
print(result)
def floor(a,b):
    return a//b
result=floor(5,3)
print(result)
def modulus(a,b):
    return a%b
result=modulus(5,3)
print(result)
x=10
def my_fun():
    y=5
    print('Inside:',x,y)
my_fun()
print('Outside:',y)
def greet():
    print('Hello')
greet()
def function(a,b):
    return a+b
result=function(3,5)
print(result)
a=3
def my_fun():
    b=10
    print('Inside:',a,b)
my_fun()
print(a)
class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def drives(self):
        print(f"The {self.color} {self.brand} is driving.🚓")
car1 = car('bmw', 'black')
car2 = car('tesla', 'white')
car1.drives()
car2.drives()
#array-collection of same data type
import array
numbers=array.array('i',[1,2,3,4,5])
print(numbers)
#print(number[index])
print(numbers[0])
print(numbers[3])
#random means samething that can not be prediccted logically,random module to work with random number
#To generate number any from 0 to 99,100 will not be included
from numpy import random
x=random.randint(100)
print(x)
#to generate number from 0 to 1.0,doen't include 1.0,it generate a 1D array
x=random.rand()
print(x)
print(type(x))
#1D
x=random.randint(100,size=(5))
print(x)
#2D,3=rows,5=coloumn
x=random.randint(100,size=(3,5))
print(x)
#2=block,8=rows,9=column,3D
x=random.randint(100,size=(2,8,9))
print(x)
#4D
x=random.randint(100,size=(2,8,9,5))
print(x)
#return one of the value of array
x=random.choice([3,5,7,9])
print(x)
x=random.choice([3,5,9],size=(2,3,4))
print(x)
#pandas is python library design for data manupulation and analysis  1)it handle tabular data
#2)labels for rows and column
#3)fast mathematical operation
#4)largest database handling
#5)stastic analysis
#series 1D array with index labeled
import pandas as pd
data=[10,20,30,40]
s=pd.Series(data)
print(s)
#data frame 2D or big from that,similar to excel and sql ,each column is a series and column together make data frame
data={'Name':['alice','bob','charlie','david'],
'Age':[24,27,22,32],
'City':['delhi','mumbai','chennai','kolkata']}
df=pd.DataFrame(data)
print(df)
import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)
data={'maths':90,'science':80,'english':78}
s=pd.Series(data)
print(s)






