import random as r

password ="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+><:"
length_password =int(input("Enter the password length: "))
a ="".join(r.sample(password,length_password))
print(a)
