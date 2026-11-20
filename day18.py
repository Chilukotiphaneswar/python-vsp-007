'''
for i in range(3):
    for j in range(2):
        print(f'i={i},j={j}')

#for every outerloop inner loop will be completely executed...
#outerloop-->row-->inner loop-->columns

for i in range(2):
    for j in range(4):
        print(i,j)
'''
#Number Patterns-->row based number patterns,column based number patterns..
'''
1 2 3
1 2 3
1 2 3

num =1
for i in range(1,4):
    for j in range(1,4):
        #print(i,j)
        print(num,end=' ')
        num = num+1
    #print()

#Square pattern-->*with n rows add columns ->Solid rectangle
n= int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
'''
n=int(input("enter the value:"))
for i in range(1,4):
    for j in range(1,10):
        print(i,end=' ')
    print()
    
