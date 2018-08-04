#write a python program that asks a user for a log in name nad password ,that when they type ub  lock they need to type in their name and password to unlock it
import sys
print ("Username = Username\n Password = password\n type exit to close program\nDeveloper victorkosgei254@gmail\n")

user_name = 'Username'
user_password = 'password'

def login():
	user_name2 = input("Enter Username :")
	user_password2 = input("Enter Password :")

	while (user_name2):
		if(user_name2 == user_name and user_password2 == user_password):
			print ("Program running")
			flag = input('>')
			if flag == 'lock':
				login()
				break
				print ("Loop Break")
			elif flag == 'exit':
				sys.exit()

			else:
				continue
		else:
			print ("Wrong Username or Password")
			login()
			break

login()
