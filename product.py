def product(x):
  """takes the numbers in a list and returns their product"""
  product = 1 
  
  for i in x:
    product *= i
  
  return product


print product([-4, 5, 5])
