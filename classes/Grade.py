

class Grade:
    id: int
    student_id: int
    subject: str
    value: int # from 1 to 5
    date: str # ISO format
    teacher_id: int

    def __init__(self, id: int, student_id: int, subject: str, value: int, date: str, teacher_id: int):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.value = value
        self.date = date
        self.teacher_id = teacher_id

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
            "teacher_id": self.teacher_id
        }
