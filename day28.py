'''
data = [i*j for i in range (1,11) for j in range (1,11)]
#print(data)
for i in range(0, 100, 10):
    print(*data[i:i+10])
'''
data = [(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f = [i*j for i in range(1,4) for j in range (1,4)if i!=j]
print(f)
print(*f)

#nested comprehension with if-else usage
#[true_value if condition else false_value
#for item1 in iterable1 for item2 in iterable2]


week_1 = [15,20,25,22,18,19]
week_2 = [23,19,21,18,19,25]

result = {'pass' if x<y else "fail" for x in week_1 for y in week_2}
print(result)

#generator --> it is a special function,which produces one value at a time
#we use yield keyword
'''
def fname():
    """doc string"""
    return value(s)...

    ....
fname()


def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3
    .....
fname()

def func():
    """normal funcation"""
    return[1,2,3,4,5]
    #return "phaneswar" #a function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)

def func():
    """generator function"""
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
#print(next(b))

def display():
    """subjects covered"""
    yield ["python",45,'paperbased exams']
    yield ["aptitude",65,'weekly exams']
    yield ["softskills",60,'activities']
    yield ["frontend",45,'projects']
    yield ["fastapi",45,'integration']
print(display())
g = display()
print(f'subject alloted is {next(g)}')
print(f'subject alloted is {next(g)}')
print(f'subject alloted is {next(g)}')


week_1 = [20,14]
week_2 = [15,20]
result = ("improved" if x<y else "lagged" for x in week_1 for y in week_2)
#print(result)
g = result
print(next(g))
print(next(g))
print(*result)

'''
#exception handling
#exception is an event that occurs during the execution of a program
#which disrupte its normal flow..

#typeerror,valueerror,indexerror,ATTRIBUTEERROR,keyerror,zerodivisionerror.
#we will be using try,except and finally...

"""
syntax:
try:
  #code that raise an exception
except exceptiontype:  #it handles the error if it occurs
  #code to handle the exception
"""

#basic exception handling
a,b =5,0
try:
    result =a/b
    print(f'answer is {result}')
except :
	print("check")
