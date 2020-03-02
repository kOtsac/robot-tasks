#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    c=1
    for i in range(13):
        move_down()
        for i in range(c):
            move_right()
            fill_cell()
        move_left(c)
        c=c+1
    move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
