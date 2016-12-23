import random
import io
import sys

def addNum(fNum, sNum):
    sumNum = fNum+sNum
    return sumNum

print(addNum(3,5))

print("What is you name?")
name = sys.stdin.readline()

# name = str(input("what is your Name?"))
print("Hello", name)

long_string ='i\'ll catch you if you fall- the floor'
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4]+'be there')
print('%c is my %s letter and my number %d is %0.5f'%
      ('X', 'favorite', 1,.15))
print(long_string.capitalize())
print(long_string.find("floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace('floor','Ground'))
print(long_string.strip())
quote_list =long_string.split(" ")
print(quote_list)