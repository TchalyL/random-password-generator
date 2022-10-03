import string
import random


# all characters we wish to generate the password from 
chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# function to generate password
def generate_password():
  pwd_length = int(input("Password Length (characters): "))

  random.shuffle(chars)

  pwd = list()

  # Creates a random password based on the pwd_length given
  for _ in range(pwd_length):
    pwd.append(random.choice(chars))

  random.shuffle(pwd)

  pwd = "".join(pwd)

  print(pwd)


option = input("Generate random password? (y/n): ").lower()

if option == 'y':
  generate_password()











