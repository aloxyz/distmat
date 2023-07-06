def filter(a, keys):
    for e in keys:
        del a[e]

    return a


def csv_to_dict(csv: [dict]):
    for k, e in enumerate(csv):
        for f, i in e.items():
            if i.isdigit():
                e[f] = int(i)
    return csv