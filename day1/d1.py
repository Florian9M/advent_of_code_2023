digits_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

def convert_literal_to_digit(s):
    for word, digit in digits_dict.items():
        s = s.replace(word, str(digit))
    return s

def sum_of_calibration(file_name: str) -> int:
    with open(file_name, "r") as file:
        sum_of_calibration = 0
        for line in file.readlines():
            line = convert_literal_to_digit(line) # for Part 2
            digits = []
            for c in line:
                if c.isdigit():
                    digits.append(c)
            if len(digits) > 1:
                two_digit_number = digits[0] + digits[-1]
            else:
                two_digit_number = digits[0] * 2
            sum_of_calibration += int(two_digit_number)
            print(sum_of_calibration)

sum_of_calibration("input.txt")