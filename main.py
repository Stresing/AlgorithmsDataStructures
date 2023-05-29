import random

list = []
for i in range(20):
    list.append(random.randint(0, 10))
print(list, 'original list')



def heapSorting(dataList):
    for start in range((len(dataList) - 2) // 2, -1, -1):
        heapSift(dataList, start, len(dataList) - 1)

    for end in range(len(dataList) - 1, 0, -1):
        dataList[end], dataList[0] = dataList[0], dataList[end]

        heapSift(dataList, 0, end - 1)
    return dataList


def heapSift(data, start, end):
    root = start

    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


print(heapSorting(list), "-HeapSort")

# def sortBubble(list): # ниже находятся другие сортировки .
#     n = 1
#     while n < len(list):
#         for i in range(len(list) - n):
#             if list[i] > list[i + 1]:
#                 list[i], list[i + 1] = list[i + 1], list[i]
#         n += 1
#     # return list
#
#
# def sortSelection(list):
#     for i in range(len(list)):
#         lowValueInList = i
#
#         for j in range(i + 1, len(list)):
#             if list[j] < list[lowValueInList]:
#                 lowValueInList = j
#         list[i], list[lowValueInList] = list[lowValueInList], list[i]
#     # return list
#
#
# def sortInsertion(dataList):
#     for i in range(1, len(dataList)):
#         elementsForInsert = dataList[i]
#         j = i - 1
#         while j >= 0 and dataList[j] > elementsForInsert:
#             dataList[j + 1] = dataList[j]
#             j -= 1
#         dataList[j + 1] = elementsForInsert

# sortInsertion(list)
# print(list, 'insert')
# sortSelection(list)
# print(list, 'selection')
# sortBubble(list)
# print(list, 'bubble') //#
