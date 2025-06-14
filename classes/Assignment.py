

class Assignment:

    # Assignment attributes
    id: int
    title: str
    description: str
    deadline: str # ISO format
    subject: str
    teacher_id: int
    class_id: str
    submissions: dict # Key: student ID, Value: content
    grades: dict # Key: student ID, Value: grade
    status: str




    def __init__(self, id: int, title: str, description: str, deadline: str, subject: str, teacher_id: int, class_id: str):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.submissions = {}
        self.grades = {}

    def add_submission(self, student_id, content):
        self.submissions[student_id] = content


    def set_grade(self, student_id, grade):
        self.grades[student_id] = grade


    def get_status(self):
        return self.status

