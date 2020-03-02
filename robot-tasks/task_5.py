#!/usr/bin/python3


import pyrob.api


@task
def task_5_2:
    while wall_is_beneath():
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()
