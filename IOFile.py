import random
import sys
import io
import os
# to write into the file
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file \n", 'UTF-8'))
test_file.write(bytes("Python is so funny language to learn!!:) \n", 'UTF-8'))

test_file.close()
# to read from the file
test_file = open("test.txt", 'r+')
test_in_file = test_file.read()

print(test_in_file)

os.remove("test.txt")#remove the file