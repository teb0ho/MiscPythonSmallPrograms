def reverse(text):
  "my own function to reverse any text provided"
  rev = ""
  for i in range(len(text) - 1, -1, -1):
    rev += text[i]
  return rev
