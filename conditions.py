import random
import sys
import io

age = 30

if age>=21:
    print('''you are old enough to drive a tractor trailer''')
elif age >=16:
    print('you are not old enough to drive car')
else:
    print("you are not old enough to drive")

    # logical operator

if((age >=1)and (age <=18)):
    print('You get a birthday, Okay')
elif((age ==21) or (age >= 65)):
    print("you get a bithday")
elif not(age ==30):
    print("You will not get a birthday")
else:
    print('You get a bithday party')

    # looping
for x in range(0,10):
    print(x, ' ', end='')
print('\n'*3)
grocery_list =['bread','banana','onion','juice']
for y in grocery_list[0:3]:
    print(y,',', end='')
print(grocery_list[3])

num_list =[[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

        #random number generator
print("Random numbers:")
random_num = random.randrange(0,20)

while (random_num != 10):
    print(random_num)
    random_num =random.randrange(0,50)
print("While, continue and break")
i = 0
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i +=1
        continue
    i +=1