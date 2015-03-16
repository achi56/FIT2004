__author__ = 'Aaron'


def insertionSort(list):
    for index in range(1, len(list)):
        current = list[index]
        position = index

        while position > 0 and list[position-1] > current:
            list[position] = list[position-1]
            position -= 1

        list[position] = current

        print(list)


aList = [54,26,72,55,33,44,76,45]
print(aList)
print("")
insertionSort(aList)