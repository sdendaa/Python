import random


count = 1
guess = int(input("Guess the number between 0 to 100: "))
num = random.randrange(0, 100)
while guess != num:
    if guess > num:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess the number between 0 to 100: "))
    count += 1
print("wow! you guessed the right number after ", count, "attempts")
