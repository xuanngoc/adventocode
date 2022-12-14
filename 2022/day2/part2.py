f = open('input.txt', 'r')

contents = f.readlines()

# A: Rock
# B: Paper
# C: Scissors

# X: lose
# Y: draw
# Z: win

def make_decision(a_selection, mandatory_result):
  match a_selection:
    case 'A':
      match mandatory_result:
        case 'X':
          return 'C'
        case 'Y':
          return 'A'
        case 'Z':
          return 'B'
    case 'B':
      match mandatory_result:
        case 'X':
          return 'A'
        case 'Y':
          return 'B'
        case 'Z':
          return 'C'
    case 'C':
      match mandatory_result:
        case 'X':
          return 'B'
        case 'Y':
          return 'C'
        case 'Z':
          return 'A'


def shape_score(shape):
  return {'A': 1, 'B': 2, 'C': 3}[shape]

def result_score(shape):
  return {'X': 0, 'Y': 3, 'Z': 6}[shape]


total_score = 0
for line in contents:
  score = 0
  a_selection = line[0]
  mandatory_result = line[2]

  b_selection = make_decision(a_selection, mandatory_result)

  score += result_score(mandatory_result)
  score += shape_score(b_selection)

  print(a_selection, mandatory_result, b_selection, score)
  total_score += score
  # break

print(total_score)
