import re

def arithmetic_arranger(problems, solve = False):
    # turn this
    # ["2 + 444", "1790 - 1", "34 + 32", "121 + 38"]

      # into this
    # "     2     1790      34      121\n+ 444    -    1    + 32    +   
    #49\n-----   ------    ----    -----"
    if (len(problems) > 5):
      return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for i in problems:
      if (re.search("[^\s0-9.+-]", i)):
        if (re.search("[/]", i) or re.search("[*]", i)) :
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      firstInteger = i.split(" ")[0]
      operator = i.split(" ")[1]
      secondInteger = i.split(" ")[2]

      if (len(firstInteger) >= 5 or len(secondInteger) >= 5) :
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if (operator == "+"):
        sum = str(int(firstInteger) + int(secondInteger))
      elif (operator == "-"):
        sum = str(int(firstInteger) - int(secondInteger))

      length = max(len(firstInteger), len(secondInteger)) + 2
      top = str(firstInteger).rjust(length)
      bottom = operator + str(secondInteger).rjust(length - 1)
      line = ""
      res = str(sum).rjust(length)
      for s in range (length):
        line += "-"

      if i != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res

    if solve:
      string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
      string = first + "\n" + second + "\n" + lines
    return string


print(arithmetic_arranger(["2 + 444", "1790 - 1", "34 + 32", "121 + 38"]))