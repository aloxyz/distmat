from startup.cmd import get_args, init_parser
import utils.config as cfg
import ray
import process.processor as proc
import utils.dict_utils as du


def boot():
    init_parser()
    args = get_args()

    cfg.MATRIX_SIZE = args.load
    
    proc.operations = du.filter(proc.operations, args.ignore)

    run()


def run():
    ray.init()

    #processor.run_test()
    ray.shutdown()


if __name__ == "__main__":
    boot()
