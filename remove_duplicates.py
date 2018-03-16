def remove_duplicates(x):
  """ takes a list as an argument and returns a list without duplicate items """
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y 

print sorted(remove_duplicates([1, 2, 3, 2, 6, 8, 10, 5, 4, 3, 2, 8, 10, 9, 9, 8, 2, 7, 1, 0]))
