'''
#Condition Statements -->Statements rely onthe condition


syntax if:

if<condition>:
    statement(s)....
    ...
   
#data = false
data = True
if data:
    print("welcome to codegnan")
    print("This is psf-vsp-007")
    print("Guys are good but thry will ccome late")


#mark = 25
mark = int(input("enter a value"))
marks = [12,14,13,25]
if mark in marks:
    print("marks successfully fetched")
    print(f'marks are {mark}')
    print(f'its done for the day')


#usage of else:

if <conditon>:
    statement(s)...
else:
    statement(s)...
   

stock = int(input("enter the value"))
total_stock = 100
if stock>0 and stock < total_stock:
    print(f'you can order the item')
    print(f'item selected and placed into cart')
    print(f'item ordered')
else:
    print(f'invalid entry')

algo:
    accept the input from the user
    make the eligility case as age greaterthanequal to 18:
        eligibility granted
        if age is not matching eligility:
            inform number of years to wait
dry run:
    age -->19 -->result -->19>=18 and 19>0
    age -->12 -->result -->18-12-->6
    age -->12 -->result -->18-(-12)-->30

#code
    
age = int(input("enter the age:"))
if age >0:
  if age>0 and age >=18:
    print(f'youy have eligibility')
else:
    print(f'wait to get vote eligibilty')
 else:  
    print(f'enter only +ve values for the age') 

#if-elif-else--> we wanted to map multiple conditions
if condition1:
statement(s)..
.........
elif condition2:
    statement(s)..
    ..............
    elif condition3:
        statement(s)..
        ............
        else:
            statement(s)
            ............


age = int(input("enter the age:"))
if age>0 and age >=18 and age <=100:
    print(f'you have eligibility')
elif age>0 and age<18:
         print(f'wait to get vote eligibilty')
else:
    print(f'invalid age entry')



#task -->placement eligibilty tracker/system
print("---------placement eligibility checker------")
name = input("enter the name of the student:")
attendance = float(input("enter the attendance of the student:"))
technical_score = float(input("enter the technical score:"))
mock_interview_score = float(input("enter the mock interview score:"))
projects = int(input("enter the number of projects"))

avg_score = (technical_score + mock_interview_score)/2
print("student name is:",name)
if attendance >=75 and avg_score >=75 and projects >2:
    print(f'result : student is placement ready he/she falls in hotlist')
elif attendance >60 and avg_score >=60 and projects >1:
    print(f'result : student needs more preparation -->improvement stage')
else:
    print(f'result : student is in foundation stage--> needs practice sessions')

'''    

