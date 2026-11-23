'''
#Usage of variable length and keyword  variable length argument

def scores(*marks,**names):
    """Scores Scenario with Variable and Keyword Variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total Marks are : {total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name : {name}')
        print(f'Value : {value}')
        
scores(25,20,15,18,16,name = "Ajay",place = "Vizag",batch = "PFS-VSP-007")

#positional arguments always follows keyword argumnts
#non default alway follows default args 


#scope -->determine where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined...


type of scope : local scope,global scope,global keyword,nonlocal scope

#locla scope: variables defined and accessible only inside the funcation..

def fname():
    """usage of local variables"""
    name = "phaneswar"
    return f'{name} is in vizag'
print(fname())
#print(name)
name = "codegnan"
print(name)


#global variable -->a variable declared outside all fi=ncations is called a
#global variable. it can be accessed from anywhere in the program
name = "phaneswar"
def uname():
    """global scope """
    name="codegnan"
    return f'{name} is in vizag,vijayawada and hyderabad'
print(uname())
print(name)


#global keyword -->used when we want to modify a global variable
#inside the funcation
count = 15
def update():
    """global keyword usage"""
    global count
    count =count+15
    return f'update count is {count}'
print(update())
print(f'new count is {count}')
values =[1,2,3,45]
values.append(count)
print(values)


#nonlocal scope -->used in nested funcations..allows modifications of
#variable from the outer funcation

def outer():
    """outer function"""
    count = 10
    def inner():
        """inner funcation"""
        nonlocal count
        count = count+15
        return f'result from inner funcation is {count}'
    print(inner())
    return f'result from outer funcation is {count}'
print(outer())


#legb -->local,enclosing-->global-->built-in

len =45
a= ['codegnan','python']
#print(len(a))


#funcation are termed as first class objects
#pass by value and pass by object reference



#pass by value -->immutable objects
#int,float,bool,str,tuple,complex,frozenset
#when immutable objects are passed to funcation,changes inside the funcation
#donot effect the original value

def update(number):
    """pass by value usage"""
    number = 15
    print('inside funcation:',number)
number = 20
#print("outside value is",number)
print(update(number))
print(update(25))

'''
