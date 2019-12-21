#!/usr/bin/python3.6

def meets_conditions(num):
    digits = [int(d) for d in str(num)]
    consecutive = False
    for index in range(len(digits) - 1):
        if digits[index] > digits[index + 1]:
            return False
        consecutive = consecutive or digits[index] == digits[index + 1]
    return consecutive

def main():
    count = 0
    for number in range(168630, 718098):
        if meets_conditions(number):
            count += 1
    print(count)

main()
