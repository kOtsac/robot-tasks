#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    c=0
    while c<3 and not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            c=c+1
        if not cell_is_filled():
            c=0


    pass


if __name__ == '__main__':
    run_tasks()
