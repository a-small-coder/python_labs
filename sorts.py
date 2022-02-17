import random
import copy


def insert(matrix):
    for i in range(n):
        # m=i
        for j in range(i, 0, -1):
            if matrix[j]<matrix[j-1]:
                matrix[j], matrix[j - 1]= matrix[j-1], matrix[j]
    return matrix
def sort(matrix):
    for i in range(n):
        # m=i
        for j in range(n-1):
            if matrix[j]>matrix[j+1]:
                matrix[j], matrix[j + 1]= matrix[j+1], matrix[j]
    return matrix

def shell(matrix):
    step = get_hibbad_steps(len(matrix))
    while step>=1:
        i=0
        while i+step<len(matrix):
            # if matrix[i]>matrix[i+step]:
            #     matrix[i], matrix[i + step] = matrix[i+step], matrix[i]
            matrix[i], matrix[i + step] = min(matrix[i], matrix[i + step]), max(matrix[i], matrix[i + step])
            i+=1
        step//=2
    return sort(matrix)

def get_hibbad_steps(n):
    step = 1
    while step < n:
        step *= 2
    step -= 1
    return step


n=50
matrix=[random.randint(0, 10) for x in range(n)]
print(matrix)
print(insert(copy.deepcopy(matrix)))
# print(sort(copy.deepcopy(matrix)))
print(shell(copy.deepcopy(matrix)))


