#!/bin/python3
import os
import sys
from datetime import date


# Settings.
template = "../blogs/src/template.html"
source = "../blogs/src/test2.md"
output = "../blogs/test2.html"
metadata = "metadata.yaml"


#TODO: Set title and date variables from python code.

def main():
    title = "Markdown Syntax"

    if check_variables(template, source, output):
        return 1

    command1 = f"touch \"{output}\""
    if os.system(command1) != 0:
        print(f"Error: The output file could not be created. ({output})")
        return 2

    command2 = f"pandoc --standalone --template \"{template}\" \"{source}\" \"{metadata}\" --toc > \"{output}\""
    print(command2)
    return os.system(command2)


def get_current_date():
    return date.today().strftime("%m/%d/%Y")
    
    
def check_variables(template, source, output):
    """Checks whether the given file paths are valid, and does some basic error
    checking. Returns true if there were any issues."""
    if sys.argv[0] == "-y":
        askForConfirmation = False
    else:
        askForConfirmation = True
    
    if not os.path.exists(template):
        print(f"Error: The template file was not found ({template}).")
        return True
    if not os.path.exists(source):
        print(f"Error: The source file was not found ({source}).")
        return True
    if os.path.exists(output):
        print(f"Warning: There is already a blog post for the specified output. Are you sure you want to overwrite it? ({output})")
        if askForConfirmation:
            userResponse = input("Y/N: ").lower()
            if userResponse == "y" or userResponse == "ye" or userResponse == "yes":
                print("Overwriting existing output...")
            else:
                print(f"Overwrite cancelled. Please update the output variable to a file that doesn't exist.")
                return True
        else:
            print("Overwriting existing output...")
        # All checks have passed.
        return False;


if __name__ == "__main__":
    main()