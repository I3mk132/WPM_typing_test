import curses
from curses import wrapper


def second(stdscr):

    curses.init_pair(
        1,
        curses.COLOR_GREEN,
        curses.COLOR_MAGENTA
    )
    curses.init_pair(
        2,
        curses.COLOR_RED,
        curses.COLOR_BLACK
    )
    curses.init_pair(
        2,
        curses.COLOR_WHITE,
        curses.COLOR_BLACK
    )
    stdscr.clear()
    stdscr.addstr(1, 0, 'Hello world!')
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)


def main(stdscr):
    curses.init_pair(
        1,
        curses.COLOR_GREEN,
        curses.COLOR_BLACK
    )
    curses.init_pair(
        2,
        curses.COLOR_RED,
        curses.COLOR_BLACK
    )
    curses.init_pair(
        2,
        curses.COLOR_WHITE,
        curses.COLOR_BLACK
    )
    stdscr.clear()
    stdscr.addstr(1, 0, 'Hello world!')
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)


wrapper(main)
wrapper(second)