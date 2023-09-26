def find_max(*args):
    if not args:
        return None
    max_arg = args[0]
    for arg in args:
        if arg > max_arg:
            max_arg = arg
    return max_arg


result = find_max(5, 3, 8, 10, 3)
print(result)  