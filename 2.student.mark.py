class Student:
    def __init__(self, std_id, std_name, std_dob):
        self.student_id = std_id
        self.student_name = std_name
        self.student_dob = std_dob

    def input(self, std_id, std_name, std_dob):
        student = Student(std_id, std_name, std_dob)
        Students.append(student)

    def list_student(self, student):
        print("ID: ", student.student_id)
        print("Name: ", student.student_name)
        print("Dob: ", student.student_dob)
        print("\n")


class Course:
    def __init__(self, c_id, c_name):
        self.course_id = c_id
        self.course_name = c_name

    def input(self, c_id, c_name):
        course = Course(c_id, c_name)
        Courses.append(course)

    def list_course(self, course):
        print("ID: ", course.course_id)
        print("Name: ", course.course_name)
        print("\n")


class Mark:
    def __init__(self, std_id, c_id, std_mark):
        self.student_id = std_id
        self.course_id = c_id
        self.mark = std_mark

    def input(self, std_id, c_id, std_mark):
        m = Mark(std_id, c_id, std_mark)
        Marks.append(m)

    def list_mark(self, m):
        print("Student ID: ", m.student_id)
        print("Course_ID: ", m.course_id)
        print("Mark: ", m.mark)
        print("\n")


def pause():
    input("Press Enter to continue!!....")


Students = []
Courses = []
Marks = []
std = Student(0, '', '')
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
          "7. Exit\n "
          "***************************\n")
    choose = int(input("Enter your choice: "))

    if choose == 1:
        num_of_std = int(input("Enter number of students in class: "))
        for k in range(0, num_of_std):
            std_id = int(input("Enter student's id: "))
            std_name = str(input("Enter student's name: "))
            std_dob = str(input("Enter student's dob: "))
            std.input(std_id, std_name, std_dob)

        for i in range(Students.__len__()):
            std.list_student(Students[i])
        pause()
        continue

    if choose == 2:
        num_of_course = int(input("Enter number of course in school: "))
        for i in range(0, num_of_course):
            c_id = int(input("Enter a course's id: "))
            c_name = str(input("Enter course's name: "))
            c.input(c_id, c_name)
            for j in range(Courses.__len__()):
                c.list_course(Courses[j])

        pause()
        continue

    if choose == 3:
        for i in range(Students.__len__()):
            std.list_student(Students[i])
        for i in range(0, num_of_std):
            choose_id = int(input("Please choose student ID: "))
            choose_course = int(input("Please choose course ID: "))
            std_mark = int(input("Please input student mark for this course: "))
            m.input(choose_id, choose_course, std_mark)
            for k in range(Marks.__len__()):
                m.list_mark(Marks[k])
        pause()
        continue

    if choose == 4:
        for i in range(Students.__len__()):
            std.list_student(Students[i])
        pause()
        continue

    if choose == 5:
        for j in range(Courses.__len__()):
            c.list_course(Courses[j])
        pause()
        continue

    if choose == 6:
        for k in range(Marks.__len__()):
            m.list_mark(Marks[k])
        pause()
        continue

    if choose == 7:
        print("Program Stopped!!!")
        break



