# Topics: Lists, Tuples, Sets, OOPS concept, Dictionaries, Files Handling
# Task: Create a simple Student Record System using Python. The system should allow
# users to perform various operations related to student information.
# Create a class named Student with the following attributes:
# Name, Age, Roll number, Marks (a dictionary where subjects are keys and marks are values),
# Implement the following functionalities:
# Add a new student's information.---
# Display the list of all students.
# Search for a student by roll number and display their information.
# Calculate the average marks of a student.
# Find the student with the highest average marks.
# Modify the marks of a specific subject for a student.---



class Student:
    def __init__(self,name, age , roll_no):
        
        self.name = name 
        self.age = age 
        self.roll_no = roll_no
        self.marks = {}
        self.avg=0


# TELL THE INFORMATION 
    def info(self):
        print(f"The name of student roll no.{self.roll_no} is {self.name}")
        


#DISPLAY THE LIST OF ALL STUDENTS 
    def to_list(self):  
        return [self.name, self.age , self.roll_no]
    

#DISPLAY THE LIST OF ALL STUDENTS 
    def to_list_with_marks(self):  
        return [self.name, self.age , self.roll_no, self.marks]
    
# Modify the marks of a specific subject for a student.---
    
    def upmarks(self):
                na=input(" Enter the subject of which you want to change the marks")
                if na in s.marks:
                    b=int(input("enter marks"))
                    s.marks[na]= b

                else:
                    print("subject not found")

                s.avg = (sum(s.marks.values()))/len(s.marks)
                return s.avg

                

            
        
    
 # to add marks in  form of dictonary   
    
    def subjects_marks(self):
         n = int(input ("Enter how many subjects?"))
         self.marks={}
         total = 0
         for i in range(n):
             sub = input("enter subject name ")
             mark = int(input("enter marks "))
             self.marks[sub] = mark
             total += mark
         self.avg = total/n
         return self.marks,self.avg



students =[]
n= int(input("How many students ?"))
for i in range (n):
    print(f"Student{i+1}")
    name = input("Enter Student name ")
    age = input (" Enter student age ")
    roll_no = input ("Enter roll no")

    s =Student(name,age,roll_no)
    s.subjects_marks
    students.append(s)
   
    

print ("""      Enter 1: To show the rollno.of the student.
        Enter 2: To show the list of the student. 
        Enter 3: To show the marks of the student.
        Enter 4: To search the roll number of the student.
        Enter 5: To find the average mark of student 
        Enter 6: To modify the marks of the student
        Enter 7: To find the highest average marks in a Class """)
while True:
    a = input()
    if int(a) ==1:
        for s in students:
            s.info()
        
    

    elif int(a)==2:
        for s in students:
            print(s.to_list())
        
    elif int(a)==3:
        for s in students:
            print(s.marks)

    elif int(a)==4:
        search = input("Enter rollno.")
        found  = False
        for s in students:
            if s.roll_no == search:
                print("Student found")
                print(s.to_list())
                found =True 
                break
        if not found:
            print("student not found ")

    elif int(a)==5:
        for s in students:
            print(f"{s.name} scored {s.avg}")
           
    elif int(a)==6:
        n= input("Enter the name of Student")
        for s in students:
             if s.name.lower() == n.lower():
                 s.upmarks
                 break
        else:
             print("student not found")
    

    elif int(a)==7:
        max  = 0
        for s in students:
            if s.avg> max:
                max= s.avg
                topper = s.name
        print(f" maxium no is of {topper} and got{max}")

    else:
        print("Program stops ")
        break

    



    



