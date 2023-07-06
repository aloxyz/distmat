from startup.cmd import get_args, init_parser
import utils.config as cfg
import ray
import process.processor as proc
import utils.dict_utils as du
from data.storage_manager import store_data


def boot():
    init_parser()
    args = get_args()

    cfg.MATRIX_SIZE = int(args.load[0])

    if args.ignore is not None:
        proc.operations = du.filter(proc.operations, args.ignore)

    run()


def run():
    ray.init()

    data_res = proc.exec_test(cfg.MATRIX_SIZE)

    store_data('test/single', data_res[0])
    store_data('test/parallel', data_res[1])

    ray.shutdown()


if __name__ == "__main__":
    boot()
