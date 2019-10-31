class Encrypt:

  def __init__(self, text = '', key = ''):
    self.raw_text = text
    self.alphabet_l = list('abcdefghijklmnopqrstuvwxyz')
    self.alphabet_u = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    self.alphalen = len(self.alphabet_u)
    if key == '':
      self.key = self.generateRandomKey()
    elif len(key) == self.alphalen:
      self.key = key

    # English Alphabet and Frequencies
    self.englishFrequency = {'A': 8.167,'B': 1.492,'C': 2.782,'D': 4.253,'E': 12.702,'F': 2.228,'G': 2.015,'H': 6.094,'I': 6.966,'J': 0.153,'K': 0.772,'L': 4.025,'M': 2.406,'N': 6.749,'O': 7.507,'P': 1.929,'Q': 0.095,'R': 5.987,'S': 6.327,'T': 9.056,'U': 2.758,'V': 0.978,'W': 2.360,'X': 0.150,'Y': 1.974,'Z': 0.074}
    self.englishFrequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    self.frequencies = [0.074, 0.095, 0.15, 0.153, 0.772, 0.978, 1.492, 1.929, 1.974, 2.015, 2.228, 2.36, 2.406, 2.758, 2.782, 4.025, 4.253, 5.987, 6.094, 6.327, 6.749, 6.966, 7.507, 8.167, 9.056, 12.702]
    self.englishLetters = [25, 16, 23, 9, 10, 21, 1, 15, 24, 6, 5, 22, 12, 20, 2, 11, 3, 17, 7, 18, 13, 8, 14, 0, 19, 4]

    # Punctuation &c.
    self.ps2 = []

  def generateRandomKey(self,cp = 0):
    import random
    al = self.alphabet_l
    au = self.alphabet_u
    stop = self.alphalen
    key = []
    keyed = []
    for i in range(stop):
      r1 = random.randrange(stop)
      while r1 in keyed:
        r1 = random.randrange(stop)
      key.append(au[r1])
      keyed.append(r1)
    if cp == 1:
      self.key = ''.join(key)
    return ''.join(key)
  
  def newKey(self):
    self.generateRandomKey(1)

  def process(self, raw):
    key = self.key
    al = self.alphabet_l
    au = self.alphabet_u
    ps1 = []
    for i in range(len(raw)):
      if raw[i] in au:
        ps1.append(raw[i])
      elif raw[i] in al:
        ps1.append(au[al.index(raw[i])])
      else:
        self.ps2.append((i,raw[i]))
    return ''.join(ps1)

  def cipher(self, raw):
    key = self.key
    au = self.alphabet_u
    ciphered = []
    for i in raw:
      ciphered.append(key[au.index(i)])
    return ''.join(ciphered)

  def repair(self, raw):
    raw = list(raw)
    ps2 = self.ps2
    ciphered2 = []
    j = 0
    for i in ps2:
      ciphered2 += raw[:i[0]-j] + [i[1]]
      del raw[:i[0]-j]
      j = i[0]+1
    return ''.join(ciphered2)

  def encrypt(self, text = '', formatted = 0):
    if self.raw_text != '':
      text = self.raw_text
    tr = self.cipher(self.process(text))
    if formatted == 0:
      return tr
    elif formatted == 1:
      return self.repair(tr)

  def frequencyDistribution(self, raw = ''):
    if self.raw_text != '':
      raw = self.encrypt(self.raw_text)
    frequency = {}
    for i in raw:
      if i not in frequency:
        frequency[i] = 1
      else:
        frequency[i] += 1
    self.textLetterFrequency = frequency
    for key in frequency:
      frequency[key] = frequency[key] / len(raw) * 100
    return frequency

  def directFrequencyMatching(self, raw = ''):
    if self.raw_text != '':
      raw = self.frequencyDistribution(self.raw_text)
    frequencies = sorted(raw.values())
    print(self.englishLetters)
    print(frequencies)
    matching = {}
    for i in range(len(frequencies)):
      if abs(frequencies[len(frequencies)-i-1] - frequencies) < 2:
