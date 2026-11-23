'''
#pass by reference--> when mutable objects (lists,sets,dict) are passed into functions
#the function,changes inside the function afferts the original object..

def update(items):
    """we will assume items as list"""
    #items.append("laptop")
    items.extend(["loptop","power bank","camer"])
cart = ["mobile","watch"]
print(update(cart))#returns nonn
print(cart)#original list changes
#print(update("phaneswar")#raises attribute error


#Dictionary usage -->updating profile
def update(profile):
    """usage of dictionary"""
    profile['branch']="vizag"
students = {'names':["vijay","ganesh"]}
pfs_students={'batches':['pfs-vsp-007','pfs-vsp-006'],
              'subjects':['python','mysql','aptitude']}
update(students)
print(students)
update(pfs_students)
print(pfs_students)

#pass by value -->original data will not change,immutable objects
#pass by object reference--> original data will change,mutable objects


#Built-in funcations -->Funcations which are inbuilt in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str()
#list(),tuple(),set(),dict(),input(),eval(),help()

#print(dir(__builtins__))#returns list of builtin 
#print(help(print))
#print(help(len))

#abc(),chr(),ord()
print(abs(-34)) #returens the absolute value of a number
print(chr(78 ))
print(ord('@')) #returns the ASCIT value
data = [24,56,78,0]
print(any(data))
print(all(data))
#print(all(None))
print(all([None]))
print(bin(17))


print(help(enumerate))

data=["phaneswar","ganesh","vijay"]
c = dict(enumerate(data))
print(c)

d=dict(enumerate(data,1))
print(d)



#zip-->it cobines multipe collections into a single collection
data = ["phaneswar","ganesh","karthik","dinesh","bharat"]
marks=[25,20,23,21]
f = dict(zip(data,marks))
print(f)

'''
