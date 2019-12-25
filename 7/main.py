#!/usr/bin/env python3.7
from pudb.remote import set_trace
from itertools import permutations
from collections import deque


class IntCodeMachine:

    def __init__(self, phase, code):
        self.code = code
        self.phase = phase
        self.phase_consumed = False
        self.input_signal = deque()
        self.output = None
        self.generator = self.run_computer()

    def __repr__(self):
        return "Phase {} Machine".format(self.phase)

    def add_input(self, new_input):
        self.input_signal.append(new_input)

    def run_computer(self):
        index_of_next_op = 0
        while index_of_next_op is not None:
            index_of_next_op = self.run_an_op(index_of_next_op)
            if self.output is not None:
                yield self.output
                self.output = None
        yield None

    def get_num_of_params(self, param_modes, opcode_index, number_to_get):
        real_params = []
        for num in range(number_to_get):
            param_mode = param_modes[num]
            initial_param = self.code[opcode_index + 1 + num]
            if param_mode == "0":
                real_params.append(self.code[initial_param])
            elif param_mode == "1":
                real_params.append(initial_param)
            else:
                raise ValueError("Unexpected mode")
        return real_params

    def get_op_and_modes(self, given_opcode):
        full_length = ["0", "0", "0", "0"] + list(given_opcode)
        op_type = full_length[-1]
        param_modes = full_length[:-2]
        param_modes.reverse()
        return op_type, param_modes


    def op_1(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        self.code[self.code[opcode_index + 3]] = params[0] + params[1]
        return opcode_index + 4

    def op_2(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        self.code[self.code[opcode_index + 3]] = params[0] * params[1]
        return opcode_index + 4

    def op_3(self, param_modes, opcode_index):
        if not self.phase_consumed:
            into = self.phase
            self.phase_consumed = True
        else:
            into = self.input_signal.popleft()
        self.code[self.code[opcode_index + 1]] = into
        return opcode_index + 2

    def op_4(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 1)
        self.output = params[0]
        return opcode_index + 2

    def op_5(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        return params[1] if params[0] != 0 else opcode_index + 3

    def op_6(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        return params[1] if params[0] == 0 else opcode_index + 3

    def op_7(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        res = 1 if params[0] < params[1] else 0
        self.code[self.code[opcode_index + 3]] = res
        return opcode_index + 4

    def op_8(self, param_modes, opcode_index):
        params = self.get_num_of_params(param_modes, opcode_index, 2)
        res = 1 if params[0] == params[1] else 0
        self.code[self.code[opcode_index + 3]] = res
        return opcode_index + 4

    def op_9(sefl, param_modes, opcode_index):
        return None

    def run_an_op(self, opcode_index):
        opcode, param_modes = self.get_op_and_modes(str(self.code[opcode_index]))
        return getattr(self, "op_{}".format(opcode))(param_modes, opcode_index)


def main():
    with open("data.txt", "r") as f:
        v = f.readline().strip().split(",")
        code = [int(op) for op in v]
    current_max = 0
    max_config = None
    for phases in list(permutations(range(5, 10))):
        amp_array = [IntCodeMachine(phase, code[:]) for phase in phases]
        new_input = 0
        amp_index = 0
        while new_input is not None:
            amp = amp_array[amp_index % 5]
            amp_index += 1
            amp.add_input(new_input)
            new_result = next(amp.generator)
            if new_result is None:
                break # final value rests in new_input
            else:
                new_input = new_result
               
        if new_input > current_max:
            current_max = new_input
            max_config = phases

    print("Max: {} - {}".format(current_max, max_config))


if __name__ == "__main__":
    main()
