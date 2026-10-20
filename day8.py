'''
#String Methods --->CAse Conversions,replacing,Finding,White Trailing Spaces,Testing Methods,
alignment Methods
#Case Conversions --->Upper(), Lower(), Title(), capitalize(),swapcase()

data="CodeGnan"
print(type(data))
print(dir(data)) #dir() returns the avaliable method functions

#Upper() ---> Converts object to uppercase
print(data.upper())
e=data.upper()
print(e)

#Lower() ---> coverts objects to lowercase
a="Phaneswar"
print(a.lower())
print(type(a))

#Capitalize ---> It will Capitalize the  first letter in the Word
print("ganesh is a good boy".capitalize())

#Title ---> IT will capitilize every First letter in each Word
print("ganesh is a good boy".title())

#Swapping ---->converts uppercase to lower and lower and upper
print("coDEgna".swapcase())


#Testing Methods (which will give the result as Boolean(True /False)
#isupper(), islower(), isalnum(), isdigit(),isalpha(),startswith(),endswith()....

print("phane234".isupper())
print("phane234".islower())
print("phane123".isalnum())#returns true when we have all alphabets
print("phane89".isalpha())#returns true for an aplhanumeric string
print("phane123".isdigit())#because this all are not digits 
print("1234".isdigit())
print("phane".istitle())
print("phane dd".istitle())#Returns false


data="python Aptitude"
print(data.startswith("A"))
print(data[7:].startswith("A"))
print(data.startswith("A",7))
print(data.endswith("e"))
print(data[-1].endswith("e"))
print(data.endswith("n",0,6))
print(data.endswith("u",0,13))


#Finding and Searching Methods --->find(),index(),Count()

data = "codegnan is in vizag"
print(data.find("a")) #returns only the first Occurance
print(data.find("a",7))#returns we will check for the next occurances
print(data.find("u"))#returns -1 the given object is not found
print(data.rfind("a"))#returns the last occurence
print(data.index('a'))#returns the first occurance
#If given object is not present in raise ValueError
print("querty".index("uerty"))
print("phaneswar".index("s"))


#Rindex() returns the last occurance
print("phane".rindex("a"))
#print("phane".rindex("s")) it will raise Error

#Count() Will Return total number of occurances
print("phaneswar".count("a"))
print("phaneswar".count("w"))#it will give 0 as result because n is not present in the given word


#Split(),Join() ,STrip(), Lstrip(), Rstrip(),zfill()

a="phaneswar ganesh karthik"
b=a.split()
print(b)
a="phaneswar ganesh.karthik"
c=a.split(',')
print(c)


#Join()
print("code".join("gnan"))#Concatenates every object with the given iterables
print("*".join("phaneswar"))
print(" @_# ".join("phaneswar"))


#White Space & Trimming methods --->Strip(),lstrip(),rstrip()

a=" phane "
print(len(a))
print(a.strip())
print(a.lstrip())
print(a.rstrip())


#Alignment Methods --->Zfill() (make sure to pass the width >len(obj))

print("phane".zfill(6))#here it will fill 00 infornt because it is 4 length we are asking to fill 6
print("phane".zfill(1))
print("phane".center(10,"@"))
print("phane".rjust(10,"#"))
#returns the right justified 
print("phane".ljust(10,"&"))
#returns the Left justified

'''
