def intcodeProgram(code):
    x = 0
  
    length = len(code)

    while x < length:
      opcode = int(code[x])
      saveLocation = int(code[x+3])
      numberLocation1 = int(code[x+1])
      numberLocation2 = int(code[x+2])
      number1 = int(code[numberLocation1])
      number2 = int(code[numberLocation2])

      if opcode == 1:
        code[saveLocation] = number1 + number2
      elif opcode == 2:
        code[saveLocation] = number1 * number2
      elif opcode == 99:
        return code[0]
      else:
        print("ERROR: INVALID CODE " + str(opcode))
        break
      
      x+=4


code = input("Input code(comma deliminated): ");

code = code.split(",");

code[1] = 12
code[2] = 2

print(intcodeProgram(code));
