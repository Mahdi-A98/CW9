def indexed_func(*ags):
    result = {}
    for key, value in enumerate(ags):
        result[key + 1] = value
    return result


Enteries = input("Enter your arguments: ")
print(indexed_func(*Enteries.split(" ")))