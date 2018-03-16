def remove_duplicates(x):
  """ takes a list as an argument and returns a list without duplicate items """
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y 

print remove_duplicates([1, 2, 3])
