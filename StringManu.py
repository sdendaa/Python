import random

# remove the values from the message
VOWELS = ("a", "e", "i", "o", "u")
message = input("Enter your massage?")
new_message = ""
for letter in message:
    if letter not in VOWELS:
        new_message += letter
    else:
        temp = random.choice(VOWELS)
        while temp == letter:
            temp = random.choice(VOWELS)
        else:
            new_message += temp

print(new_message)

string ="the quick brown fox jumped over the lazy dog"
string = list(string)
print(string)

jumbled =""
print("string before ", string)
print("Jumbled before ", jumbled)

for letter in range(0, len(string)):
    jumbled += string.pop(random.randint(0, len(string)-1))
print("string after", string)
print("Jumbled after", jumbled)

# encrypted the message(Shifted encryption) using my dictionary
letters={"A": "E", "B": "F", "C": "G", "D": "H", "E": "I", "F": "J", "G": "K", "H": "L",
         "I": "M", "J": "N", "K": "O", "L": "P", "M": "Q", "N": "R", "O": "S", "P": "T",
         "Q": "U", "R": "V", "S": "W", "T": "X", "U": "Y", "V": "Z", "W": "A", "X": "B",
         "Y": "C", "Z": "D"}
# message = input("Enter your message to encrypt?").upper()
# encrypted = ""
#
# for letter in message:
#     if letter in letters:
#         encrypted += letters[letter]
#     else:
#         encrypted += letter
#
# print(encrypted)
#     # using chr(letter) and ord(ASCII value)
# message = input("Enter your message to encrypt?").upper()
# encrypted = ""
#
# for letter in message:
#     if letter == ' ':
#         encrypted += letter
#     elif ord(letter)+5 > ord("Z"):
#         encrypted += chr(ord(letter) + 5-26)
#     else:
#         encrypted += chr(ord(letter)+5)
#
# print(encrypted)

# using index of letter
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWYZ"
message = input("Enter your message to encrypt:").upper()
encrypted = ""
print(len(ALPHABET))

for letter in message:
    if letter == " ":
        encrypted += letter
    elif ALPHABET.index(letter)+5 > len(ALPHABET):
        encrypted += ALPHABET[(ALPHABET.index(letter)+5)-26]
    else:
        encrypted += ALPHABET[ALPHABET.index(letter)+5]

print(encrypted)
