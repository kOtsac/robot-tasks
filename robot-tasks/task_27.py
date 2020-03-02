#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    c = 1
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        for i in range(c):
            if not wall_is_on_the_right():
                move_right()
        c=c+1








if __name__ == '__main__':
    run_tasks()
