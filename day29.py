'''
#a,b = map(int,input("enter the values:").split())
#print(a,b)
try:
    a,b = map(int,input("enter the values:").split())
    print(a,b)
    result = a/b
    print(f'answer is {result}')
except exception as e:
    print(f'error is {e}')

#Multiple Except Blocks
try:
    a,b=map(int,input("Enter the values:").split())
    #print(a,b)
    result=a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Sarigga chusi rayu")

try:
    subjects=['Python',45,'AI',30]
    #print(subjects[5])
    subjects.append("SQL")
    print(subjects)
except Exception as e: #this can be written if u want exception to take 
    print(e)
except IndexError:
    print("Make sure to check the spelling")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("anyway this will be printed...")

#catching multiple exceptions together
try:
    value = int(input("enter a value:"))
    result = 10/value
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occured:{e}')


#Raising exceptions
#you can raise exception intentionally using rasie keyword
value = 15
if value < 0:
    raise ValueError("value cannot be negative")
else:
    print("Done")

Custom Error Messages:
try:
    raise exception("custom error message")
except Exception as e:
    print(e)

try:
    value = -15
    if value < 0 or value in [1,20]:
        raise Exception("value cannot be negative")
except Exception as e:
    print(e)


#FILE HANDLING --> OPEN()
file and directory operations are essential to store the data..
PYTHON  provides build-in funcation -->open()

#mode of operations -->'r','w','r+','w+'
open(filename,mode) #default mode is 'r'
'''
file = open('rrr.txt',"r")
print(file)
#print(file.read())
print(file.readline())
print(file.readlines())

    

