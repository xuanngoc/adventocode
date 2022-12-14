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

max_cl = cl[0]

for c in cl:
  if c > max_cl:
    max_cl = c

print(max_cl)
