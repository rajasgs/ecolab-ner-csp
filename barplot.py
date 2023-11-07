




'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/14270391/how-to-plot-multiple-bars-grouped
'''

from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# 
import metrics_collector as mec

def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())

def plot1():

    # Usage example:
    data = {
        "v1": [0.9720, 0.9727, 0.9723],
        "v2": [0.9620, 0.9900, 0.9100],
    }

    fig, ax = plt.subplots()
    bar_plot(ax, data, total_width=.8, single_width=.9)
    plt.show()



def plot2():

    '''
        'entity' : 0,
        'p' : 1,
        'r' : 2,
        'f1' : 3,
        'tp' : 4,
        'fp' : 5,
        'fn' : 2
    '''

    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

    _, total_metrics_1 = mec.get_metrics_from_text('metrics_result_1.txt')
    _, total_metrics_2 = mec.get_metrics_from_text('metrics_result_2.txt')

    print(total_metrics_2)

    # return

    graph_title = 'NLP Mertics Comparison'
    
    # data from https://allisonhorst.github.io/palmerpenguins/

    species = ("precision", "recall", "f1")
    model_versions = {
        'v1': (total_metrics_1['p'], total_metrics_1['r'], total_metrics_1['f1']),
        'v2': (total_metrics_2['p'], 0.9927, 0.9123),
    }

    print(model_versions)

    # return

    x           = np.arange(len(species))  # the label locations
    width       = 0.25  # the width of the bars
    multiplier  = 0

    fig, ax     = plt.subplots(layout='constrained')

    for attribute, measurement in model_versions.items():
        offset  = width * multiplier
        rects   = ax.bar(x + offset, measurement, width, label = attribute)
        ax.bar_label(rects, padding = 3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Accuracy')
    ax.set_title(graph_title)
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 2)

    plt.show()

def startpy():

    # plot1()

    plot2()
    
    pass

if __name__ == '__main__':
    startpy()