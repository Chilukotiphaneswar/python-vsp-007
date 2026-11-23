
import functools
from functools import reduce
'''
#sum of number from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)

#largest number from a collection
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b:a if a>b else b,data)
print(result)

#return the longest word in a group of strings

word = ['python','developer','sql','programming']
longest = reduce(lambda a,b:a if len(a) >len(b) else b,word)
print(f'longest word : {longest}')


#list comprohensions -->in python,it is a precise way to create
#list
#syntax-->[expression for item in iterable]
#iterable -->list,set,dict or range{}

li =[]
for i in range(10):
    #print(i)
    li.append(i)
print(li)

li = [i for i in range(10)]
print(li)
#squares of 1-10 numbers in a list 
squares = [i**2 for i in range(1,11)]
print(squares)

#even number
even = [i%2==0 for i in range(1,11)]
print(even)

even = [i for i in range(1,11) if i%2==0]
print(even)

#update stores of each person with 10marks
scores =[25,45,50,60,55]
f_scores = [i+10 for i in scores]
print(f_scores)
m_scores = list(map(lambda  i:i+10,scores))
print(m_scores)

names = ['phaneswar','codegnan','vizag']
result  = [i.upper() for i in names]
print(result)

'''
#list comperhension with if-else usage
#[true_value if condition else false_value for item in literable]
data = [12,4,5,6,8,9]
result = ["even" if i%2==0 else "odd" for i in data]
print(result)
result = [i**2 if i%2==0 else i**3 for i in data]
print(result)

#nested list comprehensions -->one inside another
#[expression for i in iterable for j in iterable2]

colors = ['red','blue','white']
sizes = ['s','m','l','xl']
dress = [(color,size)for color in colors for size in sizes]
print(dress)

d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)
