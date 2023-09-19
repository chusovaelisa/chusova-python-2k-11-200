import os

current_directory = os.getcwd()

while True:
    command = input(f"{current_directory} > ").split()

    if not command:
        continue

    action = command[0]

    if action == "pwd":
        print(current_directory)
    elif action == "cd":
        if len(command) < 2:
            print("Usage: cd <dirname>")
        else:
            new_dir = os.path.join(current_directory, command[1])
            if os.path.exists(new_dir) and os.path.isdir(new_dir):
                current_directory = new_dir
            else:
                print(f"Directory '{command[1]}' not found")
    elif action == "touch":
        if len(command) < 2:
            print("Usage: touch <filename>")
        else:
            file_path = os.path.join(current_directory, command[1])
            with open(file_path, "w"):
                pass
    elif action == "cat":
        if len(command) < 2:
            print("Usage: cat <filename>")
        else:
            file_path = os.path.join(current_directory, command[1])
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    print(file.read())
            else:
                print(f"File '{command[1]}' not found")
    elif action == "ls":
        files = os.listdir(current_directory)
        for file in files:
            print(file)
    elif action == "rm":
        if len(command) < 2:
            print("Usage: rm <filename>")
        else:
            file_path = os.path.join(current_directory, command[1])
            if os.path.exists(file_path) and os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"File '{command[1]}' not found")
    elif action == "exit":
        break
    else:
        print("Invalid command. Supported commands: pwd, cd, touch, cat, ls, rm, exit")