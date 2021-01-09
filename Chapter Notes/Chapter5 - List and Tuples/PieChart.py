import matplotlib.pyplot as plt


def main():
    # Create a list of values
    values = [20, 60, 80, 40]

    # Create a list pf labels to represent the values
    slice_labels = ["1st Qtr", "2st Qtr", "3st Qtr", "4st Qtr"]

    # Create a pie chart from teh values
    plt.pie(values, labels=slice_labels, colors=('r', 'g', 'b', 'y', 'k'))

    # Add a title
    plt.title("Sales by quarter")

    # Display the pie chart
    plt.show()


main()
