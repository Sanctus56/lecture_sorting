import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r", newline="\n") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        iter = 0
        for row in reader:
            for key, value in row.items():
                if iter == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iter = iter + 1
        return data


def selection_sort(list, order = "ascending"):
    n = len(list)
    for i in range(n):
        min_idx = i
        for num_idx in range(i + 1, n):
            if "ascending" in order:
                if list[num_idx] < list[min_idx]:
                    min_idx = num_idx
            elif "descending" in order:
                if list[num_idx] > list[min_idx]:
                    min_idx = num_idx
        list[i], list[min_idx] =\
            list[min_idx], list[i]
    return list


def bubble_sort(list_numbers):
    for i in range(len(list_numbers)):
        for j in range(len(list_numbers) - i - 1):
            if list_numbers[j] > list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    return list_numbers


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key_number = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key_number:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key_number
    return numbers
def main():
    pass


if __name__ == '__main__':
    data = read_data("numbers.csv")
    print(data)
    sorted_list = selection_sort(data["series_1"], "descending")
    print(sorted_list)
    sorted_bubble_list = bubble_sort(data["series_2"])
    print(sorted_bubble_list)
    sorted_insertion_list = insertion_sort(data["series_3"])
    print(sorted_insertion_list)
    main()
