#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down()
    move_right()
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



    pass


if __name__ == '__main__':
    run_tasks()
