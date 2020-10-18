import math
from django.shortcuts import render

from randomaizer import randomaizer_def


def index(request):
    tasks = request.POST.get('exampleFormControlTextarea1')
    autors = request.POST.get('exampleFormControlTextarea2')


    if tasks is not None and autors is not None:
        if tasks.strip() != '' and autors.strip() != '':

            tasks = list(map(lambda x: x.replace('\n','').replace('\r',''), tasks.split('\n')))
            autors = list(map(lambda x: x.replace('\n','').replace('\r',''), autors.split('\n')))

            res_map, unsigned_tests = randomaizer_def(tasks, autors)
            res_text = ''


            tests_per_person = math.floor(len(tasks) / len(autors))
            tests_left = len(tasks) - tests_per_person * len(autors)

            res_text += "Количество тестов :: " + str(len(tasks)) + "\n"
            res_text += "Количество участников :: " + str(len(autors)) + "\n"
            res_text += "Количество тестов на человека :: " + str(tests_per_person) + "\n"
            res_text += "Количество нераспределенных тестов :: " + str(tests_left) + "\n"

            # print(tasks)
            # print(autors)


            for key in res_map:
                res_text += key + " :: \n"
                for cur_task in res_map[key]:
                    res_text += " -- " + cur_task + "\n"
                res_text += "---------------------\n"

            # for key in res_map:
            #     for cur_task in res_map[key]:
            #         # print(key)
            #         # print(cur_task)
            #         print(cur_task.replace("\n",'') + " " + key + "\n")
            #         res_text += cur_task.replace("\n",'') + " " + key + "\n"

            # print(res_text)

            if len(unsigned_tests) > 0:
                res_text += "---Нераскиданные тесты---\n"
                for cur_task in unsigned_tests:
                    res_text += cur_task

            return render(request, 'gitlab_test_site/htmlpage.html', {'result':res_text} )
        else:
            return render(request, 'gitlab_test_site/htmlpage.html', {'result': ''})
    else:
            return render(request, 'gitlab_test_site/htmlpage.html', {'result':''})
