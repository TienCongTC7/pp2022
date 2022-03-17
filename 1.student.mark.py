# Input student infom
def student_info(students):
    std_id = int(input("Enter student id: "))
    std_name = str(input("Enter student name: "))
    std_dob = str(input("Enter student dob: "))
    student = {
        'student id: ': std_id,
        'student name: ': std_name,
        'student dob: ': std_dob,
    }
    students.append(student)

# Input courses info
def course_info(courses):
    c_id = int(input("Enter course id: "))
    c_name = str(input("Enter course name: "))
    course = {
        'course id: ': c_id,
        'course name: ': c_name
    }
    courses.append(course)

# Input student mark
def student_mark(student,c_id):
    if "mark" not in student:
        student["mark"] = {}
    student["mark"][c_id]= input("Enter mark for student for this course: ")

# Display student list
def list_student(students):
    for student in students:
        print(f"{student['student id: ']}-{student['student name: ']}-{student['student dob: ']}")
    print()

# Display Courses
def list_course(courses):
    for course in courses:
        print(f"{course['course id: ']}-{course['course name: ']}")
    print()

# Display mark
def list_mark(students):
    for student in students:
        print(f"{student['student id: ']}-{student['student name: ']}-{student['student dob: ']}")
        if "mark" in student:
            print("Course id: Mark", end="\n")
            for c_id, mark in student["mark"].items():
                print(f"Course id-{c_id}: {mark}")
            print()





def pause():
    input("Press Enter to continue")

def main():
    students=[]
    courses=[]
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
            num_of_std = int(input("Enter number of student in class: "))
            for i in range(0,num_of_std):
                student_info(students)
            list_student(students)
            pause()
            continue

        if choose == 2:
            num_of_course = int(input("Enter number of course: "))
            for c in range(0, num_of_course):
                course_info(courses)
            list_course(courses)
            pause()
            continue

        if choose == 3:
            list_course(courses)
            select_course = int(input("Please select a course: "))
            if select_course < 0:
                print("Invalid Input!")
            else:
                for a in range(0, num_of_std):
                    print(f"Student {students[a]['student name: ']}", end="\n")
                    student_mark(students[a], courses[select_course-1]['course id: '])
            pause()
        if choose == 4:
            list_student(students)
            pause()
            continue
        if choose == 5:
            list_course(courses)
            pause()
            continue
        if choose == 6:
            list_mark(students)
            pause()
            continue
        if choose == 7:
            print("Program stopped!")
            break

if __name__ == "__main__":
    main()