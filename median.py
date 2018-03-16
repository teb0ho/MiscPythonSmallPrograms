import math

def median(x):
  """Takes a list of elements and returns the middle element"""
  y = 0
  z = []
  a = []
  
  if len(x) % 2 == 0:
    y = len(x) / 2
    z = sorted(x)
    a.append((z[y - 1] + z[y]) / (2.0))
  else:
    y = len(x) / 2.0
    z = sorted(x)
    a.append(z[int(math.floor(y))])
	
  return a    
