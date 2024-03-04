from cmd_funcs import *

def main():
	running = True
	name = input("Enter your name: ")
	if len(name) == 0:
		name = "cata"
	print("Assigning default name...")
	while running:
		path_elements = os.getcwd().split("/", 3)
		path_elements[1] = "~"
		path_elements.remove("cata")
		joined_path = os.path.join(*path_elements)
		commandInput = input(f"{colors.GREEN}{BOLD}{name}@{name}{colors.WHITE}:{colors.BLUE}{joined_path}{colors.RESET}$ ")
		lowercmdInput = commandInput.lower()
		
		match lowercmdInput:
			case "help":
				help()
			case "xor":
				string = input("Enter the string to encrypt: ")
				key = input("Enter the key for encryption: ")
				result = xor(string, key)
				print("Encrypted string: " + result)
			case "touch":
				result = touch(input("Enter the file name: "))
				if result[0] == 1:
					print(f"File '{result[1]}' created successfully.")
				else:
					print(f"Error: Unable to create file '{result[1]}': {result[2]}.")
			case "mkdir":
				result = mkdir(input("Enter directory name: "))
				if result[0] == 1:
					print(f"Directory '{result[1]}' created successfully.")
				else:
					print(f"Error: Unable to create directory '{result[1]}': {result[2]}.")
			case "ls":
				result = ls()
				if result[0] == 0:
					print("Error:", result[1])
			case "cat":
				result = cat()
				if result[0] == 1:
					print(result[1])
				else:
					print("Error:", result[1])
			case "curl":
				url = input("Enter the url for the request: ")
				typeReq = input("Enter the type of request (get/post): ")
				result = curl(typeReq=typeReq, url=url)
				print(result.text)
			case "exit":
				running = False
			case "clear":
				clear()
			case "pwd":
				print(pwd())
			case _:
				print("Command not found")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt as e:
		print("\nprocess terminated by keyboard interruption")
