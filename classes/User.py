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
