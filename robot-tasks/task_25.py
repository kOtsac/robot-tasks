#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    c=0
    move_down()
    for i in range(5):
        for i in range(1):
            move_right()
            fill_cell()
            for i in range(2):
                move_down()
                fill_cell()
            move_right()
            move_up()
            fill_cell()
            for i in range(2):
                move_left()
                fill_cell()
            move_up()
            c=c+1
        if  c<5 :
            move_right(4)
    pass


if __name__ == '__main__':
    run_tasks()
