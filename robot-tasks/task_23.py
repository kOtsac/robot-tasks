#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    c=0
    while not wall_is_on_the_right():
        move_right()
        c=c+1
        if not wall_is_above():
            n=0
            while not wall_is_above():
                move_up()
                fill_cell()
                n=n+1
            move_down(n)
    move_left(c)





    pass



if __name__ == '__main__':
    run_tasks()
