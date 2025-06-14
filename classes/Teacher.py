from classes.User import User, UserRole
from classes.Assignment import Assignment
import All_Users_Data

class Teacher(User):
    # Attributes specific to Teacher
    subjects: list
    classes: list
    assignments: dict  # Key: assignment ID, Value: Assignment

    def __init__(self, full_name, email, password):
        super().__init__(full_name, email, password, UserRole.TEACHER)
        self.subjects = []
        self.classes = []
        self.assignments = {}

    def create_assignment(self, title, description, deadline, subject, class_id, difficulty="o'rta"):
        assignment = Assignment(title, description, deadline, subject, self._id, class_id, difficulty)
        self.assignments[assignment.id] = assignment
        All_Users_Data.Platform.assignments[assignment.id] = assignment
        print(f"Assignment {assignment.id} created successfully.")

    
    def grade_assignment(self, assignment_id, student_id, grade):
        if assignment_id in self.assignments:
            assignment = self.assignments[assignment_id]
            assignment.set_grade(student_id, grade)

            student = All_Users_Data.Platform.students[student_id]
            if assignment.subject not in student.grades:
                student.grades[assignment.subject] = []
            student.grades[assignment.subject].append(grade)
            print(f"Grade {grade} set for student with {student_id} id, in assignment with {assignment_id} id.")
        else:
            print("Assignment not found.")
        
    def view_student_progress(self, student_id):
        student = All_Users_Data.Platform.students.get(student_id)
        if student:
            return student.view_grades()
        else:
            print("Student not found.")
    
    