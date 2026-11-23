'''
Funcations are termed as first class objects..

Anonymous functions : an anonymous function is a nameless function, we us lambda
keyword to use it..

they are generally used for short simple,operations can be written in the single line
they are also termed as lambda functions.. they are generally used with filter(),map()
and reduce()

syntax : lambda argument(s) :expression

#create a function to get area of rectangle

def rectangle(l,b):
    """area of rectangle"""
    return l*b
print(rectangle(7,5))

area = lambda l,b : l*b
print(f'area of rectanle is {area(7,5)}')

#Square of a number ----> Normal Function ---> Lambda Function

def square(number):
    """Square of a number"""
    return number**2
number = int(input())
print(f'Square of a number is {square(number)}')

number = int(input())
square = lambda number : number **2
print(f'Square of a number is {square(number)}')

#find maximum of two numbers

def maximum(a,b):
    """maximum logic"""
    return a if a>b else b
print(maximum(10,35))

maximum =lambda a,b : a if a>b else b
print(maximum(37,35))

greet = lambda :"welcome to vizag"
print(greet())

#filter() used to select elememts from an iterable based on condition
#only the elemets that satisfy the condition are returned

#filter(function,iterable)

number = [1,2,4,6,7,8,9,10,12,45,67]

def even(number):
    result=[]
    for i in number:
        if i%2==0:
            result.append(i)
    return result
print(even(number))

result = list(filter(lambda num:num%2==0,number))
print(result)

odd_result = list(filter(lambda num:num%2!=0,number))
print(odd_result)

prices = [500,600,700,1200,800,900]
#products above 700

result = list(filter(lambda price:price>700,prices))
print(result)



#map applies transformation to every element in a collection
#map(function,*iterables)

scores = [15,20,19,23]
result = list(map(lambda new_score:new_score+1,scores))
print(result)

d=list(map(int,input().split()))
print(d)
'''
#add gst -->18%
prices = [1000,5000,4500]
final_price = list(map(lambda price:price + (price*0.18),prices))
print(final_price)

#cal length of objects in a collection
subjects = ['python','sql','aptitude','softskills']
result = list(map(lambda word:len(word),subjects))
print(result)
