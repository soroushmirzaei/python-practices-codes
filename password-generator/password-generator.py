import string 
import numpy as np

pass_len = int(input("Password Length: "))
pass_type = int(input("Password Type\n\t1 Strong (Digits, Characters & Special)\n\t2 Medium (Digits, Characters)\n\t3 Week (Digits)\n"))
if pass_type in [1,2]:
	char_type = int(input("Characters Type\n\t1 Upper Case\n\t2 Lower Case\n\t3 Multiple Case\n"))
	char_letters = [string.ascii_uppercase, string.ascii_lowercase, string.ascii_letters][char_type - 1]

if pass_type == 3:
	ls = list(string.digits)
elif pass_type == 2:
	ls = list(string.digits)+list(char_letters)
elif pass_type == 1:
	ls = list(string.digits)+list(char_letters)+list(string.punctuation)

pass_gen = ''.join(np.random.choice(ls,pass_len))
print(f'Password: {pass_gen}')
