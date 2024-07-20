import random
def findIndex(sorted_num_list, number):
    first = 0
    last = len(sorted_num_list) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if sorted_num_list[middle] == number:
            return middle
        elif sorted_num_list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return -1
num_list = random.sample(range(1, 1500), 50)
sorted_num_list = sorted(num_list)
number = random.choice(sorted_num_list)
print(f"Список элементов:\n{sorted_num_list}\n")
index = findIndex(sorted_num_list, number)
print(f"Случайный элемент {number} находится по индексу {index}")
