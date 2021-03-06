import sys
import re

def main():
    # Checa se o comando para chamar o script foi executado corremente
    if(not check_command()):
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]        

    with open(input_file) as input, open(output_file, "w") as output:    
        pattern = re.compile(r"(   [\dabcdef]*:)|((ld|lw|lwu|lh|lhu|lb|lbu|fld|flw|sd|sw|sh|sb|fsd|fsw)[^#\n]*)")
        result = pattern.findall(input.read())

        test = result[-1]
        offset = int(result[0][0].strip(":   "), base=16)
        sp = int(result[-1][0].strip(":   "), base=16) - offset

        for line, inst, _ in result:
            if (line):
                output.write(to_trace(line, sp, offset) + "\n")
            if (inst):
                trace = to_trace(inst, sp, offset)
                if (trace != ""):
                    output.write(trace + "\n")

            

def check_command():
    if (len(sys.argv) < 3):
        print("There are not enough arguments.")
        print("Usage: python dump_to_trace.py <input_file> <output_file>")
        return False
    return True

def to_trace(instruction, sp, offset):
    # Instruction fetch:
    if (instruction.endswith(":") and instruction.startswith("   ")):
        return "2 {}".format(hex(int(instruction.strip(":   "), base=16) - offset).split("0x")[1])

    label = 0 if instruction[0] == "l" or instruction[0] == "f" or instruction[:1] == "fs" else 1

    # Extraindo endereco de uma instrucao
    if (re.search("(ld|lw|lwu|lh|lhu|lb|lbu|fld|flw|sd|sw|sh|sb|fsd|fsw)	.*", instruction)):
        addr = re.search(",-?\d*", instruction).group(0).strip(",")
        if addr == "":
            return ""
        return "{} {}".format(label, to_abs_hex(int(addr, base=16) + sp))

    return ""

def to_abs_hex(number):
    return hex(abs(int(number))).split("0x")[1]

main()