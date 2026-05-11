'''
A threading.Timer is a way to schedule a function to be called after a certain amount of time has passed. 

Timer is a subclass of threading.Thread. So it has all the thread methods — start(), join(), is_alive(), etc. Under the hood, 
it just creates a thread that sleeps for N seconds and then calls function. 

usecases:
    1. Rate Limiting / Cooldown
    2. Auto-Save
    3. Timeout for Long Operations
    4. Delayed Notifications / Reminders
    5. Health Checks / Heartbeats

Don't use it for scheduled jobs across restarts (use cron, celery, or APScheduler instead — Timer lives in memory and dies with process)
'''

import threading

def greet():
    print("Hello! 3 seconds have passed.")

t = threading.Timer(3.0, greet)  # run greet() after 3 seconds
t.start()

print("This prints immediately.")

