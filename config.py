# GMOD BASE INSTALL DIR
GMOD_INSTALL = "D:\Steam\steamapps\common\GarrysMod"

# GMOD SERVER INSTALL DIR
GMOD_SERVER_INSTALL = "D:\Downloads\Games\GMod\GModServer"


def set_directory(dirChoice: [str]):
    """
    Sets initial directories to use the main program.
    """
    print("Since this is your first time running the program, you will need to setup your install directories.\n")
    dirs = []
    print(dirChoice)

    newDir = True
    while newDir:
        if "GMOD_INSTALL" in dirChoice:
            print("Please input your steam/GarrysMod directory:\n")
            dir = input("")

            print("You've inputted", dir, "as your GMod STEAM install.\n")
            print("Type 'Y' if this is correct or anything else if it is not.")
            confirm = input("")
            if confirm.lower() == "y":
                dirs.append((dir, 0))
                break
            else:
                continue

    if len(dirChoice) == 1:
        newDir = False

    newDir = True
    while newDir:
        if "GMOD_SERVER_INSTALL" in dirChoice:
            print("Please input your server directory:\n")
            dir = input("")

            print("You've inputted", dir, "as your SERVER install.\n")
            print("Type 'Y' if this is correct or anything else if it is not.")
            confirm = input("")
            if confirm.lower() == "y":
                dirs.append((dir, 1))
                break
            else:
                continue

        newDir = False

    if len(dirChoice) == 1:
        newDir = False

    return dirs

