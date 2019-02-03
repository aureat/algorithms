# def triangular_sequence(n):
#   sequence = ''
#   ssum = 0
#   for i in range(1,n+1):
#     if ssum + i < n:
#       ssum += i
#       sequence += i*str(i)
#     else:
#       sequence += (n-ssum)*str(i)
#       return sequence

def triangular_sequence(n): # O(√n)
  sequence = []
  ssum = 0
  for i in range(1,n+1):
    if ssum + i < n:
      ssum += i
      sequence += i*[i]
    else:
      sequence += (n-ssum)*[i]
      return sequence

print(' '.join([str(i) for i in triangular_sequence(300)]))