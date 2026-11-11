'''

#range(stop)-->
for i in range(5):
    print(f'value of i is {i}')
    print(f'square of i is {i**2}')

#range(start,stop)-->u can mention start and stop postns(values)

for i in range(1,11):
    print(i,i**3)
    print('<------->')


#range(start,stop)--->
for i in range(1,21,1):
    print(i)
for i in range(1,21,2):
    print(i)
    

for i in range(2,21,2):
    print(i)
for i in range(10,0,-1):
    print(i)

for i in range(65,91):
    print(chr(i),end=' ')

names=['akash','kaushik','vijay','sanjay','lokesh']
for name in names:
    print(name,end=' ')

for i in range(len(names)):
    print(names[i])


# Ask integer input user and get the sum of numbersas per iput


n=int(input("enter the value:"))
result=0
for i in range(n+1):
    result=result+1
    print(f'result of {i} is {result}')
else:
    print("No Output")
'''
#Usecase: checking daliy workout app usage
work_log=[1,1,1,0,1,1,0]
longer_streat=0
current_streat=0
for day in work_log:
    if day==1:
        current_streat=current_streat+1
    if current_streat>longer_streat:
            longer_streat=current_streat
    else:
        current_streat=0
print(f'Longest streat is {longer_streat}')
            

