"""
GMOD Addon Adder
by Justin Berry
Python v3.9
"""

import os
import config as cfg


def add_lua_line():
    print("--------------------\n"
          "Adding addons to workshop.lua...\n"
          "--------------------\n")
    os.chdir(rf"{cfg.GMOD_SERVER_INSTALL}\garrysmod\lua\autorun\server")
    addon_list = []


    adding = True
    while adding:
        new = open("workshop.lua", "a")

        que = input("Input URL for addon> ")
        ID = ""

        if que == "":
            x = input("Confirm above addons by pressing enter. Type anything else to cancel.")
            if x == "":
                print("Addons added to workshop.lua.")
                break
            else:
                continue

        link_valid = False
        for letter in que:
            if letter.isdigit():
                ID += letter
                link_valid = True

        if len(ID) == 0 or len(ID) <= 6:
            print("Invalid link.")
            link_valid = False

        while link_valid:
            name = input("Name of addon> ")

            # If file is empty, add and notify user
            if os.stat('workshop.lua').st_size == 0:
                new.write(f'resource.AddWorkshop("{ID}") --{name}\n')
                addon_list.append((name, ID))
                print(f"workshop.lua was empty. Added '{name}' with ID {ID}")
                link_valid = False

            else:
                checking = True
                while checking:
                    old = open("workshop.lua", "r")
                    for line in old:
                        # If addon already exists, don't add and notify user
                        if ID in line:
                            print(f"{name} already exists under ID {ID} in workshop.lua.")
                            checking = False
                            link_valid = False
                            break
                        # If file is not empty, add and notify user
                        elif name not in addon_list:
                            new.write(f'resource.AddWorkshop("{ID}") -- {name}\n')
                            print(f"Addon ID '{ID}' added under name '{name}'")
                            addon_list.append((name, ID))
                            checking = False
                            link_valid = False
                            old.close()
                            break
                        else:
                            print(f"Addon '{name}' already exists or something went wrong.")

                    try:
                        old.close()
                        checking = False
                        link_valid = False
                        break
                    except IOError:
                        print("File is already closed.")

            new.close()

    print(addon_list)
    extract_and_mount(addon_list)


def extract_and_mount(addons: list[(str, str)]):
    print("--------------------\n"
          "Extracting addons...\n"
          "--------------------\n")
    cmd = None
    os.chdir("D:")

    if len(addons) == 0:
        print("No new addons detected. Exiting program.")

    for addon in addons:
        print("Going through addons...")
        for file in os.listdir(f'{cfg.GMOD_INSTALL}/garrysmod/addons'):

            if addon[1] in file:
                print(fr"GMA '{file}' found for addon '{addon[1]}'.")

                path = f'{cfg.GMOD_SERVER_INSTALL}/garrysmod/addons/{addon[0]}'

                isFile = os.path.isfile(path)
                if isFile:
                    print(f"{addon[0]} already exists in addons directory.\n"
                          f"The addon is either already extracted or copying the name of another.")

                else:
                    cmd = fr'gmad.exe' \
                          fr' extract -file "{cfg.GMOD_INSTALL}/garrysmod/addons/{file}"' \
                          fr' -out "{cfg.GMOD_SERVER_INSTALL}/garrysmod/addons/{addon[0]}"'

                    os.chdir(f"{cfg.GMOD_INSTALL}/bin")
                    os.system(cmd)
                    print(f"Addon '{addon[0]}' extracted to addons directory.")
                    break


def main():
    dirSet = []
    if cfg.GMOD_INSTALL == "" or cfg.GMOD_SERVER_INSTALL == "":
        if cfg.GMOD_INSTALL == "":
            dirSet.append("GMOD_INSTALL")
        if cfg.GMOD_SERVER_INSTALL == "":
            dirSet.append("GMOD_SERVER_INSTALL")

    if len(dirSet) > 0:
        dirs = cfg.set_directory(dirSet)

        for dir in dirs:
            if dir[1] == 0:
                cfg.GMOD_INSTALL = dir[0]
                print(cfg.GMOD_INSTALL)
            if dir[1] == 1:
                cfg.GMOD_SERVER_INSTALL = dir[0]
                print(cfg.GMOD_SERVER_INSTALL)
    add_lua_line()


if __name__ == "__main__":
    main()
