from classes.User import User

class Parent(User):

    # Attributes specific to Parent
    children: list  # List of Student IDs

    # Methods specific to Parent
    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str, role: str):
        super().__init__(id, full_name, email, password_hash, created_at, role)
        self.children = []

    def view_child_grades(self, child_id):
        child = self.get_child_by_id(child_id)
        if child:
            return child.grades
        else:
            raise ValueError("Child ID does not exist.")

    def view_child_assignments(self, child_id):
        child = self.get_child_by_id(child_id)
        if child:
            return child.assignments
        else:
            raise ValueError("Child ID does not exist.")


    def receive_child_notification(self, child_id):
        child = self.get_child_by_id(child_id)
        if child:
            return child.view_notifications()
        else:
            raise ValueError("Child ID does not exist.")








    def get_child_by_id(self, child_id):
        for child in self.children:
            if child.id == child_id:
                return child
        return None