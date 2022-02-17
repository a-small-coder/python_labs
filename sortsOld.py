import random
import copy
import time


print("Hello world!")

# константы
LIST_LENGTH = 100
MIN_NUMBER = -250
MAX_NUMBER = 1012
HEAP_SIZE = 20
TIME_LIST = []
SORTS_TYPES_LIST = []


# classes
class Heap:

    # list = []

    def __init__(self, arr):
        self.list = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(i)

    def add(self, val):
        self.list.append(val)
        i = len(self.list) - 1
        parent = int((i - 1) // 2)

        while i > 0 and self.list[parent] < self.list[i]:
            self.list[i], self.list[parent] = self.list[parent], self.list[i]
            i = parent
            parent = int((i - 1) // 2)

    def heapify(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        largest = i

        if left_child < len(self.list) and self.list[left_child] > self.list[largest]:
            largest = left_child

        if right_child < len(self.list) and self.list[right_child] > self.list[largest]:
            largest = right_child

        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]  # swap

            # Heapify the root.
            self.heapify(largest)

    def get_max(self):
        # print(self.list, " || heap list ")
        res = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop(-1)
        return res

    def sort(self):
        for i in range(len(self.list) - 1, 0, -1):
            self.list[i], self.list[0] = self.list[0], self.list[i]  # swap
            self.heapify(0)


# генерация матриц
def generate_random_list(length, min, max):
    return [random.randint(min, max) for x in range(length)]


# сортировка выбором
# В неотсортированном подмассиве ищется локальный максимум.
# Найденный максимум меняется местами с последним элементом в подмассиве.
# Если в массиве остались неотсортированные подмассивы — смотри пункт 1.
def select_sort(arr):
    sorted_list_start_index = len(arr) - 1
    while sorted_list_start_index > 0:
        max_num_index = 0
        # find a max number in unsorted list
        for i in range(sorted_list_start_index + 1):
            max_num_index = arr.index(max(arr[i], arr[max_num_index]))
        # swap elements
        arr[max_num_index], arr[sorted_list_start_index] = arr[sorted_list_start_index], arr[max_num_index]
        # reduce length of unsorted list
        sorted_list_start_index -= 1
    return arr


# сортировка вставкой
# Перебираются элементы в неотсортированной части массива.
# Каждый элемент вставляется в отсортированную часть массива на то место, где он должен находиться
def insertion_sort(arr):
    for i in range(len(arr)):
        # index_of_sorted_list
        j = i - 1
        inserting_num = arr[i]
        while arr[j] > inserting_num and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = inserting_num  #преветик дубиныааа <3
    return arr


# сортировка обменом
# Попарно сравниваются элементы массива
# Если элемент слева больше элемента справа, то элементы меняются местами
# Повторяем пункты 1-2 до тех пор, пока массив не отсортируется
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[j], arr[i] = min(arr[i], arr[j]), max(arr[i], arr[j])
    return arr


# сортировка расческой
# как пузырек, только сначала берётся достаточно большое расстояние
# между сравниваемыми значениями, а потом оно сужается вплоть до минимального.
def comb_sort(arr):
    factor = 1.247
    step = len(arr) - 1
    while step >= 1:
        i = 0
        while i + step < len(arr):
            arr[i], arr[i+step] = min(arr[i], arr[i+step]), max(arr[i], arr[i+step])
            i += 1
        step = int(step / factor)
    return bubble_sort(arr)


# сортировка Шелла
# как сортировка расческой, только выбирается более "правильное" расстояние
def shell_sort_hib(arr):
    step = get_hibbad_steps(len(arr))
    while step >= 1:
        i = 0
        while i + step < len(arr):
            arr[i], arr[i+step] = min(arr[i], arr[i+step]), max(arr[i], arr[i+step])
            i += 1
        step = int(step / 2)
    return bubble_sort(arr)


# получение стартового шага по последовательности Хиббада
def get_hibbad_steps(n):
    step = 1
    while step < n:
        step *= 2
    step -= 1
    return step


# быстрая сортировка
# Этот алгоритм состоит из трёх шагов.
# Сначала из массива нужно выбрать один элемент — его обычно называют опорным.
# Затем другие элементы в массиве перераспределяют так,
# чтобы элементы меньше опорного оказались до него, а большие или равные — после.
# А дальше рекурсивно применяют первые два шага к подмассивам справа и слева от опорного значения.
def quick_sort(arr):
    _quick_sort(arr, 0, len(arr)-1)
    return arr


def _quick_sort(arr, left, right):
    if left < right:
        median = simple_step(left, right, arr)
        _quick_sort(arr, left, median-1)
        _quick_sort(arr, median+1, right)


def simple_step(left, right, arr):
    main = arr[right]
    less = left
    for i in range(left, right+1):
        if arr[i] < main:
            arr[i], arr[less] = arr[less], arr[i]
            less += 1
    arr[less], arr[right] = arr[right], arr[less]
    return less


# пирамидальная сортировка
def heap_sort(arr):
    my_heap = Heap(copy.deepcopy(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = my_heap.get_max()
        my_heap.heapify(0)
    return arr


def tournament_sort(arr):
    arr = new_tour(arr)
    arr.reverse()   # because max-heap
    return arr


def new_tour(arr):
    array_slice = []
    for i in range(len(arr)):
        if i == HEAP_SIZE:
            break
        array_slice.append(arr[i])
    arr = arr[len(array_slice):]
    heap = Heap(array_slice)
    winners = []
    losers = []

    while len(arr) > 0:
        if len(winners) == 0:
            winners.append(heap.get_max())
            heap.heapify(0)

        if arr[0] < winners[-1]:
            heap.add(arr[0])
            arr.pop(0)
        else:
            losers.append(arr[0])
            arr.pop(0)

        if len(heap.list) > 0:
            winners.append(heap.get_max())
            heap.heapify(0)

    while len(heap.list) > 0:
        winners.append(heap.get_max())
        heap.heapify(0)

    if len(losers) == 0:
        return winners

    arr = losers + winners
    return new_tour(arr)


def main():
    matrix = matrix_generator()
    for line in matrix:
        print(line)

    print('\nselect_sort')
    SORTS_TYPES_LIST.append('select_sort')
    sort_matrix(copy.deepcopy(matrix), select_sort)

    print('\ninsertion_sort')
    SORTS_TYPES_LIST.append('insertion_sort')
    sort_matrix(copy.deepcopy(matrix), insertion_sort)

    # print('\nbubble_sort')
    # SORTS_TYPES_LIST.append('bubble_sort')
    # sort_matrix(copy.deepcopy(matrix), bubble_sort)
    #
    # print('\ncomb_sort')
    # SORTS_TYPES_LIST.append('comb_sort')
    # sort_matrix(copy.deepcopy(matrix), comb_sort)
    #
    # print('\nshell_sort_hib')
    # SORTS_TYPES_LIST.append('shell_sort_hib')
    # sort_matrix(copy.deepcopy(matrix), shell_sort_hib)
    #
    # print('\ncomb_sort')
    # SORTS_TYPES_LIST.append('comb_sort')
    # sort_matrix(copy.deepcopy(matrix), comb_sort)

    # print('\nquick_sort')
    # SORTS_TYPES_LIST.append('quick_sort')
    # sort_matrix(copy.deepcopy(matrix), quick_sort)
    #
    # print('\nheap_sort')
    # SORTS_TYPES_LIST.append('heap_sort')
    # sort_matrix(copy.deepcopy(matrix), heap_sort)
    #
    # print('\ntournament_sort')
    # SORTS_TYPES_LIST.append('tournament_sort')
    # sort_matrix(copy.deepcopy(matrix), tournament_sort)


# true_list = generate_random_list(LIST_LENGTH, MIN_NUMBER, MAX_NUMBER)
# print(true_list)
#
# print(select_sort(copy.deepcopy(true_list)), ' || select_sort')
#
# print(insertion_sort(copy.deepcopy(true_list)), ' || insertion_sort')
#
# print(bubble_sort(copy.deepcopy(true_list)), ' || bubble_sort')
#
# print(comb_sort(copy.deepcopy(true_list)), ' || comb_sort')
#
# print(shell_sort_hib(copy.deepcopy(true_list)), ' || shell_sort_hib')
#
# print(quick_sort(copy.deepcopy(true_list)), ' || quick_sort')
#
# print(heap_sort(copy.deepcopy(true_list)), ' || heap_sort')
#
# print(tournament_sort(copy.deepcopy(true_list)), ' || tournament_sort')


def matrix_generator():
    # user_m = input()
    # user_n = input()
    # user_min_limit = input()
    # user_max_limit = input()
    user_m = ''
    user_n = ''
    user_min_limit = ''
    user_max_limit = ''
    if user_m == '':
        m = LIST_LENGTH
    else:
        m = int(user_m)

    if user_n == '':
        n = 50
    else:
        n = int(user_n)

    if user_min_limit == '':
        min_limit = MIN_NUMBER
    else:
        min_limit = int(user_min_limit)

    if user_max_limit == '':
        max_limit = MAX_NUMBER
    else:
        max_limit = int(user_max_limit)

    arr = [[random.randint(min_limit, max_limit) for i in range(m)] for i in range(n)]

    for line in arr:
        print(line)
    return arr


def sort_matrix(matrix, sort_function):
    start_time = time.time()
    i = 0
    for line in matrix:
        matrix[i] = sort_function(line)
        print(matrix[i])
        i += 1
    print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
    TIME_LIST.append(round((time.time() - start_time) * 1000))


main()
print('размерность матрицы: ', LIST_LENGTH)
print('максимальный элемент матрицы: ', MAX_NUMBER)
print('минимальный элемент матрицы: ', MIN_NUMBER)
print(SORTS_TYPES_LIST)
print(TIME_LIST)
