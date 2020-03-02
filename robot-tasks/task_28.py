#!/usr/bin/python3

from pyrob.api import *

8
@task
def task_7_6():
    c=0
    while c<5:
        move_right()
        if cell_is_filled():
            c=c+1


    pass


if __name__ == '__main__':
    run_tasks()
