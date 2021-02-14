import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

'''
1. The matplotlib.pyplot module contains the Matplotlib library’s graphing capabilities that we use. This module typically is imported with the name plt.

2. The NumPy (Numerical Python) library includes the function unique that we’ll
use to summarize the die rolls. The numpy module typically is imported as np.

3. The random module contains Python’s random-number generation functions.

4. The seaborn module contains the Seaborn library’s graphing capabilities we use.
This module typically is imported with the name sns. Search for why this curious
abbreviation was chosen.
'''

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
    plt.show()

main()