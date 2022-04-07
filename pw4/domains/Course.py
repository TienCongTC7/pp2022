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


Courses = []