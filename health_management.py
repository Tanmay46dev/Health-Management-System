# --------------HEALTH MANAGEMENT SYSTEM - TANMAY PATEL--------------

# Assigning different keys for the clients
clients = {
	'1': 'Harry',
	'2': 'Rohan',
	'3': 'Hammad',
	'4': 'Tanmay',
	'5': 'Shubham'
}

# This function returns the current date and time
def get_date():
	import time
	localtime = time.asctime(time.localtime(time.time()))
	localtime = localtime.replace('  ', ' ')
	return localtime

# Asking the user to choose a client based on the keys we assigned earlier
def choose_client():
	print("Choose your client:\n\t")

	# Looping through  all the available keys and client names and printing them one by one
	for key, value in clients.items():
		print(f"Type ({key}) for {value}")

	name = input()
	# If the usre inputs a key that is not available in the above mentioned dictionary then handling the exception
	if name not in clients.keys():
		print(f"'{name}' is not a valid input")
		quit()
	else:
		return clients.get(name)

# Logging the values to the files of all clients respectively
def log():

	# This function logs the diet of the clients
	def log_diet():
		client = choose_client()
		print('What do you want to write?\n')
		content = input()
		# Opening the file of the client in append mode and adding the content to it
		with open(f"{client}_diet.txt",'a') as f:
			f.write(f"[{get_date()}]: {content}\n")

	# This function logs the exercise of the clients
	def log_ex():
		client = choose_client()
		print('What do you want to write?\n')
		content = input()
		# Opening the file of the client in append mode and adding the content to it
		with open(f"{client}_ex.txt",'a') as f:
			f.write(f"[{get_date()}]: {content}\n")

	# Asking the user what he wants to log betwwen the diet and the exercise
	print('What do you want to log?\n\tType (1) for diet\n\tType (2) for exercise')
	ans = input()
	if ans != '1' and ans != '2':
		print(f"'{ans}' is not a valid input")
	elif ans == '1':
		log_diet()
	elif ans == '2':
		log_ex()

# Retrieving the data stored in the files logged earlier
def retrieve():
	# This function retrieves the diet of the clients
	def retrieve_diet():
		client = choose_client()
		# If the user accidently tries to retrieve data from a file that doesn't exist then handling that exception
		try:
			# Opening the file of the client in read mode and reading the content in it
			with open(f"{client}_diet.txt") as f:
				print(f.read())
		except Exception as e:
			print(f"Your never logged in {client}'s file")

	# This function retrieves the exercise of the clients
	def retrieve_ex():
		client = choose_client()
		# If the user accidently tries to retrieve data from a file that doesn't exist then handling that exception
		try:
			# Opening the file of the client in read mode and reading the content in it
			with open(f"{client}_ex.txt") as f:
				print(f.read())
		except Exception as e:
			print(f"Your first need to log in {client}'s file")

	print('What do you want to retrieve?\n\tType (1) for diet\n\tType (2) for exercise')
	ans = input()
	if ans != '1' and ans != '2':
		print(f"'{ans}' is not a valid input")
	elif ans == '1':
		retrieve_diet()
	elif ans == '2':
		retrieve_ex()

print('Would you like to log or retreive?\n\tType (1) to log\n\tType (2) to retrieve')
ans = input()

if ans != '1' and ans != '2':
	print(f"'{ans}' is not a valid input")
elif ans == '1':
	log()
elif ans == '2':
	retrieve()

# ----------------------------DONE------------------------------------
