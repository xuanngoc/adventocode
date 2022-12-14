f = open('input.txt', 'r')

contents = f.readlines()
chars = []

for line in contents:
  line = line[:-1]
  first_compartment = line[:len(line) // 2]
  second_compartment = line[len(line) // 2:]

  first_dist = {char: True for char in first_compartment}

  # print("========")
  # print(line)
  # print(first_compartment)
  # print(second_compartment)
  
  # same = []
  for char in second_compartment:
    if char in first_compartment:
      same.append(char)
      # break
  # print(same)
  # print(">>>>>>>>>")
  chars.append(same[-1])

  # break


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
