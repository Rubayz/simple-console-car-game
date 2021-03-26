commands = ""
is_started = False
name = input("Enter your name: ")
name.strip()

print(f"Hello {name}!")
print("Would you like to play a game with me?")
print("1)Yes")
print("2)No")
option = int(input("Select your option: "))
if option == 1:
	print("Car Game Starting!")
	print("There are some commands to start the car, to stop, to quit and the description of the commands is the help command!")
	while True:
		commands = input("> ")
		if commands == "start":
			if is_started:
				print("The car is already started")
			else:
				is_started = True
				print("Car is started.")			
		elif commands == "stop":
			if not is_started:
				print("The car is already stopped!")
			else:
				is_started = False
				print("Car is stopped.")
		elif commands == "help":
			print("""
start - To start the car.
stop - To stop the car.
quit - To quit.
			""")
		elif commands == "quit":
			break
		else:
			print("Sorry I dont understand that!")
elif option == 2:
	print("Thank you!")
else:
	print("Invalid Option")