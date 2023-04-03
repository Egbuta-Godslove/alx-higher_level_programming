#!/usr/bin/python3
def add_integer(a, b=98):
  if type(a) not in [int, float] or type(b) not in [int, float]:
    raise TypeError
  else:
    a = int(a)
    b = int(b)
    return a + b
