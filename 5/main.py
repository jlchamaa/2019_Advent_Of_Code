#!/usr/bin/python3.6
def get_num_of_params(code, param_modes, opcode_index, number_to_get):
    real_params = []
    for num in range(number_to_get):
        param_mode = param_modes[num]
        initial_param = code[opcode_index + 1 + num]
        if param_mode == "0":
            real_params.append(code[initial_param])
        elif param_mode == "1":
            real_params.append(initial_param)
        else:
            raise ValueError("Unexpected mode")
    return real_params

def get_op_and_modes(given_opcode):
    full_length = ["0", "0", "0", "0"] + list(given_opcode)
    op_type = full_length[-1]
    param_modes = full_length[:-2]
    param_modes.reverse()
    return op_type, param_modes


def run_an_op(opcode_index, code):
    opcode, param_modes = get_op_and_modes(str(code[opcode_index]))
    if opcode == "1":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        code[code[opcode_index + 3]] = params[0] + params[1]
        return opcode_index + 4
    elif opcode == "2":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        code[code[opcode_index + 3]] = params[0] * params[1]
        return opcode_index + 4
    elif opcode == "3":
        code[code[opcode_index + 1]] = int(input("Input: "))
        return opcode_index + 2
    elif opcode == "4":
        params = get_num_of_params(code, param_modes, opcode_index, 1)
        print("Output: {}".format(params[0]))
        return opcode_index + 2
    elif opcode == "5":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        return params[1] if params[0] != 0 else opcode_index + 3
    elif opcode == "6":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        return params[1] if params[0] == 0 else opcode_index + 3
    elif opcode == "7":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        res = 1 if params[0] < params[1] else 0
        code[code[opcode_index + 3]] = res
        return opcode_index + 4
    elif opcode == "8":
        params = get_num_of_params(code, param_modes, opcode_index, 2)
        res = 1 if params[0] == params[1] else 0
        code[code[opcode_index + 3]] = res
        return opcode_index + 4
    elif opcode == "9":
        return None
    else:
        raise ValueError("no multi-digit digit opcode {}".format(opcode))


with open("modules.txt", "r") as f:
    v = f.readline().strip().split(",")
    code = [int(op) for op in v]
    index_of_next_op = 0
    while index_of_next_op is not None:
        index_of_next_op = run_an_op(index_of_next_op, code)
