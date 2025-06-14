from classes.User import User



class Teacher(User):
    # Attributes specific to Teacher
    subjects: list
    classes: list
    assignments: dict  # Key: assignment ID, Value: Assignment

    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str, role: str):
        super().__init__(id, full_name, email, password_hash, created_at, role)
        self.subjects = {}
        self.assignments = {}

    def create_assignment(self, title, description, deadline, subject, class_id):
        assignment_id = len(self.assignments) + 1
        self.assignments[assignment_id] = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "subject": subject,
            "class_id": class_id,
            # "status": "created"
        }
        return assignment_id
    
    def grade_assignment(self, assignment_id, student_id, grade):
        if assignment_id not in self.assignments:
            raise ValueError("Assignment ID does not exist.")
        # Assuming there's a method to get the student by ID
        student = self.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student ID does not exist.")
        # Assuming there's a method to record the grade for the student
        student.record_grade(assignment_id, grade)
        return True
        
    def view_student_progress(self, student_id):
        return self.get_student_by_id(student_id).grades
    
    