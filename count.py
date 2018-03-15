def count(sequence, item):
  """Takes two arguments a list and an item to search for in the list respectively, it then searches the item in the list and returns a count of the searched item"""
  count = 0 
  for i in sequence:
    if item == i:
      count += 1 
  return count 

print count([1, 2, 1, 1], 1)
