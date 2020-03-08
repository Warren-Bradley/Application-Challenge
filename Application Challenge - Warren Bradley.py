import sys

#Creating class student
class Student:
  def __init__(self, name, surname, score):
    self.name = name
    self.surname = surname
    self.score = score

#Defining relevant Lists
students = []
allscores = []
topstudents = []

#Requesting input and output file names

if len(sys.argv) == 3:
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
else:
#Safety check to allow different method of file location input
    inputfile = input('What is the name of the input file?: ')
    outputfile = input('What is the name of the output file?: ')


#Creating Functions

def creatingstudentlist(fileinput):
    
    with open(fileinput, 'r') as file:
        data = file.readlines()
        
        for line in data:
            lst = line.split(",")
            name = lst[0].strip()
            surname = lst[1].strip()
            score = int(lst[2].strip())

            person = Student(name,surname,score)
            students.append(person)  
    return students

def checkiftherearestudents(students,fileoutput):
    if len(students) == 0:
        file = open(fileoutput, "w")
        file.write("No Students in source file")
        file.close()
        print ("No Students in source file")
        exit()
    
def findtopscore(students):
    for student in students:
        number = student.score
        allscores.append(number)
    return allscores

def findbeststudent(students):
    for student in students:
        check = student.score
        if check==max(allscores):
            topstudents.append(student)
    return topstudents

def writinganswertofile(fileouput,best_students):
    file = open(fileouput, "w")

    for student in best_students:
        file.write(student.name + " " + student.surname + "\n")

    file.close()    

#Implementing Functions
creatingstudentlist(inputfile)
checkiftherearestudents(students,outputfile)        
findtopscore(students)
findbeststudent(students)
writinganswertofile(outputfile,topstudents)

for student in topstudents:
    print (student.name + " " + student.surname)    
        
    
