import re

import math
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import configs
from django.shortcuts import render

from randomaizer import randomaizer_def


def index(request):
    tasks = request.POST.get('exampleFormControlTextarea1')
    autors = request.POST.get('exampleFormControlTextarea2')


    print(tasks)
    print(autors)

    if tasks is not None and autors is not None:
        if tasks.strip() != '' and autors.strip() != '':
            res_map, unsigned_tests = randomaizer_def(tasks, autors)
            res_text = ''
            #
            # if tasks.strip() != '' and autors.strip() != '':
            #     tests_per_person = math.floor(len(tasks) / len(autors))
            #     tests_left = len(tasks) - tests_per_person * len(autors)
            #


            tasks = tasks.split('\n')
            autors = autors.split('\n')

            tests_per_person = math.floor(len(tasks) / len(autors))
            tests_left = len(tasks) - tests_per_person * len(autors)

            res_text += "Количество тестов :: " + str(len(tasks)) + " \n "
            res_text += "Количество участников :: " + str(len(autors)) + " \n "
            res_text += "Количество тестов на человека :: " + str(tests_per_person) + " \n "
            res_text += "Количество нераспределенных тестов :: " + str(tests_left) + " \n "


            for key in res_map:
                res_text += key + " :: \n"
                for cur_task in res_map[key]:
                    res_text += " -- " + cur_task + "\n"
                res_text += "---------------------\n"

            if len(unsigned_tests) > 0:

                res_text += "---Нераскиданные тесты---\n"
                for cur_task in unsigned_tests:
                    res_text += cur_task

            return render(request, 'gitlab_test_site/htmlpage.html', {'result':res_text} )
    else:
        return render(request, 'gitlab_test_site/htmlpage.html', {'result':''})
