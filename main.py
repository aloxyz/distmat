from startup.cmd import get_args, init_parser
import ray


def boot():
    init_parser()
    args = get_args()


def run():
    ray.init()
    ray.shutdown()

    pass


if __name__ == "__main__":
    boot()
