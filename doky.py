import sys
import os

project = ["robob","bobsh","bobhh"]
projectNumber = 0

#display projects
while projectNumber < len(project):
    print (projectNumber, project[projectNumber])
    projectNumber = projectNumber+1


#project choice 
while projectNumber >= len(project) :
    projectNumber = int(input("choose your destiny (Enter a number): "))
    if  projectNumber <= len(project) :
        chosenOne = project[projectNumber]
        print (chosenOne)
    else :
        print  ("you....LOOSER!")

#copy stuff between "tags"
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
os.system(f"pandoc -o {chosenOne}.docx newfile.md")
