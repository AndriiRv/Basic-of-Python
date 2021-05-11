# Author: Andrii Reva, sKS-18
# Date: 12.03.2020


def main():
    input_file = open("../resources/task8.txt", 'r', encoding="utf-8")
    fruits = dict()
    vitamines = list()
    for line in input_file:
        if line == "\n":
            continue
        if line.__contains__("Вид"):
            vit = line.split()
            for i in range(1, len(vit) - 1, 1):
                vitamines.append(vit[i])
            continue
        strs = line.split()
        key = strs[0]
        value = [float(i) for i in strs[1:len(strs)]]
        fruits[key] = value
    input_file.close()
    print("All fruits:")

    for key, value in fruits.items():
        print(key, "-", value)
    print("All vitamines: ", vitamines)
    search_vitamine = str(input("Enter the vitamine: "))
    index = vitamines.index(search_vitamine)

    max = 0
    fruit = ""
    for key, value in fruits.items():
        if value[index] > max:
            max = value[index]
            fruit = key
    print("Fruit: " + str(fruit) + "; max = " + str(max))
    needed_count = float(input("Enter the count of vitamine: "))
    for key, value in fruits.items():
        temp_count = value[index]
        temp_weight = value[len(value)-1]
        needed_weight = (needed_count * temp_weight) / temp_count
        print("Fruit: " + str(key) + "; needed weight = " + str(needed_weight))
    arr_fruits = []
    while True:
        str = str(input("Enter the fruit: "))
        if str == "END":
            break
        arr_fruits.append(str)
    count_vitamines = [0 for i in range(0, len(vitamines), 1)]
    for key, value in fruits.items():
        if arr_fruits.__contains__(key):
            for i in range(0, len(value) - 1, 1):
                count_vitamines[i] += value[i]
    print("Count of vitamines: " + str(count_vitamines))


main()
