import random
import sys
import os


print("Hello World!!")

quote ="\"Always remember you are unique"
multi_line_quote ='''Just like everyone else'''

print("%s,%s,%s"%('I liked the quote', quote,multi_line_quote))

print("I don't like new Line ", end="")
print("new lines")



### the List
grocery_list =['tomato', 'lemonate', 'banana']
grocery_list[0] = 'juice'
print("first Item", grocery_list[0])
print(grocery_list[1:3])

other_list =['wash car', 'pick kids', 'cash check']
to_do_list =[grocery_list,other_list]
print(to_do_list)

print(to_do_list[0][1])
grocery_list.append("onion")
print(grocery_list)
grocery_list.insert(1, 'pickle')
print(grocery_list)
grocery_list.remove('pickle')
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)
del grocery_list[3]
print(grocery_list)
print(len(grocery_list))
print(max(grocery_list))

#tuple == if you don't want to change value

pi_tuple =(3,65,43,32,34)
new_tuple = list(pi_tuple)
print(new_tuple)

#dictionary==> key, value
print("Dictionary:")
super_villain ={'Fiddler':'Isaac Bowin',
                'Captian Cold':'Leonard Snart',
                'Weather Wizard':'Mark mardon',
                'Mirror Master':'Sam Scudder',
                'pied Piper':'Thomas Peterson'}
print(super_villain['Fiddler'])
print(super_villain)
del super_villain['Fiddler']
super_villain['pied Piper'] ='Hartley Rathaway'
print(super_villain)
print(len(super_villain))
print(super_villain.get('pied Piper'))
print(super_villain.keys())
print(super_villain.values())