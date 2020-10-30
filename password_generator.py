import random

number = 10
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&()?0123456789'
length = random.randrange(16)

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)