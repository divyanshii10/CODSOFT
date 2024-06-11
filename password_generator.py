#INSTRUCTIONS:
# 1. Easy -> password includes lowercase and uppercase letters.
# 2. Medium -> password includes lowercase, uppercase letters and digits.
# 3. Hard -> password includes lowercase, uppercase letters, digits and special characters.
# 4. Minimum length of password is 3.

import random
import string

def pass_generator(l,c):
       
    if l<=3:
        return 'Please enter valid length! Minimum length of password is 3.'

    if c == 'easy':
        p = string.ascii_lowercase + string.ascii_uppercase
    elif c == 'medium':
        p = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif c == 'hard':
        p = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        return 'Invalid complexity! Please enter a valid complexity (easy,medium or hard).'
    
    password = ''.join(random.choice(p) for i in range(l))
    return password

print("\n----Welcome to my mini Project 'Password Generator'----\n")
try:
    l = int(input('Enter the length of password you want:'))
except ValueError:
       print('Invalid input! Please enter a integer number.')

c = input('Enter the complexity of password (Easy, medium or hard):').lower().strip()
result = pass_generator(l,c)
print('Your Password is: ',result)
