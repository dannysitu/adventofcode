import intcode

intcodes = input("Input code(comma deliminated): ")

code = intcodes.split(",")

x = 0
noun = 0

while x <= 99:
  code[1] = noun
  verb = 0
  y = 0

  while y <= 99:
    code[2] = verb
    output = intcode.intcodeProgram(code)

    if output == 19690720:
      print(100 * noun + verb)
      break
    else:
      code = intcodes.split(",")
      code[1] = noun

    y = y + 1
    verb = y
  
  x = x + 1
  noun = x
