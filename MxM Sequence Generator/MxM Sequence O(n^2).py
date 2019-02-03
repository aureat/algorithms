def triangular_sum(n):
  s = 0
  for i in range(1, n+1):
    s += i
  return s

def triangular_sequence(n): #O(n^2)
  sequence = [1]
  for i in range(1,n+1):
    isum = triangular_sum(sequence[i-1])
    if i>isum:
      sequence += [sequence[i-1]+1]
    elif i<=isum:
      sequence += [sequence[i-1]]
  return sequence[1:]

def triangular_full(n): #O(n)
  text = ''
  for i in range(1,n+1):
    text += i*str(i)
  return text

print(triangular_full(8))
print(''.join([str(i) for i in triangular_sequence(17)]))