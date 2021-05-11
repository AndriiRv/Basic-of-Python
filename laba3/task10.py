# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def task10():
    ukrainian_deutsch_dictionary = dict()
    ukrainian_deutsch_dictionary["ручка"] = "griff"
    ukrainian_deutsch_dictionary["пенал"] = "federmäppchen"
    ukrainian_deutsch_dictionary["зошит"] = "notizbuch"
    ukrainian_deutsch_dictionary["крейда"] = "kreide"
    ukrainian_deutsch_dictionary["домашнє завдання"] = "hausaufgaben"
    ukrainian_deutsch_dictionary["оцінка"] = "bewertung"
    ukrainian_deutsch_dictionary["екзамен"] = "prüfung"
    ukrainian_deutsch_dictionary["викладач"] = "lehrer"
    ukrainian_deutsch_dictionary["студент"] = "student"
    ukrainian_deutsch_dictionary["школяр"] = "schüler"

    deutsch_ukrainian_dictionary = dict()
    for key, value in ukrainian_deutsch_dictionary.items():
        deutsch_ukrainian_dictionary[value] = key

    for key, value in deutsch_ukrainian_dictionary.items():
        print(key, '-', value)


task10()
