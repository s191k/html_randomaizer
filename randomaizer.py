import io
import math
from random import random, randint
#
# with io.open("task.txt", encoding='utf-8') as file:
#     for line in file:
#         tasks = file.readlines()
#     tasks = list(map(lambda x: x[:-1] if x.endswith('\n') else x, tasks))
#
# with io.open("autor.txt", encoding='utf-8') as file:
#     for line in file:
#         autors = file.readlines()
#     autors = list(map(lambda x: x[:-1] if x.endswith('\n') else x, autors))


def randomaizer_def(tasks,autors):

    print(autors)
    print(type(autors))
    print(tasks)
    print(type(tasks))

    tasks = tasks.split('\n')
    autors = autors.split('\n')

    res_map = {}
    for autor in autors:
        res_map[autor] = []

    tests_per_person = math.floor(len(tasks) / len(autors))
    tests_left = len(tasks) - tests_per_person * len(autors)

    print("Количество тестов :: ",len(tasks))
    print("Количество участников :: ",len(autors))
    print("Количество тестов на человека :: ",tests_per_person)
    print("Количество нераспределенных тестов :: ",tests_left)
    print("---------------------")

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

    for key in res_map:
        print(key + " :: \n")
        for cur_task in res_map[key]:
            print(" -- " + cur_task)
        print("---------------------")

    if tests_left > 0:
        print("---Нераскиданные тесты---")
        print(unsigned_tests)

    return res_map,unsigned_tests
    # for key in res_map:
    #     print(key + " :: " + str(len(res_map[key])))