import matplotlib.pyplot as plt


def make_scatter(xvals, yvals, xlabel, ylabel):
    plt.scatter(xvals, yvals)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()
