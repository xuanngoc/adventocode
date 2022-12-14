f = open('input.txt', 'r')

contents = f.readlines()

# A - X: Rock
# B - Y: Paper
# C - Z: Scissors

def which_win(a, b):
  match a:
    case 'A':
      match b:
        case 'X':
          return 'draw'
        case 'Y':
          return 'p2'
        case 'Z':
          return 'p1'
    case 'B':
      match b:
        case 'X':
          return 'p1';
        case 'Y':
          return 'draw';
        case 'Z':
          return 'p2';
    case 'C':
      match b:
        case 'X':
          return 'p2';
        case 'Y':
          return 'p1';
        case 'Z':
          return 'draw';

def shape_score(shape):
  return {'X': 1, 'Y': 2, 'Z': 3}[shape]

total_score = 0
for line in contents:
  score = 0
  a_selection = line[0]
  b_selection = line[2]

  winner = which_win(a_selection, b_selection)
  if winner == 'p2':
    score += 6
  elif winner == 'draw':
    score += 3
  
  score += shape_score(b_selection)

  print(a_selection, b_selection, score)
  total_score += score
  # break

print(total_score)
