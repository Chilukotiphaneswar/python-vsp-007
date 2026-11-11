'''
Usage of fro  with conditional stsatements


notifications = [0,0,1,1,0,0]
#0 -->Notfication read
#1 -->unread notification
#Notification checker
for notification in notifications:
    #you need to map condition
    if notification ==1:
        print("Unread Notification")
       
else:
    print("All Notifications are caught up")


#break -->terminate the loop
notifications = [0,0,1,1,0,0]
#0 -->Notfication read
#1 -->unread notification
#Notification checker
for notification in notifications:
    #you need to map condition
    if notification ==1:
        print("Unread Notification")
        break


#Searching in a list
#You want to handle the "item not found" case

fruits = ["apple","banana","kiwi","cherries"]
item = input("which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        break
else:
        print(f'could not find {item} in the fruits')


#Continue -->ArithmeticError will skip the current iteration and proceeds for the
#rmng iteration
fruits = ["apple","banana","kiwi","cherries"]
item = input("which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        continue
else:
        print(f'could not find {item} in the fruits')


notifications = list(map(int,input("enter the values:").split(',')))
print(notifications)
for notification in notifications:
    #you need to map condition
    if notification ==1:
        print("Unread Notification")
        #continue
        break
else:
    print("All notifications are Caught up")


#while --> loops


while <condition>:
     statement(s).........
     ............
     
while True:
     print("yes")

#initalizer with which we need to initalise

i = 0
while i<=10:
     print(i)
     i = i+1
#get the counter from 10 to1 using while
i = 10
while i>= 1:
     print(i)
     i = i-1     
'''
i=1
while i<=8:
     print(8-i)
     i = i+1
