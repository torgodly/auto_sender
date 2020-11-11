import time
import pynput

from pynput.keyboard import Controller,Key

key = Controller()
time.sleep(5)
a = 1
while True:
    key.type(str(a))
    time.sleep(0.5)
    key.press(Key.enter)
    a = a + 1
