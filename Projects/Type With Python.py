from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

texttowrite = "..............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."

#time.sleep()

for char in texttowrite:
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(300)
input()


while (0<1) :
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(200)
        keyboard.(Key.enter)
        keyboard.release(Key.enter)


keyboard.release(Key.enter)


Key.alt_l: Left ALT
Key.backspace: Backspace
Key.ctrl_l: Left Ctrl
Key.delete: Delete
Key.enter: Enter
Key.esc: Escape
Key.f1: F1
Key.f5: F5
Key.media_play_pause: Play/Pause
Key.page_down: Page Down
Key.up: Up Arrow Key
The rest can be found in the pynput docs for the Key class.
