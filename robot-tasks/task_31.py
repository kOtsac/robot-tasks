#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    c=0
    while c<2:
        while not wall_is_on_the_right():
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                    c=0
            move_right()
            if wall_is_on_the_right():
                c=c+1
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                    c=0
            if wall_is_on_the_left():
                c=c+1
            move_left()
    pass


if __name__ == '__main__':
    run_tasks()
