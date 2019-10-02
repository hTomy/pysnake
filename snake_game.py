import random
import curses
import sys
import time
uname = input('Choose a username: ')
if len(str(uname)) > 50:
    print('Username too long.')
    sys.exit(0)

s = curses.initscr()

curses.start_color()

curses.init_pair(1, 255, 255)
curses.init_pair(2, 4, 6)
curses.init_pair(3, 4, 4)

curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), 'c',curses.color_pair(3))

key = curses.KEY_RIGHT
for i in range(13,sw-2):
    w.addstr(2,i,'#',curses.color_pair(1))
    w.addstr(sh-2,i,'#',curses.color_pair(1))

for i in range(2,sh-1,1):
    w.addstr(i,12,'#',curses.color_pair(1))
    w.addstr(i,sw-2,'#',curses.color_pair(1))

w.addstr(1, 1, 'User: ' + str(uname))
start_time = time.time()
s = 0
t= 0
while True:
    w.addstr(3, 1, 'Score: ' + str(s))
    w.addstr(5, 1, 'Time: ' + str(t))
    # w.addstr(6, 7, str(t))
    t = int(time.time()-start_time)
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [2, sh-2] or snake[0][1]  in [12, sw-2] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        s +=1
        food = None
        while food is None:
            nf = [
                random.randint(3, sh-3),
                random.randint(14, sw-3)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI,curses.color_pair(3))
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD,curses.color_pair(2))