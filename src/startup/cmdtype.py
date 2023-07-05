from argparse import ArgumentTypeError


def unsigned(x):
    x = int(x)
    if x < 0:
        raise ArgumentTypeError("Il valore inserito deve essere > 0")
    return x
