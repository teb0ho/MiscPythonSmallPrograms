def factorial(x):
  """Calculates the factorial of a given numbera"""
  sum = 0
  for i in range(x, 0, -1): 
    if sum == 0: 
      sum += i
    else:
      sum *= i   
  return sum




  
 	
  	
