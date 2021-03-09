# -*- coding: utf-8 -*-
'''
This class has some functions to measure the action time.
'''
import time


class TimeWatch:
    # constructor.
    def __init__(self):
        self.__actions = dict()

    # destructor.

    def __del__(self):
        del self.__actions

    ''' start measuring time.
    Args:
        action_name (str): an action name.
    '''

    def start(self, action_name: str) -> None:
        start_time = time.time()
        self.__actions[action_name] = {
            'start': start_time
        }

    ''' stop measuring time.
    Args:
        action_name (str): an action name.
    '''

    def stop(self, action_name: str) -> None:
        start_time = self.__actions[action_name]["start"]
        end_time = time.time()
        elapsed_time = end_time - start_time
        item = {
            'end': end_time,
            'elapsed_time': elapsed_time
        }
        self.__actions[action_name].update(item)

    ''' print the elapsed time of action.
    Args:
        action_name (str): an action name.
    '''

    def print(self, action_name: str) -> None:
        elapsed_time = self.__actions[action_name]["elapsed_time"]
        print(
            f"[action name : {action_name} ] elapsed time : {elapsed_time * 1000}[ms]")

    ''' clear instance variable.
    '''

    def clear(self) -> None:
        self.__actions.clear()
