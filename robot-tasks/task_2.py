#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for i in range(1):
        move_right(2)
        move_down(2)
        fill_cell()
        move_right(2)
        move_down(1)
    pass


if __name__ == '__main__':
    run_tasks()