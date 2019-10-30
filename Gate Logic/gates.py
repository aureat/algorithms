class Gates:

  def __init__(self, in1, in2):
    allowed = [0, 1]
    if in1 in allowed and in2 in allowed:
      self.a = in1
      self.b = in2

  def BUFFER(self):
    return self.a
  
  def INVERT(self, v):
    if v == 1:
      return 0
    else:
      return 1
  
  def INVERTER(self):
    return self.INVERT(self.a)

  def AND(self):
    if self.a == 1 and self.b == 1:
      return 1
    elif self.a == 0 or self.b == 0:
      return 0
  
  def NAND(self):
    return self.INVERT(self.AND())

  def OR(self):
    if self.a == 1 or self.b == 1:
      return 1
    else:
      return 0
  
  def NOR(self):
    return self.INVERT(self.OR())

  def XOR(self):
    if self.a == 0 or self.b == 0:
      if self.a == 0 and self.b == 0:
        return 0
      else:
        return 1
    else:
      return 0
  
  def XNOR(self):
    return self.INVERT(self.XOR())