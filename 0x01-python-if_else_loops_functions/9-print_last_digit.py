def print_last_digit(number):
    if number < 0:
        number = number % (-10)
        n = number * -1
    else:
        n = number % 10

    print("{}".format(n), end='')
    return n
