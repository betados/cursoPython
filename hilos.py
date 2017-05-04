import _thread
import time
import sys

def printTime(idProceso, delay):

    for i in range(5):
        time.sleep(delay)
        print("%s: %s" %(idProceso, time.ctime(time.time())))

try:
    _thread.start_new_thread(printTime, ("proceso 1", 1))
    _thread.start_new_thread(printTime, ("proceso 2", 2))

except:
    print("fallo")

input("pulsa")
sys.exit()


