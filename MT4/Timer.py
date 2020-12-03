from threading import Thread, Event
import threading
from time import sleep

event = Event()
alive = True


def setter():
    global alive
    alive = False
    event.set()
def Timer():
    global alive
    while True:
        event.wait()
        event.clear()
        print("ich lebe!")
        alive = True
periode = 5

thread = Thread(target=Timer)
thread.start()
while alive:
    t = threading.Timer(periode, setter)
    t.start()
    sleep(periode)





