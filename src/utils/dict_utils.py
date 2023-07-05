def filter(a, keys):
    for e in keys:
        del a[e]

    return a