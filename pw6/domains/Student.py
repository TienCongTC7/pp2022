
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


Students = []
std = Student(0, '', '',0)