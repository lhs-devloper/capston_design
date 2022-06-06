from pathlib import Path
from argparse import ArgumentParser

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]


def run(weights=ROOT / "yolov5s.pt"):
    pass


def parse_opt():
    parser = ArgumentParser()
    parser.add_argument(
        "--weights",
        nargs="+",
        type=str,
        default=ROOT / "yolov5s.pt",
        help="model path(s)",
    )
    return opt


def main(opt):
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
