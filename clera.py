#!/usr/bin/env python3

from time import sleep
from sys import exit
from os import get_terminal_size, system

bomb = [
    [
        " * ",
        "**)",
        " **",
    ],
    [
        " * ",
        "***",
        " (*",
    ],
]

frames = [
    [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        r"         _____\\*//______         ",
    ],
    [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                       ,          ",
        "             `                    ",
        """         *  %  '  "    :          """,
        "         '   _____   ,            ",
        r"           '/_ - _\               ",
        r"    _______/_||||||\_________     ",
    ],
    [
        "          CcQ0;cCQOo0.Q           ",
        "       CcQ0;cCQOo0.0oCQe.e        ",
        "    CcQ0;cCQOo0.0oCQe.CcQ0;cCQ    ",
        "    CcQ0;cCQOo0.0oCQe.CcQ0;cCQ    ",
        "   CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0   ",
        "CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0.0oCQe",
        "   CcQ0;cCQOo0.0oCQe.CcQ0;cCQ     ",
        " ____________|_|_|_|____________  ",
        "(_______________________________) ",
        "             |||||||              ",
        "             |||||||              ",
        "           CcQ0;cCQOo0            ",
        "          CcQ0;cCQOo0.o           ",
        "________CcQ0;cCQOo0.0oCQe.________",
    ],
]

clear = "\033[H\033[J"  # ANSI escape code to clear the terminal

termW, termH = get_terminal_size()

halfW = int(termW / 2)

frame_off_set = int(len(frames[0][0]) / 2)

fall_speed = 0.16

tick_speed = 0.2


def bomb_fall():
    fall_start, fall_end = abs(termH - halfW - 3), halfW - 3

    for i in range(fall_start, fall_end):
        print("\n" * (termH - halfW + i), end="")
        bomb_stage = bomb[i % 2 == 0]

        for line in bomb_stage:
            print(" " * i, end="")
            print(line)

        sleep(fall_speed)
        print(clear, end="")


def explosion():
    for frame in frames:
        print("\n" * termH, end="")

        for line in frame:
            print(" " * (halfW - frame_off_set), end="")
            print(line)

        sleep(tick_speed)
        print(clear, end="")


def animate_clera():
    bomb_fall()
    explosion()


if __name__ == "__main__":
    try:
        animate_clera()
    except KeyboardInterrupt:
        exit(0)
    finally:
        sleep(0.4)
        system("clear")
