#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    c=1
    while not wall_is_beneath():
        move_down()
        c=c+1
    while c>1:
        for i in range (c-2):
            move_right()
            fill_cell()
        move_right()
        for i in range(c - 2):
            move_up()
            fill_cell()
        move_up()
        for i in range(c - 2):
            move_left()
            fill_cell()
        move_left()
        for i in range(c - 2):
            move_down()
            fill_cell()
        move_right()
        c=c-2
    while not wall_is_beneath():
        move_down()
        move_left()







    """
   Такие дела  ¯\_(ツ)_/¯  
    c=0
    while not wall_is_beneath():
        c=c+1
        move_down()
    c=c+1
    if wall_is_beneath():
        for i in range(c-2):
            move_right()
            fill_cell()
        move_up()
        for i in range(c-4):
            move_left()
            fill_cell()
        if c>=5:
            move_up()
            for i in range(c - 6):
                move_right()
                fill_cell()
        if c>=7:
            move_up()
            for i in range(c - 8):
                move_left()
                fill_cell()
        if c>=9:
            move_up()
            for i in range(c - 10):
                move_right()
                fill_cell()
        if c>=11:
            move_up()
            for i in range(c - 12):
                move_left()
                fill_cell()
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        move_right()
    if wall_is_on_the_right():
        for i in range(c-2):
            move_up()
            fill_cell()
        move_left()
        for i in range(c-4):
            move_down()
            fill_cell()
        if c>=5:
            move_left()
            for i in range(c - 6):
                move_up()
                fill_cell()
        if c>=7:
            move_left()
            for i in range(c - 8):
                move_down()
                fill_cell()
        if c>=9:
            move_left()
            for i in range(c - 10):
                move_up()
                fill_cell()
        if c>=11:
            move_left()
            for i in range(c - 12):
                move_down()
                fill_cell()
    while not wall_is_on_the_right():
        move_right()
    while not wall_is_above():
        move_up()
    if wall_is_above():
        for i in range(c - 2):
            move_left()
            fill_cell()
        move_down()
        for i in range(c - 4):
            move_right()
            fill_cell()
        if c>=5:
            move_down()
            for i in range(c - 6):
                move_left()
                fill_cell()
        if c>=7:
            move_down()
            for i in range(c - 8):
                move_right()
                fill_cell()
        if c>=9:
            move_down()
            for i in range(c - 10):
                move_left()
                fill_cell()
        if c>=11:
            move_down()
            for i in range(c - 12):
                move_right()
                fill_cell()

    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    if wall_is_on_the_left():
        for i in range(c - 2):
            move_down()
            fill_cell()
        move_right()
        for i in range(c - 4):
            move_up()
            fill_cell()
        if c>=5:
            move_right()
            for i in range(c - 6):
                move_down()
                fill_cell()
        if c>=7:
            move_right()
            for i in range(c - 8):
                move_up()
                fill_cell()
        if c>=9:
            move_right()
            for i in range(c - 10):
                move_down()
                fill_cell()
        if c>=11:
            move_right()
            for i in range(c - 12):
                move_up()
                fill_cell()
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
    pass

"""
if __name__ == '__main__':
    run_tasks()
