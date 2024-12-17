import argparse

from work_with_card import *
from work_with_file import *
from logging_config import setup_logging

setup_logging()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-card', '--get_card', help='Finds card by hash', action="store_true")
    group.add_argument('-luhn', '--alg_luhn', help='Checks num with Luhn algorithm', action="store_true")
    group.add_argument('-graph', '--graph', help='Draws graph num_of_threads/seconds', action="store_true")

    parser.add_argument('-p', '--paths', type=str, help='Path to json file with paths')
    parser.add_argument('-o_p', '--other_path', type=str, help='Change path to files')

    args = parser.parse_args()
    logging.info(f"Parsed command-line arguments: {args}")

    paths = read_json(args.paths)
    c = read_json(paths["info"])

    match args:
        case args if args.other_path:
            logging.info(f"Changing file paths: {args.other_path}")
            temp = args.other_path.split(",")
            if temp[0] in paths.keys():
                paths[temp[0]] = temp[1]

        case args if args.get_card:
            logging.info("Finding card numbers by hash")
            find_num(c["hash"], c["last_num"], c["bins"], paths["card_num"])

        case args if args.alg_luhn:
            logging.info("Checking card number with Luhn algorithm")
            card_num_str = read_file(paths["card_num"])
            print(f"Card number is {algorithm_luhn(card_num_str)}")

        case args if args.graph:
            logging.info("Generating graph of collision search time")
            data = get_stats(c["hash"], c["last_num"], c["bins"], paths["time"])
            data = list(map(float, data))
            graph(data, paths["graph"])

    write_to_json(args.paths, paths)
