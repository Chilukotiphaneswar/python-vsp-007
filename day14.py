'''

best=int(input("enter the saller amoung:"))
if best>1000:
    print("best seller")
else:
    print("No 0utput")

n=bool(input("enter the value:"))
if n:
    print("Extra Rain Charges Applied")
else:
    print("No output")


z=int(input())
if n>99:
    print("final bill amount:"f'{z}')
else:
    print("final bill amount:"f'{z+30}')


Plan=int(input("Enter amount:"))
if Plan>10000:
    print("Trip")
elif Plan>5000:
    print("Resort Stay")
elif Plan>3000:
    print("Movie and Dinner")
elif Plan>1000:
    print("Cafe and Shopping")
elif Plan>500:
    print("Street Food and Park Visit")
else:
    print("Stay Home")


#Repetitions Statementss (Loops)-->Lopps helps us in automating repetitive



syntax:
for <temp> in collection/renge:
    statement(s)...
    ..............
    ..............

marks=[25,20,21,13,10,12]

#Marks can be dynamic
marks = list(map(int,input("enter the marks:").split(',')))
for i in marks:
    print(i)

marks = list(map(int,input("enter the marks:").split(',')))
total=0
for mark in marks:
    total=mark + total
    print(total)
print(f'Total marks are:{total}')
print(f'Avg marks are:{total/len(marks)}')



details={'ids':[121,123,124],
         'marks':[25,20,21]}
for data in details:
    print(details[data])
for data in details.values():
    print(data)
for key,value in details,items():
    print(key,value)

'''
