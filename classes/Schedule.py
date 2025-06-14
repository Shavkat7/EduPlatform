

class Schedule:

    # Attributes:
    id: int
    class_id: str
    day: str # e.g., "Monday", "Tuesday"
    lessons: dict # Key: time, Value: subject, teacher_id



    _id_counter = 1

    def __init__(self, class_id, day):
        self.id = Schedule._id_counter
        Schedule._id_counter += 1

        self.class_id = class_id
        self.day = day
        self.lessons = {}

    def add_lesson(self, time, subject, teacher_id):
        if time in self.lessons:
            raise ValueError(f"Conflict: Lesson already scheduled at {time}")
        else:
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
        
    
