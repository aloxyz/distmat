from startup.cmd import get_args, init_parser


def boot():
    init_parser()
    args = get_args()


def run():
    pass


if __name__ == "__main__":
    boot()
