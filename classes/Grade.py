import datetime

class Grade:
    student_id: int
    subject: str
    value: int # from 1 to 5
    date: str # ISO format
    teacher_id: int

    def __init__(self, student_id, subject, value, teacher_id, comment=""):
        self.id = Grade._id_counter
        Grade._id_counter += 1

        self.student_id = student_id
        self.subject = subject
        self.value = value
        self.date = datetime.datetime.now().isoformat()
        self.teacher_id = teacher_id
        self.comment = comment

    def update_grade(self, value: int):
        if 1 <= value <= 5:
            self.value = value
            return True
        else:
            raise ValueError("Grade value must be between 1 and 5")

    def get_grade_info(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "value": self.value,
            "date": self.date,
            "teacher_id": self.teacher_id,
            "comment": self.comment
        }
