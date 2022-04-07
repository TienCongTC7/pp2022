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
Marks = []