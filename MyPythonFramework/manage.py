import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("code", help="increase output verbosity")
args = parser.parse_args()
if args.code == "runserver":
    os.system("color 02 & cd settings & python main.py")
