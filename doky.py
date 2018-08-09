from sys import argv
from os import system

projects = ["robobsh","bobsh","bobhh"]

def help():
    print("usage:\n\tdoky.py <project>\nAvailable projects:\n")
    
    for project in projects:
        print('\t- ' + project)

def transform():
    #copy stuff between "tags"
    chosenOne = argv[1]
    print("Doing things with the chosenOne: " + chosenOne)

    with open('somefile1.md') as infile, open('newfile.md', 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip() ==   f"<{chosenOne}>":
                copy = True

            elif line.strip() == f"</{chosenOne}>":
                copy = False

            elif copy:
                outfile.write(line)

    #pandocing
    system(f"pandoc -o {chosenOne}.docx newfile.md")

if __name__ == "__main__":
    if len(argv) != 2:
        help()
        exit()
    else:
        transform()