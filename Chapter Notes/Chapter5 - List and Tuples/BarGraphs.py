import matplotlib.pyplot as plt


def main():
    # Creating a list with the X coordinates of each bar's left edge
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar
    heights = [100, 200, 300, 400, 500]

    # Build the bar chart
    bar_width = 10
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'y', 'k'))

    # Add a title
    plt.title("Sales by Year")

    # Add labels to the axis
    plt.xlabel("Year")
    plt.ylabel("Sales")

    # Customize the tick marks
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Display the bar chart
    plt.show()


main()

