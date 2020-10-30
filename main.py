from time import sleep

from pyautogui import write, press
from prompt_toolkit.shortcuts import ProgressBar

from sys import argv

for i in range(3):
    print(i)
    sleep(1)


def enter():
    press('enter')


def file_len(self):
    return sum(1 for line in open(self, 'r'))


file_name = argv[1]

lines = file_len(file_name)

with open(file_name, 'r') as f:
    words = []
    for word in f:
        print(word)
        words.append(word)

    with ProgressBar() as pb:
        for i in pb(words):
            write(i)
            if not ("\n" in i or "\r" in i):
                press('enter')
