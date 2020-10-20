from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


while (0<1) :
        keyboard.press("s")
        keyboard.release("s")
        keyboard.press("p")
        keyboard.release("p")
        keyboard.press("a")
        keyboard.release("a")
        keyboard.press("m")
        keyboard.release("m")
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

input()

