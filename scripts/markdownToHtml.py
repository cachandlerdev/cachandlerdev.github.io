#!/bin/python3
import os
import sys
import ntpath


"""Set the template and source files here. Note that template and
source must be located in root/blogs/src/ and the output will be placed in 
root/blogs/ (unless otherwise specified)."""
template = "template.html"
source = "medium.md"

templateLocation = ""
sourceLocation   = ""
outputLocation   = ""

def main():
    """Generates an HTML blog file from a given source markdown file,
    template file, and output location. The input markdown file must
    follow the pandoc yaml format."""
    global templateLocation
    global sourceLocation
    global outputLocation

    if templateLocation == "":
        templateLocation = "../blogs/src/"
    if sourceLocation == "":
        sourceLocation = "../blogs/src/"
    if outputLocation == "":
        outputLocation = "../blogs/"

    templatePath = templateLocation + template
    sourcePath = sourceLocation + source
    outputPath = outputLocation + getOutputFileName(sourcePath)

    if (len(sys.argv) >= 2):
        if sys.argv[1] == "-u" or sys.argv[2] == "-u":
            return updateExistingFiles(templatePath)

    generateFile(templatePath, sourcePath, outputPath, True)
    
    
def getOutputFileName(sourcePath):
    """Gets the filename from the source path and replaces the .md with .html"""
    fullName = ntpath.basename(sourcePath)
    return fullName.replace(".md", ".html")
    
    
def updateExistingFiles(templatePath):
    """Updates all existing blog files to use the specified template file."""
    for file in os.listdir(outputLocation):
        if file.endswith(".html"):
            blogSourcePath = sourceLocation + ntpath.basename(file).replace(".html", ".md")
            outputPath = outputLocation + file
            generateFile(templatePath, blogSourcePath, outputPath, False)


def generateFile(templatePath, sourcePath, outputPath, askForConfirmation=True):
    """Generates an HTML blog file using the specified parameters."""
    if check_variables(templatePath, sourcePath, outputPath, askForConfirmation):
        return 1

    command1 = f"touch \"{outputPath}\""
    if os.system(command1) != 0:
        print(f"Error: The output file could not be created. ({outputPath})")
        return 2

    command2 = f"pandoc --standalone --template \"{templatePath}\" \"{sourcePath}\" --toc > \"{outputPath}\""
    print(command2)
    return os.system(command2)
    
    
def check_variables(templatePath, sourcePath, outputPath, askForConfirmation):
    """Checks whether the given file paths are valid, and does some basic error
    checking. Returns true if there were any issues."""
    if askForConfirmation == True:
        if len(sys.argv) >= 2:
            if sys.argv[1] == "-y":
                askForConfirmation = False
    
    if not os.path.exists(templatePath):
        print(f"Error: The template file was not found ({templatePath}).")
        return True
    if not os.path.exists(sourcePath):
        print(f"Error: The source file was not found ({sourcePath}).")
        return True
    if os.path.exists(outputPath):
        if askForConfirmation:
            print(f"Warning: There is already a blog post for the specified output. Are you sure you want to overwrite it? ({outputPath})")
            userResponse = input("Y/N: ").lower()
            if userResponse == "y" or userResponse == "ye" or userResponse == "yes":
                print("Overwriting existing output...")
            else:
                print(f"Overwrite cancelled. Please update the output variable to a file that doesn't exist.")
                return True
        else:
            print(f"Overwriting {outputPath}")
        # All checks have passed.
        return False;


if __name__ == "__main__":
    main()