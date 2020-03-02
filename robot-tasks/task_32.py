#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    painted = 0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    painted = painted + 1
                if not cell_is_filled():
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        move_right()
    mov('ax', painted)


    pass


if __name__ == '__main__':
    run_tasks()
