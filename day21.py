'''
#Variable length arguments ---> We can capture any number of positional
#arguments, we use (*args), captures excess positional arguments and pack them into _
#pack them into tuple....

def sample(*a):
    #usage of arbitary arguments
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample('sanketh','codegnan')
sample([12,3,4,5])

#In above case we used 'e' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c=2,4,5,6,65,12,-12
print(a)
print(c)
print(b)
#a,*b,*c=2,4,5,6,65,12,-12
print(a)
print(b)
print(c)


#find the sum of values
def add (*a):
    #print(a)
    #print(type(a))
    result = 0
    for value in a:
        if type(value) in (int,float):
        #if type(value) == int or if type(value) == float:
            result = result + value
    #print(result)
    return result
#add()
#print(add(1,3,4,5))
#print(add(12,3,4,5,6-98,12))

print(add(1,2,4,-2,'codegnan',2,12,'phaneswar'))

#what if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d))



#we will use above usage of variable length arguement for ordering pizza

def order_pizza(size,*toppings):
    print(f'Size of pizza is {size}')
    #print(f"toppings:{toppings}")
    for topping in toppings:
        print(f'topping added : {topping}')
order_pizza("large","onions","panner","capsicum","olives","mushrooms")


#keyword variable length arguments:any number of keyword arguments,
#date is stored in dictionary,we use **kwarge...

def sample(**a):
    print(a)
    print(type(a))
sample()
sample(name="vinay",batch="pfs-vsp-007",place="vizag",branch="cse",course="pfs")


def order_pizza(size,*toppings,**details):
    print(f'Size of pizza is {size}')
    #print(f"toppings:{toppings}")
    for topping in toppings:
        print(f'topping added : {topping}')
    for key ,value in details.items():
        print(f'data is{key},result is {value}')
order_pizza("large","onions","panner","capsicum","olives","mushrooms",
            name="phaneswar",
            bill=200,
            delivery=False,
            tip=100)
'''
