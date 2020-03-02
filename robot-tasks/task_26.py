#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    b=0
    for i in range(5):
        c = 0
        for i in range(10):
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
            if c<10:
                move_right(4)
            if c==10:
                move_left(36)
                b=b+1
                if b<5:
                    move_down(4)
    pass


if __name__ == '__main__':
    run_tasks()
