def indexed_func(*ags):
    result = {}
    for key, value in enumerate(ags):
        result[key + 1] = value
    return result


Enteris = input("Enter your arguments: ")
print(indexed_func(*Enteris.split(" ")))