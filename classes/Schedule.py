

class Schdedule:

    # Attributes:
    id: int
    class_id: str
    day: str # e.g., "Monday", "Tuesday"
    lessons: dict # Key: time, Value: subject, teacher_id



    def __init__(self, schedule_id: int, name: str, description: str, start_date: str, end_date: str):
        self.schedule_id = schedule_id
        self.name = name
        self.description = description
        self.start_date = start_date


    def add_lesson(self, time, subject, teacher_id):
        if time in self.lessons:
            raise ValueError(f"Conflict: Lesson already scheduled at {time}")
        self.lessons[time] = {
            "subject": subject,
            "teacher_id": teacher_id
        }
    
    def view_schedule(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "day": self.day,
            "lessons": self.lessons
        }
    
    def remove_lesson(self, time):
        if time in self.lessons:
            del self.lessons[time]
        else:
            raise KeyError(f"No lesson found at time {time}")
        
    
