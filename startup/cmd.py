from argparse import ArgumentParser
from startup.cmdtype import unsigned

parser = ArgumentParser(
    prog="Progetto di Laboratorio di reti e sistemi distribuiti",
    description="Progetto creato per Laboratorio di reti e sistemi distribuiti")


def init_parser():
    parser.add_argument('-i', '--ignore', nargs="*", choices=["p", "d", "i"], help="ignora un'operazione matriciale[p: prodotto, d: determinante, i: inversa]")
    parser.add_argument('-l', '--load', nargs=1, type=unsigned, required=True)


def get_args():
    return parser.parse_args()
