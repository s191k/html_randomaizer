import math
from random import random

def randomaizer_def(tasks,autors):
    res_map = {}
    for autor in autors:
        res_map[autor] = []

    tests_per_person = math.floor(len(tasks) / len(autors))
    tests_left = len(tasks) - tests_per_person * len(autors)

    unsigned_tests = []

    if tests_left > 0:
        tasks = tasks[:-tests_left]
        unsigned_tests = tasks[-tests_left:]


    tasks = sorted(tasks, key=lambda A: random())

    for cur_tsk in tasks:
        cur_autor =min(res_map.items(), key=lambda x: len(x[1]))[0]
        res_map[cur_autor].append(cur_tsk)

    result_taks = []
    for key in res_map.keys():
        result_taks.extend(res_map[key])

    return res_map,unsigned_tests