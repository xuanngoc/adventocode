f = open('input.txt', 'r')

contents = f.readlines()

cl = []

sumCl = 0
for line in contents:
  if line != '\n':
    sumCl += int(line[0:(len(line) - 1)])
  else:
    cl.append(sumCl)
    sumCl = 0

print(cl[0], cl[1], cl[2])

cl.sort()
print(cl[-1], cl[-2], cl[-3])

print(cl[-3] + cl[-1] + cl[-2])
