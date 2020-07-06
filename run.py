import lib.v1 as lib

import argparse
import os
import sys
import glob



def main():
    parser = argparse.ArgumentParser(description='Compiles Kaze language.')
    parser.add_argument('--dir', help='folder containing .kaze files', required=True)
    args = parser.parse_args()

    lexer = lib.lexer.lg.build()
    parser = lib.parser.pg.build()

    path = os.path.realpath(args.dir)
    files = sorted(glob.glob(os.path.join(path, '*.kaze')))
    for file in files:
        with open(file) as fp:
            print(f'Parsing file {file}')
            mainbox = parser.parse(lexer.lex(fp.read()))
            print(mainbox.name)
            print(mainbox.eval())


if __name__ == '__main__':
    main()
