import random #to import random charactor from standard library
print('==================== Password Generator ==================== ') #it will say on the top what we doing
chars1 = 'abcdefghijklmnopqrstuvwxyz' #it will pic a random character from here
chars2 = 'ABCDEFGHIJKLMNOPQURSTUVWXYZ'
chars3 = '0123456789'
chars4 = '~!@#$%^&*()_+'
password1 = random.choice(chars1) #running the random modeuel and generating random characters and storing it to password
password2 = random.choice(chars2)
password3 = random.choice(chars3)
password4 = random.choice(chars4)
password = f'{password1}{password2}{password3}{password4}' #using f string to combine all of those together
print ("Your new random password is: ", password)
