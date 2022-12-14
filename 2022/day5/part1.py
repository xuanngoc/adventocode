import numpy as np

lines = open("input.txt", "r").read().splitlines()

# print(f[0])
# print(f[1])


# print(len(f[0]))
# print(len(f[1]))
# print(len(f[2]))

# print(f[2][0:4])
# print(len(f[2][0:4]))

crates = []

for index, crate in enumerate(lines[:8]):
  crates.append([])
  for i in range(0, 36, 4):
    crates[index].append(crate[(i):(i+4-1)])

# print(crates)
for i in range(0, len(crates)):
  for m in range(0, len(crates[0])):
    print(crates[i][m], end=' ')
  print('')

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

m = np.array(crates)

crates = np.rot90(m, 3).tolist()

for i in range(0, len(crates)):
  print(i+1, end=' ')
  for m in range(0, len(crates[0])):
    print(crates[i][m], end=' ')
  print('')


def parse_rearrangement(rearrangement):
  rearrangement = rearrangement.replace('move ', '')
  rearrangement = rearrangement.replace('from', '')
  rearrangement = rearrangement.replace('to', '')
  # print(rearrangement)
  return list(map(int, rearrangement.split('  ')))


for i in range(0, len(crates)):
  crates[i] = [x for x in crates[i] if x != '   ']
  print(crates[i])


for rearrangement in lines[10:]:
  num_crates, src_stack, des_stack = parse_rearrangement(rearrangement)

  print(num_crates, src_stack, des_stack)

  l = crates[src_stack - 1][len(crates[src_stack - 1]) - num_crates:]
  l.reverse()
  for i in l:
    # print(i)
    crates[des_stack - 1].append(i)

  for i in range(0, num_crates):
    if len(crates[src_stack - 1]) != 0:
      crates[src_stack - 1].pop()
    # print(crates[src_stack])
  
  
  # break;
  for i in range(0, len(crates)):
    print(str(i+1) + ' ', end='')
    print(crates[i])

  print("\n>>>>>>>>>>>>>>>>>>>>>>\n")

for i in range(0, len(crates)):
  print(crates[i][len(crates[i]) - 1][1], end='')
print()