# Author: Andrii Reva, sKS-18
# Date: 12.03.2020


def main():
    global list
    input_file = open("../resources/task10.txt", "r", encoding="utf-8")
    cities = dict()
    information = list()
    for line in input_file:
        if line == "\n":
            continue
        if line.__contains__("Місто"):
            inf = line.split()
            for i in range(0, len(inf), 1):
                information.append(inf[i])
            continue
        strs = line.split()
        key = strs[0]
        value = [i for i in strs[1:len(strs)]]
        cities[key] = value
    input_file.close()
    print(str(cities))
    set_areas = set()
    for key, value in cities.items():
        set_areas.add(value[0])
    area_square = dict()
    area_density = dict()
    area_hospital = dict()
    area_university = dict()
    for area in set_areas:
        # print(str(area))
        area_square[area] = list()
        area_density[area] = list()
        area_hospital[area] = list()
        area_university[area] = list()
    for key, value in cities.items():
        # Area_square
        list = area_square[value[0]]
        list.append([key, float(value[2])])
        area_square[value[0]] = list
        # Area_density
        list = area_density[value[0]]
        list.append([key, float(value[1]) / float(value[2])])
        area_density[value[0]] = list
        # Area_hospital
        list = area_hospital[value[0]]
        list.append([key, (1000 * float(value[3])) / float(value[1])])
        area_hospital[value[0]] = list
        # Area_university
        list = area_university[value[0]]
        list.append([key, (1000 * float(value[4])) / float(value[1])])
        area_university[value[0]] = list
    output_file = open("text10_result.txt", 'w')
    print("Areas_square:")
    output_file.write("\nAreas_square:\n")
    print_areas(area_square, output_file)
    print("Areas_density:")
    output_file.write("\nAreas_density:\n")
    print_areas(area_density, output_file)
    print("Area_hospital:")
    output_file.write("\nArea_hospital:\n")
    print_areas(area_hospital, output_file)
    print("Area_university:")
    output_file.write("\nArea_university:\n")
    print_areas(area_university, output_file)
    output_file.close()


def print_areas(areas, output_file):
    for key, value in areas.items():
        print(str(key) + ":")
        output_file.write(str(key) + ":")
        for city in value:
            print(str(city))
            output_file.write(str(city))


main()
