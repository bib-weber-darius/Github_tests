from threading import Thread, RLock, Event
from time import sleep

queue = []
lock = RLock()
event = Event()

def rechnen():
    global queue, lock

    while True:
        event.wait()# sonst läuft schleife weiter und es kommt zu einer Fehlermeldung
        if len(queue) == 1:
            event.clear()

        lock.acquire()
        try:
            rechnung = queue.pop(0)
        finally:
            lock.release()
        if(rechnung == "Ende"):
            break
        sleep(2)
        print(eval(rechnung))

thread = Thread(target=rechnen)
thread.start()#Thread startet

while True:
    x = input("Rechnung: ")
    lock.acquire()
    try:
        queue.append(x)
        event.set()
    finally:
        lock.release()
    if (x == "Ende"):
        break