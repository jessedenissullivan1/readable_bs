from codecs import encode
from os import urandom
from time import sleep
from random import randrange, choice
from pdb import set_trace


class readable_bs:
  def __init__(self, bs, ws = 3, rs = 9, codec = "hex_codec", offset = 0x40000000):
    self.bs = bs
    self.rs = rs
    self.ws = ws
    self.codec = codec
    self.offset = offset

  def print_row(self,s): 
    ret = []
    for x in range(0, len(s), self.ws):
      ret += [encode(s[x:x+self.ws], self.codec).__repr__()[2:-1]]
    return " ".join(ret)

  def __repr__(self):
    ret = ""
    addr = 0
    stride = (self.rs*self.ws)
    if stride == 0: return ""
    for i in range(0, len(self.bs), stride):
      ret += "0x{:08x} {}\n".format(self.offset + addr, self.print_row(self.bs[i:i+stride]))
      addr += stride
    return ret

  def __str__(self):
    return self.__repr__()

for i in range(20):
  a = readable_bs(bs = urandom(randrange(1000)), 
                  ws = randrange(10), 
                  rs = randrange(10),
                  codec = choice(["hex_codec", "base64_codec"]),
                  offset = randrange((2**36)-1))
  print(a)
  sleep(1)