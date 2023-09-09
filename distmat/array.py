# Auxilliary functions for vanilla arrays

def is_array_scalar(array):
    return isinstance(array, (int, float))

def is_array_row(array):
    return isinstance(array, list) and len(array) >= 1 and isinstance(array[0], (int, float))

def is_array_column(array):
    return isinstance(array, list) and len(array) >= 1 and isinstance(array[0], list) and len(array[0]) == 1

def is_array_2d(array):
    return not (is_array_row(array) and is_array_column(array))

def empty_2d_array(rows, columns):
    return [[0] * rows for _ in range(columns)]

def empty_row_array(n):
    return [0 for _ in range(n)]

def empty_column_array(n):
    return [[0] for _ in range(n)]
