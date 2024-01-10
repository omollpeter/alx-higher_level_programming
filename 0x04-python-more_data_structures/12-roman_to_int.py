#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_string = roman_string.upper()
    values = []
    for ch in roman_string:
        if ord(ch) == ord('I'):
            values.append(1)
        elif ord(ch) == ord('V'):
            values.append(5)
        elif ord(ch) == ord('X'):
            values.append(10)
        elif ord(ch) == ord('L'):
            values.append(50)
        elif ord(ch) == ord('C'):
            values.append(100)
        elif ord(ch) == ord('D'):
            values.append(500)
        elif ord(ch) == ord('M'):
            values.append(1000)
        else:
            print("Not a roman numeral")
            return

    len_roman = len(values)
    if len_roman == 1:
        return values[0]

    if len_roman == 2:
        if values[0] >= values[1]:
            return values[0] + values[1]
        else:
            return values[1] - values[0]

    i = 0
    total = 0
    while i < len_roman - 1:
        if values[i] >= values[i + 1]:
            total += values[i]
            i += 1
            if i == len_roman - 1:
                total += values[i]
        else:
            total += (values[i + 1] - values[i])
            i += 2

    return total
