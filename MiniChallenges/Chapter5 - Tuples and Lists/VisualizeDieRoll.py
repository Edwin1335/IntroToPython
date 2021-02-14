import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import seaborn as sns
import sys


def update(frame_number, rolls, faces, frequencies):
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1
     # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(faces, frequencies, palette='bright')  # new bars
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%
    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')
    # read command-line arguments for number of frames and rolls per frame
    number_of_frames = int(sys.argv[1])
    rolls_per_frame = int(sys.argv[2])
    sns.set_style('whitegrid')  # white background with gray grid lines
    figure = plt.figure('Rolling a Six-Sided Die')  # Figure for animation
    values = list(range(1, 7))  # die faces for display on x-axis
    frequencies = [0] * 6  # six-element list of die frequencies
    die_animation = animation.FuncAnimation(
        figure, update, repeat=False, frames=number_of_frames, interval=33, fargs=(rolls_per_frame, values, frequencies))
    plt.show()


def main():
    rolls = [random.randrange(1, 7) for i in range(600)]
    values, frequencies = np.unique(rolls, return_counts=True)
    title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
    sns.set_style("whitegrid")
    axes = sns.barplot(values, frequencies, palette='bright')
    axes.set_title(title)
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    update()


update()
