class Reminder:
    def __init__(self, message, time):
        self.message = message
        self.time = time

    def remind(self):
        print(f"Reminder: {self.message} at {self.time}")