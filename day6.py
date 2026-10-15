'''
Tokens,Datatypes (Numeric,Boolean,NoneType,Sequences (str,lists,tuples,sets,Frozensets,Mapping odjects
(dicts)) typecasting
Operators
Input Formatting / output Formatting


#input formatting -->input()

#Usage of input()
#we can pass any type of object as input -->result is in only string


name = input("enter the name:")
print(name)
print(type(name))


#integer input -->in()
roll_number = int (input("enter the roll number:"))
print(roll_number)
print(type(roll_number))

#Float input -->float()-->we can pass either integeer / decimal value -->float
marks  = float(input("enter the marks:"))
print(marks)
print(type(marks))


#group of strings (multiple values as strings)
#Space separted values --> we need to give one space after each object
names = input("enter the names:").split()
print(names)
print(type(names))

#comma Separted Values
subjects = input("enter the subjects:").split(',')
print(subjects)
print(type(subjects))


#multiple values (more than one)strings
#make sure to match the argumentss

name,batch = input("enter the details:").split()
print(name)
print(batch)



#multiple integer values

order_id,cost = map(int,input().split())
print(order_id)
print(cost)

#we want to take subjects marks
p_marks,ap_marks,ss_marks = map(float,input().split())
print(p_marks,ap_marks,ss_marks)


#Group of integers,float values

stu_marks= list(map(int,input("enter the marks:").split(',')))
print(stu_marks)


discounts = list(map(float,input("enter the discounts:").split(',')))
print(discounts)

#Accept the cost of selling the product from user
original_amount = float(input("enter the original_amount:"))
selling_amount = float(input("enter the selling_amount:"))
print = selling_amount - original_amount
print(profit)


#set of integers
#set of float values -->replace int with float
ids = set(map(int,input("enter the ids:").split(',')))
print(ids)
print(type(ids))          


#passing list() as input using eval()
#u can directly pass same as list,tuple,set data as it is
list_data = eval(input("enter the list values"))
print(list_data)
tuple_data = eval(input("enter the tuple values"))
print(tuple_data)
print(len(tuple_data)
set_data = eval(input("enter the set values'))
print(set_data)
print(len(set_data)

#passing dict data using eval

stu_details = eval(input("enter the data:"))
print(stu_details)


#output formatting -->print()
a,b,c= map(str,input("enter the names:").split())
print(a,b,c)
#now we will use sep --> sep is the keyword
print(a,b,c,sep="----")
print(a,b,c,sep=":",end='\p')
print("phaneswar","vizag",end=" ")
print(34,4.5)


#1) using commas in print()
name = "codegnan";branch = "vizag";batch = 'pfs-vsp-007'
print(name,"is in",branch)
print(batch,"belongs to",branch,"branch")

#2) using %(modules) formatting -->old style c programming
#%d --> integers,%f -->float,%s -->strings
age = 32
price = 45.256
place = "vizag"
print("age =%d | price = %f | place = %s"%(age,price,place))
print("price is %.f"%price)
print("print is %.2f"%price)



#3) usage of string formatting --> str. format()

name='codegnan';branch ='vizag';age=8
print("{} is in {}and itis of {} years in  edtech industry".format(name,branch,age))
a,b=2,45
print("{},{}".format(a,b))
print("the value of a={} and the value of b={}".format(a,b))

#4) f-string notation -->
name='codegnan';branch ='vizag';age=8
print(f'{name} is in {branch}')

'''
