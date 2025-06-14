import datetime
import All_Users_Data

class Notification:

    # Attributes:
    message: str
    recipient_id: int
    created_at: str # ISO format


    _id_counter = 1

    def __init__(self, message, recipient_id, priority="Normal"):
        self.id = Notification._id_counter
        Notification._id_counter += 1

        self.message = message
        self.recipient_id = recipient_id
        self.created_at = datetime.datetime.now().isoformat()
        self.is_read = False
        self.priority = priority

    def send(self):
        recipient = All_Users_Data.Platform.users.get(self.recipient_id)
        if recipient:
            recipient.add_notification(self.message)
            print(f"Notification sent to {recipient._full_name}.")
        else:
            print("Recipient not found.")

    
    def mark_as_read(self):
        self.is_read = True
    