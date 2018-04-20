#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        if roman_string is not str(roman_string):
            return(0)

        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        symbols = list(roman_string)
        for s in symbols:
            if s not in dic.keys():
                return(0)

        decode = []
        decode = [dic.get(x) for x in symbols]

        sum = 0
        i = 0
        while(i < len(decode)):
            if i is (len(decode) - 1):
                sum += decode[i]
            elif decode[i] < decode[i + 1]:
                sum -= decode[i]
            else:
                sum += decode[i]
            i += 1
        return(sum)
    else:
        return(0)
