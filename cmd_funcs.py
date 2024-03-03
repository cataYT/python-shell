import os
import platform

current_platform = platform.system()

# ANSI escape codes for text colors
class colors:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'
	RESET = '\033[0m'
	
BOLD = '\033[1m'

def help():
	print("Commands:")
	print("help: Displays the list of commands")
	print("xor: Encrypts the string and decrypts it")
	print("touch: Creates a new file")
	print("mkdir: Creates a new directory")
	print("ls: Lists directory contents")
	print("cat: Displays file contents")
	print("clear: Clears the screen")
	print("pwd: Print current working directory")
	print("exit: Exits the program")

def xor(string, key):
	result = ""
	for char in string:
		result = result + chr(ord(char) ^ ord(key))
	return result

def touch(file_name):
	try:
		with open(file_name, "w"):
			pass
		return (1, file_name)
	except IOError as error:
		return (0, file_name, error)

def mkdir(directory_name):
	try:
		os.mkdir(directory_name)
		return (1, directory_name)
	except OSError as error:
		return (0, directory_name, error)

def ls():
    directory = "."
    file_and_dir_names = []
    try:
        for item in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, item)):
                file_and_dir_names.append(f"{colors.BLUE}{BOLD}{item}{colors.RESET}")
            elif os.path.isfile(os.path.join(directory, item)):
                file_and_dir_names.append(item)
        print(" ".join(file_and_dir_names))
        return [1]
    except OSError as error:
        return (0, error)

def cat():
	file_name = input("Enter the file name: ")
	try:
		with open(file_name, "r") as file:
			return (1, file.read())
	except IOError as error:
		return (0, error)

def clear():
	print('\033[2J')
	print('\033[H', end='')
 
def pwd():
    return os.getcwd()