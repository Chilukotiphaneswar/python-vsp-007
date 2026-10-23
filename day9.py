'''

Sequences --> Strings,Lists[],Tuples(),Sets set(),Dictionaries{}
List[] --> A List is a Ordered,Mutable,Indexed and heterogenous collection
it will be dynamic in size,allow duplicates


#Creation of lists
details = [123,"phaneswar",22,"pfs",75.5]
print(type(details))
print(len(details))
print(details)


#Nested Lists
batches = [["pfs","pfs-vsp-007","pfs-vsp-008"],
           ["da","da-vsp-007","da-vsp-008"],
           "vizag",8]
print(len(batches))
print(type(batches))

#indexing,slicing,striding
print(batches[0])
print(batches[-3])
print(batches[1:4])

print(batches[1:4])
print(batches[:2])
print(batches[1:5:2])
print(batches[-5:-1:4])

print(batches[0][1])
print(batches[2][3:])


#subindexing

print(batches[0])
print(batches[1][2:])
print(batches[1][2][-3:])
print(batches[1]*9)
a=a*73
print(len(b))


batches = [["pfs","pfs-vsp-007","pfs-vsp-008"],
           ["da","da-vsp-007","da-vsp-008"],
           "vizag",8]
print(batches)
print('vizag' in batches)
print('pfs' in batches)
print('pfs' in batches[0])


#list methods
data =[]
#print(dir(data))

#append(),extend(),insert()
data.append(24)
print(data)

#extend
datas=(1,2,3,'pfs')
data.extend(datas)
print(data)

#insert
data.insert(4,'vijay')
print(data)
data.insert(9,'dd')
print(data)



marks = [25,24,27,28,30,35,36]
print(marks)
marks[6] =['ganesh']
print(marks)
marks[:-4]=['dd']
print(marks)


#pop(),remove(),clear() ->removes elements from the list
subjects = ['python','aptitude','ss','mysql','flask',123]

#pop()
print(subjects.pop(2))

#remove()
subjects.remove(123)
print(subjects)

#clear()
subjects.clear()
print(subjects)

#index(),count()
marks = [1,2,1,3,4,5,6]
print(marks.index(1))
print(marks.index(1,2))

#count()
print(marks.count(1))
print(marks.count(248))

#task: create a nested list with lists and strings and perform list methods

#list methods

list = ["python",[1,2,3],"java",[4,5]]
print(list)

list.append(24)
print(list)

list = ['p','f','s']
list.extend(list)
print(list)

list.insert(8,'vijay')
print(list)

#pop()
print(list.pop(2))

#remove()
list.remove('vijay')
print(list)

#clear()
list.clear()
print(list)

'''
