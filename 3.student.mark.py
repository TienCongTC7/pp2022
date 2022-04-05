import math
import numpy as np


class Student:
    def __init__(self, std_id, std_name, std_dob, std_mark=0):
        self.student_id = std_id
        self.student_name = std_name
        self.student_dob = std_dob
        self.student_mark = std_mark

    def input(self, std_id, std_name, std_dob, std_mark):
        student = Student(std_id, std_name, std_dob,std_mark)
        Students.append(student)

    def search(self, std_id):
        for i in range(Students.__len__()):
            if(Students[i].student_id == std_id):
                return i

    def update_mark(self,std_id, std_mark):
        i = std.search(std_id)
        Students[i].student_mark += std_mark 
    
    def GPA(self,std_mark, num_of_course):
        std_mark = std_mark / num_of_course
        return std_mark

    def __repr__(self):
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.student_name}\n"
            f"Dob: {self.student_dob}\n"
            f"GPA: {self.student_mark}\n"
        )

class Course:
    def __init__(self, c_id, c_name):
        self.course_id = c_id
        self.course_name = c_name

    def input(self, c_id, c_name):
        course = Course(c_id, c_name)
        Courses.append(course)

    def __repr__(self):
        return (
            f"ID: {self.course_id}\n"
            f"Name: {self.course_name}\n"
        )


class Mark:
    def __init__(self, std_id, c_id, std_mark):
        self.student_id = std_id
        self.course_id = c_id
        self.mark = std_mark

    def input(self, std_id, c_id, std_mark):
        m = Mark(std_id, c_id, std_mark)
        Marks.append(m)

    def __repr__(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Course ID: {self.course_id}\n"
            f"Mark: {self.mark}\n"
        )


def pause():
    input("Press Enter to continue!!....")


Students = []
Courses = []
Marks = []
std = Student(0, '', '',0)
c = Course(0, '')
m = Mark(0, 0, 0)


while True:
    print("***************************\n"
          "1. Input Student's Info \n"
          "2. Input a Course \n"
          "3. Input a Student's mark \n"
          "4. Display Student \n"
          "5. Display course \n"
          "6. Display marks \n"
          "7. Sort Student List by GPA descending"
          "8. Exit\n "
          "***************************\n")
    choose = int(input("Enter your choice: "))

    if choose == 1:
        num_of_std = int(input("Enter number of students in class: "))
        for k in range(0, num_of_std):
            std_id = str(input("Enter student's id: "))
            std_name = str(input("Enter student's name: "))
            std_dob = str(input("Enter student's dob: "))
            std_mark = 0
            std.input(std_id, std_name, std_dob, std_mark)

        print(Students)
        pause()
        continue

    if choose == 2:
        num_of_course = int(input("Enter number of course in school: "))
        for i in range(0, num_of_course):
            c_id = int(input("Enter a course's id: "))
            c_name = str(input("Enter course's name: "))
            c.input(c_id, c_name)
        print(Courses)
        pause()
        continue

    if choose == 3:
        print(Students)
        for i in range(0, num_of_std):
            choose_id = str(input("Please choose student ID: "))
            if (choose_id) != Students[i].student_id:
                print("Invalid ID!!!!!")
                break
            else:
                print(Courses)
                choose_course = int(input("Please choose course ID: "))
                std_mark = float(input("Please input student mark for this course: "))
                std_mark = math.floor(std_mark)
                std_mark1 = std.GPA(std_mark,num_of_course)
                std.update_mark(choose_id,std_mark1)
                m.input(choose_id, choose_course, std_mark)
                print(Marks)
        pause()
        continue

    if choose == 4:
        print(Students)
        pause()
        continue

    if choose == 5:
        print(Courses)
        pause()
        continue

    if choose == 6:
        print(Marks)
        pause()
        continue
    
    if choose == 7:
        print(sorted(Students, key= lambda x: x.student_mark, reverse= True))


    if choose == 8:
        print("Program Stopped!!!")
        break

    else:
        print("You select Wrong number")
        pause()
        continue