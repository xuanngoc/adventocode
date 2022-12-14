f = open('input.txt', 'r')

contents = f.readlines()
chars = []

for i in range(0, len(contents) - 1, 3):
  line1 = list(set(contents[i][:-1]))
  line2 = list(set(contents[i+1][:-1]))
  line3 = list(set(contents[i+2][:-1]))
  
  # print(line1)
  # print(line2)
  # print(line3)


  h = {}
  for c in line1:
    h[c] = 1

  for c in line2:
    if h.get(c, 0) == 0:
      h[c] = 1
    elif h.get(c) == 1:
      h[c] = 2

  for c in line3:
    if h.get(c, 0) == 0:
      h[c] = 1
    elif h.get(c) == 2:
      print(3, h[c], c)
      chars.append(c)


""" 
  Lowercase item types a through z have priorities 1 through 26.
  Uppercase item types A through Z have priorities 27 through 52.
"""

priorities = 0
print(chars, len(chars))
for char in chars:
  # Ascii characters: 
  # A-Z: 65-90 -> priority: (27 through 52) => ord(char) - 65 + 27
  # a-z: 97-122 -> priority: (1 through 26) => ord(char) - 97 + 1
  char_in_ascii = ord(char)
  # print(char_in_ascii)
  if char_in_ascii >= 65 and char_in_ascii <= 90:
    # print(1, char, char_in_ascii - 65 + 27)
    priorities += (char_in_ascii - 65 + 27)
  elif char_in_ascii >= 97 and char_in_ascii <= 122:
    # print(2, char, char_in_ascii - 97 + 1)
    priorities += (char_in_ascii - 97 + 1)
  
  # print("=======")

print (priorities)
