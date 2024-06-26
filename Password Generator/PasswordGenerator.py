import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "(){}[],:;.^_-/\\?+*#"

upper, lower, nums, syms = True, True, True, True

length = int(input("Enter the length of password to be generated: "))
amount = int(input("Enter the number of variations to be produced: "))

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

generated_passwords = []
for x in range(amount):
    password = "".join(random.sample(all, length))
    generated_passwords.append(password)

print(f"The generated passwords are:\\n")
for password in generated_passwords:
    print(password)


