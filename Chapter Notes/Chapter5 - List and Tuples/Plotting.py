import matplotlib.pyplot as plt


def main():
    x_coord = [0, 1, 2, 3, 4]
    y_coord = [0, 3, 1, 5, 2]

    # The plot function builds the graph in memory but does not display it
    plt.plot(x_coord, y_coord, marker='o')

    # Customizing the plot with names
    plt.title("Sale by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    # Changing lower and Upper limits of the graph
    plt.xlim(xmin=-1, xmax=6)
    plt.ylim(ymin=-1, ymax=6)

    # Tick marks
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Add a grid
    plt.grid(True)

    # To display the graph we use the "show" function
    plt.show()


main()
