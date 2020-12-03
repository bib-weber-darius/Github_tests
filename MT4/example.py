from threading import Event, Thread
import logging

logging.basicConfig(level=logging.DEBUG, format="%(threadName)-10s - %(message)s")

def worker():
    global running
    while running:
        logging.debug("Thread legt sich schlafen.")
        event.wait()
        event.clear()
        logging.debug("Thread ist aufgeweckt.")
    logging.debug("Thread wird beendet.")

thread = Thread(target=worker)
event = Event()
running = True

logging.debug("Starte Thread")
thread.start()
eingabe = ""
while eingabe.upper() != "ENDE":
    eingabe = input("<ENTER> zum Aufwecken des Threads ('Ende' zum Beenden) ")
    if eingabe.upper() == "ENDE":
        running = False
        logging.debug("Verlasse die Schleife.")
    event.set()

logging.debug("Warte auf Beendigung des Threads.")
thread.join()