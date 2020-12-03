from time import sleep
from threading import Thread,Event

def statemachine(taster):
    status = "START"
    while True:
        if status == "START":
            status="GRÜN/ROT"
            ticks = 0

        elif status =="GRÜN/ROT":
            if taster.is_set():
                status="ORANGE/ROT"
                ticks=0


        elif status == "ORANGE/ROT":
            if ticks==3:
                status="ROT/GRÜN"
                ticks=0

        elif status == "ROT/GRÜN":
            if ticks==10:
                status= "ROT/ROT"
                ticks = 0

        elif status == "ROT/ROT":
            if ticks==5:
                status="GRÜN/ROT"
                ticks=0
                taster.clear() #wenn nochmal gedrückt das es nicht permanent wieder kommt

        else:
            print("unbekannter Status", status)
            status="Start"

        sleep(1)
        if ticks == 0:
            print("Status:", status)
        else:
            print("*", end="")


        ticks+=1

if __name__ == "__main__":
    taster = Event()
    thread = Thread(target = statemachine, args=(taster,))
    thread.daemon = True
    thread.start()

    while True:
        eingabe = input("Kommando:")
        if eingabe.upper()=="ENDE":
            break
        elif eingabe.upper()=="TASTER":
            print("Taster gedrückt")
            taster.set()
print("ENDE")