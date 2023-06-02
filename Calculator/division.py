def divide(*args):
    try:
        print(args)
        first = args[0]
        result = 0
        for num in list(args[1:]):
            result = first / num
            first = result
        return result
    except ZeroDivisionError:
        print("First element of division operation must be non-zero")

