import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    graph_2d_data()
    graph_image_rgb()

def graph_image_rgb():
    image_filename = 'images/not_interesting_sub_logo.jpeg'
    plot_filename = 'image_rgb_plot.png'

def graph_2d_data():
    data_filename = 'data/2d_data.txt'
    plot_filename = 'images/2d_plot.png'

    generate_data(data_filename, 100, 100, 0)
    with open(data_filename) as file:
        x_values, y_values = zip(*list(map(lambda line : line.strip().split(','), file.readlines())))
        x_values = np.array(list(map(int, x_values)))
        y_values = np.array(list(map(int, y_values)))

        plt.plot(x_values, y_values, 'o')
        plt.savefig(plot_filename)

def generate_data(filename, points, max, min):
    with open(filename, 'w') as file:
        newline = ''
        for _ in range(points):
            x = random.randrange(min, max)
            y = random.randrange(min, max)
            file.write(f'{newline}{x},{y}')
            newline = '\n'

if __name__ == '__main__':
    main()