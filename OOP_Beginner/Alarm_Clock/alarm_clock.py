class AlarmClock:
    def __init__(self):
        self.current_time = '00:00'
        self.alarm_enabled = False
        self.alarm_time = '00:00'
    def set_time(self):
        self.current_time = input("Enter time to set: ")
        print("Time set to ", self.current_time)
    def toggle_alarm(self):
        self.alarm_enabled = not self.alarm_enabled
    def set_alarm(self):
        self.alarm_time = input("Enter the alarm time to set: ")
        print("Alarm set to ", self.alarm_time)

