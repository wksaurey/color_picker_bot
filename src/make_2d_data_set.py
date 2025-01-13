import argparse
import random
import sys

def main():
    parser = argparse.ArgumentParser(description="2d Data Generation")
    parser.add_argument('-p', '--points', type=int, help='Number of points')
    parser.add_argument('--max', type=int, default=100, help='Max value')
    parser.add_argument('--min', type=int, default=0, help='Min value')
    parser.add_argument('--filename', type=str, default='2d_data.txt', help='Where to save the data')
    args = parser.parse_args()

    if args.max <= args.min:
        print(f'Please set max to be larger than min')
        sys.exit(1)

    generate_data(args.filename, args.points, args.max, args.min)


def generate_data(filename, points, max, min):
    with open(filename, 'w') as file:
        newline = ''
        for index in range(points):
            x = random.randrange(min, max)
            y = random.randrange(min, max)
            file.write(f'{newline}{x},{y}')
            newline = '\n'

if __name__ == "__main__":
    main()