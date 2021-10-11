from alarm_clock import AlarmClock

alarm_clock = AlarmClock()

print(f"The current set time is: {alarm_clock.current_time}")
alarm_clock.set_time()
alarm_clock.toggle_alarm()
if (alarm_clock.alarm_enabled == True):
    print(f"Alarm enabled and set for {alarm_clock.alarm_time}")
else:
    print(f"Alarm disabled")