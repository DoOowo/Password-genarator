import random

syb = ['!', '$', '%', '?', '<']
alphabet_lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
alphabet_uppercase = [string.upper() for string in alphabet_lowercase]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


pass_length = random.randint(8, 12)
big_ass = [syb, alphabet_lowercase, alphabet_uppercase, num]
pswd = ""
for i in range(pass_length ):
    tip = random.randint(0, len(big_ass)) - 1
    element = random.randint(0, len(big_ass[tip])) - 1
    pswd_elmn = big_ass[tip][element]
    pswd = pswd + str(pswd_elmn)
print(pswd)

