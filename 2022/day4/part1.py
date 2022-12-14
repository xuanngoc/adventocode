f = open('input.txt', 'r')

contents = f.readlines()

counter = 0
for line in contents:
  line = line[:-1].split(',')

  first_elf = line[0].split('-')
  second_elf = line[1].split('-')
  
  first_elf = [int(x) for x in first_elf]
  second_elf = [int(x) for x in second_elf]

  first_elf.sort()
  second_elf.sort()



  if int(first_elf[0]) in range(int(second_elf[0]), int(second_elf[1]) + 1):
    if int(first_elf[1]) in range(int(second_elf[0]), int(second_elf[1]) + 1):
      counter += 1
    elif second_elf[0] in range(int(first_elf[0]), int(first_elf[1]) + 1):
      # print(second_elf[0])
      if int(second_elf[1]) in range(int(first_elf[0]), int(first_elf[1]) + 1):
        # print(12)
        counter += 1
  elif second_elf[0] in range(int(first_elf[0]), int(first_elf[1]) + 1):
    if int(second_elf[1]) in range(int(first_elf[0]), int(first_elf[1]) + 1):
      # print(2)
      counter += 1
  else:
    print(counter, first_elf, second_elf)


print(counter)

