# Sorting
import time

class Sorting:
    def __init__(self, data):
        self.data = data

    def bubbleSort(self):
        print("==== before sorting ====")
        arr = self.data
        print(arr)
        total = len(arr)
        t1 = time.perf_counter()
        for i in range(total-1):
            for j in range(0, total-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] # swaping arr[0] with arr[1] dst.
        t2 = time.perf_counter()
        print("==== after sorting ====")
        print(arr)
        print(f"=== bubbleSort execution time : {t2 - t1:0.6f} seconds")

    def insertionSort(self):
        print("==== before sorting ====")
        arr = self.data
        print(arr)
        total = len(arr)
        t1 = time.perf_counter()
        for i in range(1, total):
            key = arr[i] # key > arr[1]
            j = i - 1 # j = 0
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        t2 = time.perf_counter()
        print("==== after sorting ====")
        print(arr)
        print(f"=== insertionSort execution time : {t2 - t1:0.6f} seconds")

    def mergeSort(self, arr):
        total = len(arr)
        if total > 1:
            mid = total // 2
            left = arr[:mid] # dari index 0 sampai mid
            right = arr[mid:] # dari mid sampai index terakhir
            
            # recursive untuk sorting arr left dan right
            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0
            # copas data ke temp array left[] dan right[]
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # checking jika ada element di left
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            # checkig jika ada element di kanan
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
    
    def callMergeSort(self):
        print("==== before sorting ====")
        arr = self.data
        print(arr)
        t1 = time.perf_counter()
        self.mergeSort(arr)
        t2 = time.perf_counter()
        print("==== after sorting ====")
        print(arr)
        print(f"=== mergeSort execution time : {t2 - t1:0.6f} seconds")

    def partition(self, arr, start, end):
        pivot = arr[start]
        low = start + 1
        high = end
        while True:
            while low <= high and arr[high] >= pivot:
                high -= 1
            
            while low <= high and arr[low] <= pivot:
                low += 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low] # swap
            else:
                break
        
        arr[start], arr[high] = arr[high], arr[start] # swaping
        return high
    
    def quickSort(self, start, end):
        if start >= end:
            return
        
        part = self.partition(self.data, start, end)
        self.quickSort(start, part-1)
        self.quickSort(part+1, end)

    def callQuickSort(self):
        print("==== before sorting ====")
        arr = self.data
        print(arr)
        t1 = time.perf_counter()
        self.quickSort(0, len(arr) - 1)
        t2 = time.perf_counter()
        print("==== after sorting ====")
        print(arr)
        print(f"=== quickSort execution time : {t2 - t1:0.6f} seconds")

    def selectionSort(self):
        print("==== before sorting ====")
        arr = self.data
        total = len(arr)
        print(arr)
        t1 = time.perf_counter()
        # logic here
        for i in range(total):
            # set minimun index
            min = i
            for j in range(i+1, total):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        t2 = time.perf_counter()
        print("==== after sorting ====")
        print(arr)
        print(f"=== selectionSort execution time : {t2 - t1:0.6f} seconds")


    

sorting = Sorting([10, 9, 7, 100, 22, 44, 13, 76, 34, 23])
# sorting.bubbleSort()
# sorting.insertionSort()
# sorting.callMergeSort()
# sorting.callQuickSort()
sorting.selectionSort()

