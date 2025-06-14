from classes.User import User, UserRole
import All_Users_Data
from classes.Teacher import Teacher
from classes.Student import Student
from classes.Parent import Parent


class Admin(User):

    # Attributes specific to Admin
    permissions: list  # List of permissions granted to the admin
    user_list: list  # List of users managed by the admin

    def __init__(self, full_name, email, password):
        super().__init__(full_name, email, password, UserRole.ADMIN)
        self.permissions = ["add_user", "remove_user", "generate_report"]

    def add_user(self, user):
        if isinstance(user, Student):
            All_Users_Data.students[user._id] = user
        elif isinstance(user, Teacher):
            All_Users_Data.teachers[user._id] = user
        elif isinstance(user, Parent):
            All_Users_Data.parents[user._id] = user
        elif isinstance(user, Admin):
            All_Users_Data.admins[user._id] = user
        All_Users_Data.users[user._id] = user
        print(f"User {user._full_name} added successfully.")

    def remove_user(self, user_id):
        user = All_Users_Data.users.get(user_id)
        if user:
            del All_Users_Data.users[user_id]
            if isinstance(user, Student):
                del All_Users_Data.students[user_id]
            elif isinstance(user, Teacher):
                del All_Users_Data.teachers[user_id]
            elif isinstance(user, Parent):
                del All_Users_Data.parents[user_id]
            elif isinstance(user, Admin):
                del All_Users_Data.admins[user_id]
            print(f"User {user_id} removed successfully.")
        else:
            print("User not found.")

    def generate_report(self):
        report = []
        for student_id, student in All_Users_Data.students.items():
            avg = student.calculate_average_grade()
            report.append(f"{student._full_name} (ID: {student_id}) - Average Grade: {avg}")
        return report
    