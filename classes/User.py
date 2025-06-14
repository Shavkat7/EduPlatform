from classes.AbstractRole import AbstractRole

from enum import Enum
class UserRole(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"

class User(AbstractRole):

    # Attributes specific to User
    role: UserRole
    notifications: list

    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str, role: UserRole):
        super().__init__(id, full_name, email, password_hash, created_at)
        self.role = role
        self.notifications = []

    def add_notification(self, notification: str):
        self.notifications.append(notification)

    def view_notifications(self):
        return self.notifications
    
    def delete_notification(self, notification: str):
        if notification in self.notifications:
            self.notifications.remove(notification)
            return True
        return False
