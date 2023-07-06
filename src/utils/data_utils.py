import os


PROJECT_ROOT = os.path.abspath(os.curdir)


def to_ppath(path: str) -> str:
    return os.path.join(PROJECT_ROOT, path)


def data_path(filename: str) -> str:
    return to_ppath("..\\data\\" + filename)
