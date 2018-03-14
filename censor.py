def censor(text, word):
"""censors your text"""
  output = ""
  if word in text:
    output = text.replace(word, "*" * len(word))
    
  return output 

print censor("this hack is wack hack", "hack")
