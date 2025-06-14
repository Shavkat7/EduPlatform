from classes.User import User, UserRole
import All_Users_Data
class Parent(User):

    # Attributes specific to Parent
    children: list  # List of Student IDs

    # Methods specific to Parent
    def __init__(self, full_name, email, password):
        super().__init__(full_name, email, password, UserRole.PARENT)
        self.children = []

    def view_child_grades(self, child_id):
        child = All_Users_Data.Platform.students.get(child_id)
        if child:
            return child.view_grades()
        else:
            print("Child not found.")

    def view_child_assignments(self, child_id):
        child = All_Users_Data.Platform.students.get(child_id)
        if child:
            return child.assignments
        else:
            print("Child not found.")

    def receive_child_notification(self, child_id):
        child = All_Users_Data.Platform.students.get(child_id)
        if child:
            return child.view_notifications()
        else:
            print("Child not found.")