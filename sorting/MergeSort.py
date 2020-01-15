class MergeSort:

    def __init__(self):
        pass

    def getSortedList(self, listToSort):
        if len(listToSort) <= 1:
            return listToSort
        mid = len(listToSort) // 2
        L = listToSort[:mid]
        R = listToSort[mid:]

        listToSort = self.mergeSortedList(self.getSortedList(L),
                                          self.getSortedList(R))
        return listToSort

    def mergeSortedList(self, L, R):
        resultList = []
        itrL = 0
        itrR = 0

        while itrL < len(L) and itrR < len(R):
            if L[itrL] <= R[itrR]:
                resultList.append(L[itrL])
                itrL += 1
            else:
                resultList.append(R[itrR])
                itrR += 1

        # Copy the remaining elements of L, if there are any
        while itrL < len(L):
            resultList.append(L[itrL])
            itrL += 1

        # Copy the remaining elements of R, if there are any
        while itrR < len(R):
            resultList.append(R[itrR])
            itrR += 1

        return resultList


myList = [56, 87, 23, 49, 102, 34, 1, 9, 72]
print("Actual list: " + str(myList))
sorting = MergeSort()
myList = sorting.getSortedList(myList)
print("Sorted list: " + str(myList))
