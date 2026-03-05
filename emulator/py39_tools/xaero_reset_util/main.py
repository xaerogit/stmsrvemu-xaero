# =============================================================================
# STMSRVEMU Reset Util
# Resets the emulator to the respective default values as they were provided
# With the emulator.ini file
# =============================================================================

from time import sleep as wait
import os
import sys
import colors
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

def main():
    ini_path = os.path.join(os.path.dirname(__file__), "..", "..", "emulator.ini")

    print("INI Path: " + ini_path + "\n")
    print("How would you like to reset the emulator?" + "\n")
    print("1. Reset General settings" + "\n")
    print("2. Flush The Cache" + "\n")
    print(colors.RED + "3. Reset the emulator to default values" + "\n" + colors.RESET)
    choice = input("") 

    if choice == "1":
        print("Resetting General Settings...")
    elif choice == "2":
        print("Flushing cache..." + "\n")
        wait(2)
        print("Placeholder - pretend it is actually deleting the cache")
    elif choice == "3":
        print("Resetting the emulator to  default values..." + "\n")
        confirm = input(colors.RED + "Are you sure you want to reset the emulator to factory defaults? (Y/N): " + colors.RESET)
        if confirm.lower() == "Y" or confirm.lower() == "y":
            print("Resetting the emulator to default values...")
            print("Placeholder - pretend it is actually doing something" + "\n")
            wait(5)
        elif confirm.lower() == "N" or confirm.lower() == "n":
            print("this does nothing yet.")
    else:
        print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
