import math

def term(n):
  x = (math.sqrt(8*n+1)-1) / 2
  y = math.ceil(x)
  return y

print(term(16))