def subtract(*args):
    first = args[0][0]
    result = 0
    for num in list(args[0][1:]):
        result = first - num
        first = result
    return result
