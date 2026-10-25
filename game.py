import curses
from curses import wrapper
from assets import snake, food
import time

def valid_key(key):
    if key == "KEY_RIGHT" or key == "KEY_LEFT" or key == "KEY_UP" or key == "KEY_DOWN":
        return True


def main(stdscr):
    snk = snake(stdscr)
    fd = food(stdscr)
    stdscr.nodelay(True)
    curses.curs_set(False)   
    while True:
        stdscr.clear()
        if snk.bp[0].x == fd.x and snk.bp[0].y == fd.y:
            fd.update()
            snk.increase_length()
        fd.draw(stdscr)
        try:
            key = stdscr.getkey()
        except:
            key = None
        if key is not None: 
            if key == 'q':
                break
            elif valid_key(key):
                snk.update_head_direction(key)
        snk.update_loc(stdscr)
        snk.draw(stdscr)
        snk.update_body_parts_directions()
        stdscr.refresh()
        time.sleep(0.1)
        

wrapper(main)
