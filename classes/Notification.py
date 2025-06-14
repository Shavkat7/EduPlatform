


class Notification:

    # Attributes:
    id: int
    message: str
    recipient_id: int
    created_at: str # ISO format


    def __init__(self, id: int, message: str, recipient_id: int, created_at: str):
        self.id = id
        self.message = message
        self.recipient_id = recipient_id
        self.created_at = created_at


    def send(self, message, recipient_id):
        # Logic to send the notification
        print(f"Notification sent to {self.recipient_id}: {self.message} at {self.created_at}")
        return True
    
    def mark_as_read(self):
        # Logic to mark the notification as read
        print(f"Notification {self.id} marked as read.")
        return True
    