import random
tries = 0
name = input("Enter your name: ")
name.strip()

print(f"Hello {name}!")
print("Would you like to play a game with me?")
print("1)Yes")
print("2)No")
option = int(input("Select your option: "))
if option == 1:
	print("Car Game Starting!")
elif option == 2:
	print("Thank you!")
else:
	print("Invalid Option")