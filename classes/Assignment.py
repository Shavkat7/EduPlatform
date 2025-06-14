

class Assignment:

    # Assignment attributes
    title: str
    description: str
    deadline: str # ISO format
    subject: str
    teacher_id: int
    class_id: str
    submissions: dict # Key: student ID, Value: content
    grades: dict # Key: student ID, Value: grade
    difficulty: str


    _id_counter = 1

    def __init__(self, title, description, deadline, subject, teacher_id, class_id, difficulty="o'rtacha"):
        self.id = Assignment._id_counter
        Assignment._id_counter += 1

        self.title = title
        self.description = description
        self.deadline = deadline
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.difficulty = difficulty
        self.submissions = {}
        self.grades = {}

    def add_submission(self, student_id, content):
        self.submissions[student_id] = content


    def set_grade(self, student_id, grade):
        self.grades[student_id] = grade


    def get_status(self):
        return {"submissions": self.submissions, "grades": self.grades}
