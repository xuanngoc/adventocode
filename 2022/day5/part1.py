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
  for m in range(0, len(crates[0])):
    print(crates[i][m], end=' ')
  print('')


def parse_rearrangement(rearrangement):
  rearrangement = rearrangement.replace('move ', '')
  rearrangement = rearrangement.replace('from', '')
  rearrangement = rearrangement.replace('to', '')
  # print(rearrangement)
  return rearrangement.split('  ')

for rearrangement in lines[10:]:
  num_crates, stack_src, stack_des = parse_rearrangement(rearrangement)

  print(num_crates, stack_src, stack_des)

  

  break;
