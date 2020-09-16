def arithmetic_arranger(problems, display=False):
  operators = ['+', '-']
  row_1 = ''
  row_2 = ''
  row_3 = ''
  row_4 = ''
  if len(problems) > 5:
      return "Error: Too many problems."
  
  for problem in range(len(problems)):
    problems[problem] = problems[problem].split(" ")
    if problems[problem][1] not in operators:
      return "Error: Operator must be '+' or '-'."

    if problems[problem][0].isdigit() == False or problems[problem][2].isdigit() == False:
        return "Error: Numbers must only contain digits."
    
    if len(problems[problem][0]) > 4 or len(problems[problem][2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    if problems[problem][1] == '+':
        result = int(problems[problem][0]) + int(problems[problem][2])
    else:
        result = int(problems[problem][0]) - int(problems[problem][2])

    size = max(len(problems[problem][0]),len(problems[problem][2])) + 2

    space = '    '

    row_1 += problems[problem][0].rjust(size)
    row_2 += problems[problem][1] + problems[problem][2].rjust(size-1)
    row_3 += '-' * size
    row_4 += str(result).rjust(size)

    if problem < len(problems) - 1:
        row_1 += space
        row_2 += space
        row_3 += space
        row_4 += space  

  if display:
      solution = row_1 + '\n' + row_2 + '\n' + row_3 + '\n' + row_4
  else:
      solution = row_1 + '\n' + row_2 + '\n' + row_3

  return solution
      