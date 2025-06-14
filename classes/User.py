from classes.AbstractRole import AbstractRole

from enum import Enum
class UserRole(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"

class User(AbstractRole):
    def __init__(self, full_name, email, password, role):
        super().__init__(full_name, email, password)
        self.role = role
        self._notifications = []

    def add_notification(self, notification):
        self._notifications.append(notification)

    def view_notifications(self):
        return [{"ID": n.id, "Message": n.message, "Priority": n.priority, "Is Read": n.is_read} for n in self._notifications]

    def delete_notification(self, notification_id):
        for notification in self._notifications:
            if notification.id == notification_id:
                self._notifications.remove(notification)
                print(f"Notification {notification_id} deleted.")
                return
        print("Notification ID is invalid!")


    def get_profile(self):
            return {
                "ID": self._id,
                "Name": self._full_name,
                "Email": self._email,
                "Role": self.role.value,
                "Created At": self._created_at
            }

    def update_profile(self, full_name=None, email=None, password=None):
        if full_name:
            self._full_name = full_name
        if email:
            self._email = email
        if password:
            self._password_hash = self._hash_password(password)