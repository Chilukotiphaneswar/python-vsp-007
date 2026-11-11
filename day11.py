'''

#every can contion only tuples in the but not lists,sets..
we use set() or data inside {} braces

subjects = set()
print(type(subjects))
print(len(subjects))
data = ('python','aptitude','sql','ss')
subjects = set(data)
print(subjects)
print(len(subjects))

ids = {123,125,126,129,ArithmeticError['poll',123]}


#set properties -->membership
print(124 in {124,123,125})
ids = {123,121,125}
new_ids = {126,127}
#total = ids + new_ids #Typeerror
#print(total)


#set is a mutable collection -->methods -->insertion,deletion along
#with mathematical set operations

marks = {45,25,35,20,21}

print(type(marks))
print(len(marks))
marks.add(250)
print(marks)
print(len(marks))
marks.add((12,13,15))
print(marks)

d_marks = [10,5,3,4,6]
marks.update(d_marks)
print(marks)
print(len(marks))
marks.update("codegnan")
print(marks)
print(len(marks))

#remove(),discard(),pop()
print(marks.remove(45))
print(marks)
#print(marks.remove(4))

print(marks.discard(45))
print(marks.discard(12345678))

marks.discard(20)
print(marks)
#pop()
print(marks.pop())
print(marks.pop())
print(marks.pop())

#clear()
marks.clear()
print(marks)



#mathematical set operation -->union(),intersection(),difference()...

a1 = {12,34,23,45}
a2 = {3,45,23,12}

a3 = a1.union(a2)
print(a3)
print(len(a3))
a4 = a1 | a2
print(a4)
a5 = a1.intersection(a2)
print(a5)
print(len(a5))
a6 = a2 & a1
print(a6)
a7 = a1.difference(a2)
print(a7)
a8 = a2 - a1
print(a8)
a9 = a1.symmetric_difference(a2)
print(a9)
a10 = a2 ^ a1
print(a10)



#intersection_update()
a3 = a1.intersection_update(a2)
print(a3)
print(a1)
#difference_update(),symmetric_difference_update()
a4 = a1.difference_update(a2)
print(a4)
print(a1)
a5 = a1.symmetric_difference_update(a2)
print(a5)
print(a1)

print(a1,a2)
a1.add(3)
print(a1,a2)

print(a1.issuperset(a2))
print(a2.issubset(a1))
print(a1.isdisjoint(a2))

#Dictionaries : A Dictionary is a collection of key,value pairs,we use {k:v} as syntax,
#key must be unique,mutable, ordered,indexed 

data = {1:'vinay',
        2:'vijay',
        3:'ajay'}
print(data)
print(type(data))
print(len(data))
print(data[2])
print(type(data[1]))

'''   

details = {'ids':['cgvi0242','cgvi0249',
                  'cgvi0224','cgvi0240'],
           'name':['nikitha','deepthi',
                   'vinay','tej' ],
           'batch':'pfs-vsp-007',
           'place':('vizag','vjwda','hyd','bnglre',),
           'subjects':{'python','aptitude','softskills'}}
print(details)
print(len(details))
print(details.keys())
print(details['ids'])
print(type(details['ids']))
details['ids'].append("cgvi0245")
print(details['ids'])
details['ids'].insert(3,"cgvi0247")
print(details['ids'])
print(details['ids'][:3])
print(details['ids'][::2])

#Task : 1)Insert raju at the end also sanju and nihanth at the end in names
        2)Update subjects with sql,flask,fastapi
        3)remove bnglre and vizag from place
        4)convert batch number to lowercase


