import gates

class Memory:

  def __init__(self,a1,a2):
    allowed = [0,1]
    if a1 in allowed and a2 in allowed:
      self.a = a1
      self.b = a2
    self.gates = Gates(self.a,self.b)

  def SRLATCH(self):
    gates.INVERTER()