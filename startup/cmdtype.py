from argparse import ArgumentTypeError


def unsigned(x):
    x = int(x)
    if x < 0:
        raise ArgumentTypeError("Minimum bandwidth is 12")
    return x
