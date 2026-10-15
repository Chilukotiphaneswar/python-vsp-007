'''
Sequences -->String,lists,tuples,sets,frozensets,dicts

strings  --> A string is a group of charaa=cters,it is an immutable


data = '' #empty string
print(type(data))
print(len(data))

#operations -->
sub1 = "python"
sub2 = "mysql"
print(sub1+sub2)

print(f'{sub1},{sub2}')
print(sub1+" <--> "+sub2)


#repetition --> String can be repeated any number of items with avalid int

print("*")
print('*' * 10)
name = "phaneswar";place = "vizag"
print(f'{name * 20}*')
print(f'---->{name} is in --->{places}')



#mumbership --> in,not in
print("Phane" in "Eswar")
print("Phane" in "eswar")


#indexing
#Traversing the elements
name = "phaneswar"
print(name[6])
#Negative indexing
print(name[-9])

#slicing
m = "codegnan"
print(m[:])
print(m[2:6])
print(m[0:])
print(m[0:6])
print(m[:4])
print(m[:24])
print(m[24:])

print(m)
print(m[-1:])
print(m[-5:-1])
print(m[:-3])


p = "phaneswar"
print(p[:])
print(p[3:5])
print(p[0:4])

print(p)
print(p[-1:])
print(p[0:-4])


print(p)
print(p[1:-1])
print(p[-1:3])



#Task -->Create a string and explore above possibilties

#string -->[start:end:step]

s = "codegnan"
print(s[::1])
print(s[::2])
print(s[::3])


place = "visakhapatnam"
print(place[1:7:3])
print(place[2:6:5])
print(place[3:4:6])

print(place[::-2])
print(place[-6:-3:2])

print(place[::-1])# this helps to reverse the string order
print(place[::-2])# this skips one elements in reverse order
#you can explore all cases in string
print(place[1:9:-2])
print(place[-9:-1:1])

#Built in functions ---> len(),type(),min(),max(),ord(0,char(),stored()
password="admin123"
print(len(password))
print(type(password))
print(min(password))
print(max(password))
print(ord(password))

'''
