class InsertionSort:

    def __init__(self):
        pass

    def getSortedList(self, listToSort):
        for i in range(len(listToSort)):
            for j in range(i, 0, -1):
                if listToSort[j] < listToSort[j - 1]:
                    self.swap(listToSort, j , j-1)

        return listToSort

    def swap(self, listToSort, posA, posB):
        temp = listToSort[posA]
        listToSort[posA] = listToSort[posB]
        listToSort[posB] = temp


myList = [56, 87, 23, 49, 102, 34, 1, 9, 72]
print("Actual list: " + str(myList))
sorting = InsertionSort()
myList = sorting.getSortedList(myList)
print("Sorted list: " + str(myList))
