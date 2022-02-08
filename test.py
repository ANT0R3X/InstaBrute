from webbot import Browser
from pynput.keyboard import Key, Controller
import time
import random

#samscript

username = ''
print('Put the username... ' + username)
username = input()
web = Browser()
keyboard = Controller()
web.go_to('instagram.com')
time.sleep(5)
keyboard.press(Key.f6)
keyboard.release(Key.f6)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

word = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
        "Y", "Z"]
w=["","","","","","","",""]
word_list = list(word)

s = ''
while(True):
    s = random.choices(word_list, k=len(w))
    print(s)
    s = ''.join(s)
    print(s)
    web.type(s, into='Password')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
