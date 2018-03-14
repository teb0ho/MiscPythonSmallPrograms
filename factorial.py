def factorial(x):
  """Calculates the factorial of a given numbera"""
  ans = 0
  for i in range(x, 0, -1): 
    if ans == 0: 
      ans += i
    else:
      ans *= i   
  return ans




  
 	
  	
