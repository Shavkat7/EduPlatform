from classes.User import User

class Student(User):

    # Attributes specific to Student
    grade: str
    subjects: dict # Key: subject name, Value: Teacher ID
    assignments: dict # Key: assignment ID, Value: status
    grades: dict # Key: subject name, Value: list of grades

    # Methods specific to Student
    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str, role: str, grade: str):
        super().__init__(id, full_name, email, password_hash, created_at, role)
        self.grade = grade
        self.subjects = {}
        self.assignments = {}
        self.grades = {}

    def submit_assignment(self, assignment_id: int, content):
        if assignment_id not in self.assignments:
            raise ValueError("Assignment ID does not exist.")
        self.assignments[assignment_id] = 'submitted'

    def view_grades(self, subject: str = None):
        if subject:
            return self.grades.get(subject, [])
        return self.grades
    
    def calculate_average_grade(self):
        total_grades = 0
        count = 0
        for subject, grades in self.grades.items():
            if grades:
                average = sum(grades) / len(grades)
                # print(f"Average grade for {subject}: {average:.2f}")
                total_grades += average
                count += 1
            else:
                pass
                # print(f"No grades available for {subject}.")
        return (total_grades / count) if count > 0 else 0
    