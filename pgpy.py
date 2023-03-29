import random

alphabets = 'abcdefghijklmnopqrstuvwxyz'
small = list(alphabets)  # make a list of capital and small chars
capital = list(alphabets.upper())
nums = [str(i) for i in range(10)]  # make a list of symbols and numbers
symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-','+', '=']

# input number of the chars needed
n_small = int(input('Number of small chars: '))
n_capital = int(input('Number of capital chars: '))
n_symbols = int(input('Number of symbols : '))
n_nums = int(input('Number of numbers : '))

password = ""
# choose sample random numbers from each list baesd on inputs
for i in range(1, n_small + 1):
    rands = random.choice(small)
    password += rands
for i in range(1, n_capital + 1):
    randc = random.choice(capital)
    password += randc
for i in range(1, n_symbols + 1):
    randsy = random.choice(symb)
    password += randsy
for i in range(1, n_nums + 1):
    randn = random.choice(nums)
    password += randn
print('-' * 15)
print(f'the raw shape of pass is {password}')
print('-' * 15)

# shuffle the password
shuff = random.sample(password, len(password))
password = ''.join(shuff)

print('-' * 15)
print('Final pass: ', password)
print('-' * 15)

# TODO:
# 1. make a file and save pass
# 2. write a message for pass to remember it
# 3. hashing the passes
# 4. encrypting file
# 5. gui