def is_prime(x):
  """Function to test if any number provided is a prime number or not return true if the number is a prime number and false if not"""
  count = 0
  if x == 1:
  	return False 
  else:
    for i in range(x - 1, 1, -1):
      if x % i == 0:
        count += 1
    if count == 0:
      return True 
    else:
      return False
  
