#!/bin/python3
import os
import sys
from datetime import date


"""Set the template, source, and output files here. Note that template and
source must be located in root/blogs/src/ and the output will be placed in 
root/blogs/."""
template = "template.html"
source = "medium.md"
output = "medium.html"

def main():
    """Generates an HTML blog file from a given source markdown file,
    template file, and output location. The input markdown file must
    follow the pandoc yaml format."""

    templatePath = "../blogs/src/" + template
    sourcePath = "../blogs/src/" + source
    print("source path: " + sourcePath)
    outputPath = "../blogs/" + output
    print("output path: " + outputPath)

    if check_variables(templatePath, sourcePath, outputPath):
        return 1

    command1 = f"touch \"{outputPath}\""
    if os.system(command1) != 0:
        print(f"Error: The output file could not be created. ({outputPath})")
        return 2

    command2 = f"pandoc --standalone --template \"{templatePath}\" \"{sourcePath}\" --toc > \"{outputPath}\""
    print(command2)
    return os.system(command2)


def get_current_date():
    return date.today().strftime("%m/%d/%Y")
    
    
def check_variables(templatePath, sourcePath, outputPath):
    """Checks whether the given file paths are valid, and does some basic error
    checking. Returns true if there were any issues."""
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-y":
            askForConfirmation = False
    else:
        askForConfirmation = True
    
    if not os.path.exists(templatePath):
        print(f"Error: The template file was not found ({templatePath}).")
        return True
    if not os.path.exists(sourcePath):
        print(f"Error: The source file was not found ({sourcePath}).")
        return True
    if os.path.exists(outputPath):
        print(f"Warning: There is already a blog post for the specified output. Are you sure you want to overwrite it? ({outputPath})")
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