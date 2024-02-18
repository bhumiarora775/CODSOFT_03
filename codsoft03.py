import random
import string


password_length = int(input("Enter the desired length of the password: "))


use_uppercase = input("Do you want to include uppercase letters? (yes/no) ").lower() == 'yes'
use_numbers = input("Do you want to include numbers? (yes/no) ").lower() == 'yes'
use_punctuation = input("Do you want to include punctuation? (yes/no) ").lower() == 'yes'


if use_uppercase:
    char_set = string.ascii_uppercase
else:
    char_set = ''

if use_numbers:
    char_set += string.digits

if use_punctuation:
    char_set += string.punctuation

else:
    char_set += string.ascii_lowercase


password = ''.join(random.choice(char_set) for i in range(password_length))


print("Generated password: ", password)
