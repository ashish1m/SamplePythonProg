class SelectionSort:

    def __init__(self):
        pass

    def getSortedList(self, listToSort):
        for i in range(len(listToSort)):
            currentMinIndex = i
            for j in range(i + 1, len(listToSort)):
                if listToSort[currentMinIndex] > listToSort[j]:
                    currentMinIndex = j
            self.swap(listToSort, i, currentMinIndex)
        return listToSort

    def swap(self, listToSort, posA, posB):
        temp = listToSort[posA]
        listToSort[posA] = listToSort[posB]
        listToSort[posB] = temp


myList = [56, 87, 23, 49, 102, 34, 1, 9, 72]
print("Actual list: " + str(myList))
sorting = SelectionSort()
myList = sorting.getSortedList(myList)
print("Sorted list: " + str(myList))