#!/usr/bin/env python3

from time import sleep
from os import get_terminal_size
from sys import stdout

write = stdout.write
flush = stdout.flush

move_cursor = "\033[%d;%dH"
move_cursor_home = move_cursor % (1, 1)
hide_cursor = "\033[?25l"
show_cursor = "\033[?25h"
clear_screen = move_cursor_home + "\033[2J"
clear_line = "\033[2K"

term_width, term_height = get_terminal_size()
horizontal_center = int(term_width / 2)

spf = 0.15

bomb = [
    lambda x, y:
           f"{move_cursor%(y,x)} *"
         f"{move_cursor%(y+1,x)}**"
        f"{move_cursor%(y+2,x)} *)",

    lambda x, y: 
           f"{move_cursor%(y,x)} *"
         f"{move_cursor%(y+1,x)}**"
        f"{move_cursor%(y+2,x)} (*",
]

frames = [
    f"{move_cursor%(term_height,horizontal_center-8)}" r"_____\\*//______",

    f"{move_cursor%(term_height-4,horizontal_center-12)}"   "            ,            "
    f"{move_cursor%(term_height-4,horizontal_center-12)}"   "         `               "
    f"{move_cursor%(term_height-3,horizontal_center-12)}" """     *  %  '  "    :     """
    f"{move_cursor%(term_height-2,horizontal_center-12)}"   "     '   _____   ,       "
    f"{move_cursor%(term_height-1,horizontal_center-12)}"  r"       '/_ - _\          "
    f"{move_cursor%(term_height,horizontal_center-12)}"    r"_______/_||||||\_________",

    f"{move_cursor%(term_height-13,horizontal_center-17)}" "          CcQ0;cCQOo0.Q            "
    f"{move_cursor%(term_height-12,horizontal_center-17)}" "       CcQ0;cCQOo0.0oCQe.e         "
    f"{move_cursor%(term_height-11,horizontal_center-17)}" "      CcQ0;cCQOo0.0oCQe.CcQ0;      "
    f"{move_cursor%(term_height-10,horizontal_center-17)}" "    CcQ0;cCQOo0.0oCQe.CcQ0;cCQ     "
    f"{move_cursor%(term_height-9,horizontal_center-17)}"  "   CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0    "
    f"{move_cursor%(term_height-8,horizontal_center-17)}"  "CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0.0oCQe "
    f"{move_cursor%(term_height-7,horizontal_center-17)}"  "   CcQ0;cCQOo0.0oCQe.CcQ0;cCQ      "
    f"{move_cursor%(term_height-6,horizontal_center-17)}"  " ____________|_|_|_|____________   "
    f"{move_cursor%(term_height-5,horizontal_center-17)}"  "(_______________________________)  "
    f"{move_cursor%(term_height-4,horizontal_center-17)}"  "             |||||||               "
    f"{move_cursor%(term_height-3,horizontal_center-17)}"  "             |||||||               "
    f"{move_cursor%(term_height-2,horizontal_center-17)}"  "           CcQ0;cCQOo0             "
    f"{move_cursor%(term_height-1,horizontal_center-17)}"  "          CcQ0;cCQOo0.o            "
    f"{move_cursor%(term_height,horizontal_center-17)}"    "________CcQ0;cCQOo0.0oCQe._________",
]


def bomb_fall():
    for i in range(1, term_height - 1):
        write(
            f"{move_cursor%(i-1,1)}{clear_line}"
            f"{move_cursor%(i,1)}{clear_line}"
            f"{bomb[i % 2](horizontal_center-term_height+i, i)}"
        )
        flush()
        sleep(spf)


def blow_up():
    for frame in frames:
        write(frame)
        flush()
        sleep(spf)


def animate_clera():
    try:
        write(clear_screen + hide_cursor)
        bomb_fall()
        blow_up()
    except KeyboardInterrupt:
        return
    finally:
        write(show_cursor + "\n")


if __name__ == "__main__":
    animate_clera()
