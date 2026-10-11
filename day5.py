'''
operators -->operators help us to perform operations between operands

Arithmetic operators  -->+,-,*,/,**,//(Integer or floor division),
%(modulus -->remainder)

Assignment opertors -->it helps to assign ,update (increment),decrement values
# = (assiging),





data = 20
print(data)
print(type(data))

stock = data
print(stock)

#increment the value of stock
stock = stock + 5
print(stock)
print(data)


#decrement the value of data by 2 values
data = data-2
print(data)
data = data*2
print(data)
data = data%2
print(data)
data = data/2
print(data)
data = data//2
print(data)
data = data**2
print(data)


stock = 100
stock**=2
print(stock)



#comparision operators (relational operators) -->It performs comprision
#between the operands and results in boolean trun /false -->conditions
# ==, != , <,<=,>,>=
name = 'vinay'
vinay_attendance = 75

print(vinay_attendance ==80)
print(vinay_attendance >80)
print(vinay_attendance >=80)
print(vinay_attendance <80)
print(vinay_attendance <=80)
print(vinay_attendance !=80)


#logical operators -->and , or, not (keywords)
#and --> it needs all conditions to be satisfied (two or more)
#or --> it needs any one condition  to be satisfied
#not -->opp to existing


max_marks = 80
vinay_marks = 75
max_att = 75
vinay_att = 70

vinay_marks +=10
certificate = vinay_marks >= max_marks and vinay_att >= max_att
print(certificate)
chance = vinay_marks >= max_marks or vinay_att >= max_att
print(chance)
data = []
print(data)
print(not(data))#returns true
data = [12,3,4]
print(not(data))#returns false

#Both logical and comparision operators will return result in Boolean



#Membership operators -->in,not,in

names = ['vinay','vijay','balakrishna','raju']

name = 'ajay'
print(name in names)#returns false
print(name not in names)#returns true
print('12' in '121')
#print(12 in 121) #TypeError



print('ajay' in 'ajay ,kumar')#returns true
print(['ajay'] in ['ajay'])#returns false



#Identity operators -->It specifically refers to the object (memory locations)
#id -->ArithmeticError is,is not

a = 15
b = 15
print(a==b)
print(id(a))
print(id(b))
c = a
print(id(c))

print(c is a)#as id of both a and c are same->true



a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(id(a))
print(id(b))
#as we have taken two lists evnthough with similar values identity
print(a is b)

c = a
print(id(c))
print(c is a)#returns true



a = (1,2,3)
b = (1,2,3)
print(id(a),id(b))
print(a is b)

#whene.we check with the interpreter mode and scripting mode above
#tuple result changes

#Logical,membership,identity,comparision (relational) -->always result is in boolean


'''

bitwise operators -->it perform bitwise operations -->&(bitwise and)
#j (bitwise or) ^ (bitwise xor)
#an integer will be converted binary format and performs bitwise operation
#following integer to binary conversion

print(7&3)
print(7|3)
print(7^3)


