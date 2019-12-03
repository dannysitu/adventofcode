import intcode

code = input("Input code(comma deliminated): ")

code = code.split(",")

code[1] = 12
code[2] = 2

print(intcode.intcodeProgram(code))
