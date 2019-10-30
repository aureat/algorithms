def insertion_sort(arr):
  for j in range(1,len(arr)):
    key = arr[j]
    i = j - 1
    while (i>=0) and (arr[i] > key):
      arr[i+1] = arr[i]
      i = i-1
    arr[i+1] = key
  return arr

insertion_sort([5,4,3,15,5,6,2,10])