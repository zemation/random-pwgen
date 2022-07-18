import character_list
import random


print("Welcome to the PyPassword Generator!")
user_letters= int(input("How many letters?\n")) 
user_symbols = int(input(f"How many symbols?\n"))
user_numbers = int(input(f"How many numbers?\n"))

password = []

for item in range(1, user_letters + 1):
  password.append(random.choice(character_list.letters))
for item in range(1, user_symbols + 1):
  password.append(random.choice(character_list.symbols))
for item in range(1, user_numbers + 1):
  password.append(random.choice(character_list.numbers))

random.shuffle(password)
print(''.join(password))