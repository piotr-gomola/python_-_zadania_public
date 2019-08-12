
col = [1, 2, 3, ['a', ['A', 'B', 'C'], 'b', 'typ_string', 2.0, (2,3)]]

def flatten_list(col):

    flattened = []

    for item in col:
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

unpacked_col = flatten_list(col)
print(unpacked_col)
