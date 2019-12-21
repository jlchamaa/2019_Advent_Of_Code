def mult(a,b):
    return a * b

def add(a,b):
    return a + b


def try_a_code(code, noun, verb):
    code[1] = noun
    code[2] = verb
    num_of_ops = len(code) // 4 + 1
    for op_number in range(num_of_ops):
        op_index = 4 * op_number 
        op_number = code[op_index]
        if op_number == 2:
            fun = mult
        if op_number == 1:
            fun = add
        if op_number == 99:
            break
        code[code[op_index + 3]] = fun(code[code[op_index + 1]], code[code[op_index + 2]])
    return code[0]


with open("modules.txt", "r") as f:
    v = f.readline().strip().split(",")
    code = [int(op) for op in v]
    for noun in range(100):
        for verb in range(100):
            if try_a_code(code[:], noun, verb) == 19690720:
                print("Noun: {}, Verb: {}".format(noun, verb))
