# visualize.py

"""Visualize matrix."""

from matrix import *
import seaborn as sns
from scipy import special
from matplotlib import pyplot as plt

def transform_matrix(A: np.array) -> np.array:
    """
    Apply a transformation element-wise to a matrix.
    """
    # Sigmoid transform
    A = special.expit(A)

    # Min-max normalize
    A = (A - A.min())/(A.max() - A.min())

    return A

def visualize_matrix(A: np.array, transform: bool = True):
    """
    Visualize matrix.
    Return plot object.
    """
    # Transform matrix
    if transform:
        A = transform_matrix(A)

    # Visualize matrix with fixed upper bound on colormap
    # Text and ticks are white
    G = sns.heatmap(A, cmap = "mako", xticklabels = False, yticklabels = False, vmax = 1)
    # Generate figure
    G = G.get_figure()

    return G

# Create 1000 x 1000 matrix with random integer entries
# test_matrix = np.random.randint(0, 100, size = (1000, 1000))

# Visualize and show matrix
# G = visualize_matrix(test_matrix, transform=True)
# plt.show()




