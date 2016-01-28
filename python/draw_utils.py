__author__ = 'binus'

import math
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

def show_heatmap(data):

    # Place individual heatmaps so they occupy roughly square area.
    shape = data.shape
    cols = math.ceil(math.sqrt(1.0 * shape[1] * shape[2] / shape[0]))
    rows = math.ceil(1.0 * shape[2] / cols)

    # Use Red->Black->Blue color scheme.
    cmap = rb_cm()

    # Center data range so the 0 is black.
    vmax = np.amax(np.abs(data))
    vmin = -vmax

    # Plot individual graphs.
    fig = plt.figure()
    for i in range(0, shape[2]):
      a = fig.add_subplot(rows, cols, i + 1)
      a.set_title(i)
      plt.axis('off')
      im = plt.imshow(data[:,:,i], cmap=cmap, vmin=vmin, vmax=vmax)

    # Plot the color bar.
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)

    # Show the result.
    plt.show()

def rb_cm():
    cdict = {
        'red':   ((0.0, 1.0, 1.0),
                  (0.5, 0.0, 0.0),
                  (1.0, 0.0, 0.0)),

        'green': ((0.0, 0.0, 0.0),
                  (1.0, 0.0, 0.0)),

        'blue':  ((0.0, 0.0, 0.0),
                  (0.5, 0.0, 0.0),
                  (1.0, 1.0, 1.0))
    }
    return LinearSegmentedColormap('RedBlackBlue', cdict)