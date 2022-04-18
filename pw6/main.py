from ast import comprehension
import os
import zipfile
from zipfile import ZipFile
from domains.Course import*
from domains.Student import*
from domains.Mark import*
import math
import pickle

def pause():
    input("Press Enter to continue!!....")




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
          "7. Sort Student List by GPA descending\n"
          "8. Compress to a Zip file\n"
          "9. Pickle\n"
          "10. Exit\n"
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
        with open('Student.txt', 'w') as std_f:
            for student in Students:
                std_f .write("%s\n" % student)
        print(Students)
        pause()
        continue

    if choose == 5:
        with open('Course.txt', 'w') as std_c:
            for course in Courses:
                std_c .write("%s\n" % course)
        print(Courses)
        pause()
        continue

    if choose == 6:
        
        with open('Mark.txt', 'w') as std_m:
            for mark in Marks:
                std_m .write("%s\n" % mark)
        print(Marks)
        pause()
        continue
    
    if choose == 7:
        print(sorted(Students, key= lambda x: x.student_mark, reverse= True))

    if choose == 8:
        handle = zipfile.ZipFile('Student.zip', 'w')
        for x in os.listdir():
            if x.endswith('.txt'):
                handle.write(x, compress_type = zipfile.ZIP_DEFLATED)
        handle.close()
        #os.remove("Course.txt")
        #os.remove("Mark.txt")
        #os.remove("Student.txt")
        #print("Program Stopped!!!")
        pause
        continue

    if choose == 9:
        db = {}
        db['Student'] = Student
        db['Course'] = Course
        db['Mark'] = Mark 
        dbfile = open('Examplepickle.txt', 'ab')
        pickle.dump(db,dbfile)
        dbfile.close()  

    if choose == 10:
        os.remove("Course.txt")
        os.remove("Mark.txt")
        os.remove("Student.txt")
        os.remove("Student.zip")
        os.remove("Examplepickle.txt")
        print("Program Stopped!!!") 
        break
    else:
        print("You select Wrong number")
        pause()
        continue