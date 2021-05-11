# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import operator


def main():
    input_file = open("../resources/task9.txt", "r", encoding="utf-8")
    students = dict()
    subjects = dict()
    for line in input_file:
        if line == "\n":
            continue
        if line.__contains__("ПІБ"):
            subj = line.split()
            for i in range(1, len(subj), 1):
                subjects[subj[i]] = 0
            continue
        strs = line.split()
        key = strs[0]
        value = [int(i) for i in strs[1:len(strs)]]
        students[key] = value
    input_file.close()
    index_subj = 0
    for key1, value1 in subjects.items():
        sum_rates = 0
        count_stud = 0
        for key2, value2 in students.items():
            sum_rates += value2[index_subj]
            count_stud += 1
        index_subj += 1
        subjects[key1] = (sum_rates / count_stud)
    print("Average rating of subjects:")
    for key, value in subjects.items():
        print(str(key) + " - " + str(value))
    rating = dict()
    for key, value in students.items():
        # print(str(key) + " - " + str(value))
        sum = 0
        for r in value:
            sum += r
        rating[key] = (sum / len(value))
    print()
    print("Average rating of group:")
    for key, value in rating.items():
        print(str(key) + " - " + str(value))
    print()
    rating = sorted(rating.items(), key=operator.itemgetter(1))
    max_rating = rating[len(rating) - 1]
    print("Max rating:")
    for rating in rating:
        if rating[1] == max_rating[1]:
            print(str(rating))
    print()


main()
