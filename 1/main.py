def required_fuel(mass):
    return max(0, mass // 3 - 2)


def final_fuel(mass):
    additional_fuel = required_fuel(mass)
    cumulative_additional_fuel = additional_fuel 

    while additional_fuel > 0:
        additional_fuel = required_fuel(additional_fuel)
        cumulative_additional_fuel += additional_fuel
    return cumulative_additional_fuel


total_fuel = 0
with open("modules.txt", "r") as m:
    line = True
    while line:
        line = m.readline().strip()
        if line == "":
            break
        module_mass = int(line)
        total_fuel += final_fuel(module_mass)

print(total_fuel)
