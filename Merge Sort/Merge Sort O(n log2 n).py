def mergeSort(A):
  if len(A) > 1:
    q = len(A)//2
    L = A[:q]
    R = A[q:]
    mergeSort(L)
    mergeSort(R)
    n1 = len(L)
    n2 = len(R)
    i = j = k = 0
    while i<n1 and j<n2:
      if L[i] > R[j]:
        A[k] = R[j]
        j += 1
      else:
        A[k] = L[i]
        i += 1
      k += 1
    while i<n1:
      A[k] = L[i]
      i += 1
      k += 1
    while j<n2:
      A[k] = R[j]
      j += 1
      k += 1
  return A