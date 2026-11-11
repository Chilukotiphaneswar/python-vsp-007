'''
#task: create a nested list with lists and strings and perform list methods

#copy(),sort(),reverse()

details = [['sanjay','python',50],
           ['akash','flask',45],
           ['vinay','aptitude',30]]
print(details)
print(len(details))

#copy()
data = details.copy()
print(data)
print(len(data))


data[0].append("a")
data.append("vizag")
print(data)
print(len(data))
print(details)
print(len(details))

data.extend(["pfs","jfs"])
print(data)
print(len(data))
print(details)
print(len(details))



details.extend(["hyd","vizag","vij","codegnana"])
print(len(details))
print(len(data))

subjects = ['python','mysql','aptitude','softskills']
data = subjects.copy()
print(data)


data.insert(2,"frontend")
print(data)
print(subjects)


data = subjects
data.insert(2,"frontend")
print(data)
print(subjects)
subjects.remove("python")
print(subjects)
print(data)

#sort() reverse()

marks = [12,15,20,24,21]
marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.append("phaneswar")
marks.sort()
print(marks)

marks.extend([-23,12,87])
print(marks)
marks.sort(reverse=True)
print(marks)

print(marks)
marks.reverse()
print(marks)
marks.extend(['poll','sunday',123])
marks.reverse()
print(marks)
print(marks[::-1])

#min(),max(),len(),type(),sorted()
marks = [20,12,23,25,30]
print(marks)
print(min(marks))
print(max(marks))
b=sorted(marks)
print(b)
print(marks)


#Tuples-->Tuples are Immutable,Ordered,Indexed,Collection,it can also have
#duplication, we use() to store the data

data =()
print(type(data))
print(len(data))

data =1,2,3,4
print(data)
print(type(data))
#data[-2]= 'codegnan' it is not possible
#nested tuples (also will have list in it)



details = ("vizag",8,("pfs","jfs","da"),["aptitude","softskills"])
print(len(details))
print(details[:2])
print(details[2][1])
print(details[2][::2])

print(details[-1])
details[-1].extend(['python','java'])
print(details)

print(details[0].upper())
print(details)


#indexing,slicing,repetition,merging are possible

temp = (23.5,24,34.5)
b=temp*2
print(b)
print(b + temp)

#tuple methods -->index(),count()
data = (12,3,24,3,12,4,5)
print(data)
print(data.index(3))
print(data.index(3,2))
print(data.count(3))

b = sorted(data)
print(tuple(b))
c = tuple(sorted(data,reverse=True))
print(c)

'''
#sets: A set is an unordered,unique,mutable collection.it well never allow the duplicates

id=set()
print(id)
print(type(id))

names = {'phane','ganesh',22,3,'ganesh',24}
print(names)
print(len(names))

#d = {12,3,4,[12,3,4],45}
#print(d)

d = {12,3,4,(12,3,4),45}
print(d)

#Tack : create a nested tuple with lists inside it and make all methods of lists in the Tuple.
