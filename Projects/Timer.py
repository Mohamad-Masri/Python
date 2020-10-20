import threading

def myFun():
    print("BEEP")

timer = threading.Timer(5.0, myFun)

timer.start()
