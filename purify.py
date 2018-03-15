def purify(x):
"""takes a list and returns a list with the odd numbers removed from the list"""
  y = []
  for i in x:
    if not(i == 0):
      if i % 2 == 0:
        y.append(i)
  return y

print purify([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10])
  
