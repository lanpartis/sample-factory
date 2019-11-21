import sys

from algorithms.utils.arguments import maybe_load_from_checkpoint, get_algo_class, parse_args
from utils.utils import log


def train(cfg):
    cfg = maybe_load_from_checkpoint(cfg)

    algo = get_algo_class(cfg.algo)(cfg)
    algo.initialize()
    status = algo.learn()
    algo.finalize()

    log.info('Done')
    return status


def main():
    """Script entry point."""
    cfg = parse_args()
    return train(cfg)


if __name__ == '__main__':
    sys.exit(main())