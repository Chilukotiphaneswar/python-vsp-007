'''

Built-in funcations-->funcations which are in builtin python
abc(),any(),all(),bin(),bool()...


dir(_builtins_)-->enumerate(),zip()
'''
details = ['codegnan','saketh','pfs-vsp-007']
'''
0 : codegnan
1 : saketh
2 : pfs-vsp-007

for i in details:
    print(details.index(i),':',i)

for i in range(len(details)):
    print(i,':',details[i])

for i,j in enumerate(details):
    print(f'{i} : {j}')

#enumerate() will create a counter object for an iterable
#zip() will combine multiple iterables into a single iterable

data=['ganesh','sai','karthik']
marks=(20,25,24)
details = dict(zip(data,marks))
print(details)



emails=input().split()
print(emails)
for email in emails:
    print(email.split('@')[1])

orders = list(map(int,input().split()))
print(orders)


salaries = eval(input("enter the salaries:"))
print(salaries)
print(type(salaries))


print(int(4.56))
print(round(4.56))
print(round(4.567,2))
'''
#function is termed as first class object
#recursive functions--> a function calling itself,where it makes the
#smaller problem is broken into multiple times...
#depends on two cases -->base case (it indicates when to stop recursion)
                        #-->Recursive case (it makes the problem to the be repeated)

'''
syntax:
def function():
    if base_condition:
        return
    funcation{}
funcation()


#factorial approach using recursion

def factorial(n):
    """recursive approach"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return "no -ve values only +ve values to be accepted"
    else:
        return n*factorial(n-1)
n=int(input("enter a value:"))
print(factorial(n))
'''

#sum of natural number using recursive logic
#5 -->15 #

def sum_natural(n):
    """recursive approach"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return "no -ve values only +ve values to be accepted"
    else:
        return n+ sum_natural(n-1)
n=int(input("enter a value:"))
print(sum_natural(n))

#task:build a simple choice chooser:
------------------welcome to game---------------
1-->recursion logic factorial
2-->sum of natural number (recursion)
3-->bmi calculation
4-->fibonacci series
5-->atm usecase
any other number --> only enter 1-5
q-->quit
'''
    
