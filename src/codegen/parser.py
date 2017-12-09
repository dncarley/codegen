import argparse


def register_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--framework",
                        choices=['flask', 'gatling', 'nodejs'],
                        help="Select output framework")
    parser.add_argument("-i", "--input",
                        help="Input file")
    return parser
