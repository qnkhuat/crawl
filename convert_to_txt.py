import json_lines as jl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f',nargs='*')
args=parser.parse_args()

for arg in args.f:

    with open(arg) as f:
        data= jl.reader(f)
        for line in data:
            txt= open('dic.txt','a')
            txt.write(line['vin'] + '\n')
