import curses
import random


class body_part:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
class snake:
    def __init__(self, stdscr):      
        self.ubx, self.uby = stdscr.getmaxyx()
        self.ubx = self.ubx - 1
        self.uby = self.uby - 1
        self.bp = [body_part(0, 0, 2)] # body parts
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def increase_length(self):
        last_part = self.bp[-1]
        od = (last_part.d+2)%4
        nx = (last_part.x + self.directions[od][0])%self.ubx
        ny = (last_part.y + self.directions[od][1])%self.uby
        self.bp.append(body_part(nx, ny, last_part.d))

    def draw(self, stdscr):
        for i,p in enumerate(self.bp):
            stdscr.addstr(p.x, p.y, "⬤") 
    
    def update_loc(self, stdscr):
        for i, p in enumerate(self.bp):
            self.bp[i].x = (p.x + self.directions[p.d][0])%self.ubx
            self.bp[i].y = (p.y + self.directions[p.d][1])%self.uby
    
    def update_head_direction(self, key):
       # updating direction of head of the snake 
        if self.bp[0].d%2:
            # can only move left or right
            if key == "KEY_LEFT":
                self.bp[0].d = 0
            elif key == "KEY_RIGHT":
                self.bp[0].d = 2
        else:
            # can only move up or down
            if key == "KEY_UP":
                self.bp[0].d = 3
            elif key == "KEY_DOWN":
                self.bp[0].d = 1
        
    def update_body_parts_directions(self):
        for i in range(len(self.bp)-1, 0, -1):
           self.bp[i].d = self.bp[i-1].d

    def get_direction(self, stdscr, key):
        if self.d%2:
            # can only move left or right
            if key == "KEY_LEFT":
                self.d = 0
            elif key == "KEY_RIGHT":
                self.d = 2
        else:
            # can only move up or down
            if key == "KEY_UP":
                self.d = 3
            elif key == "KEY_DOWN":
                self.d = 1
        

class food:

    def __init__(self, stdscr):
        self.lbx, self.lby = 0, 0
        self.ubx, self.uby = stdscr.getmaxyx()
        self.uby = self.uby - 1
        self.ubx = self.ubx - 1
        self.x = 0
        self.y = 0
        self.update()
    def update(self):
        self.x = random.randint(self.lbx, self.ubx-1)
        self.y = random.randint(self.lby, self.uby-1)
    def draw(self, stdscr):
        stdscr.addstr(self.x, self.y, "■")

