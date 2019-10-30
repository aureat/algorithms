class Stack:

  def __construct(self):
    self.operands = ['+','-','*','/']
    self.stack = []
  
  def operation(x1,x2,op):
    return {
      '+': lambda x,y: x + y,
      '-': lambda x,y: x - y,
      '*': lambda x,y: x * y,
      '/': lambda x,y: x / y
    }.get(op,0)(x1,x2)

  def load(self, tokens):
    if len(tokens) > 1:
      for token in tokens:
        if str(token) in operands:
          x1 = stack.pop()
          x2 = stack.pop()
          r = stack_operation(x2,x1,token)
          stack.append(r)
        else:
          try:
            stack.append(int(token))
          except ValueError:
            return 0
      return stack
    else:
      if str(tokens[0]) in operands:
        return 0
      else:
        return int(tokens[0])