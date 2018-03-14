def anti_vowel(text):
"""This program takes a string of text and removes any vowels in the text if it finds any"""
  text1 = ""
  for i in range(0, len(text), 1):
    if not(text[i].lower() == 'a' or \
         	text[i].lower() == 'e' or \
          text[i].lower() == 'i' or \
          text[i].lower() == 'o' or \
          text[i].lower() == 'u'):
      
   	  text1 += text[i] 
      
  return text1

print anti_vowel("Hey You!")
