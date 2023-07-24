# visualize.py

"""Visualize matrix."""

from matrix import *
import seaborn as sns
from matplotlib import pyplot as plt

def transform_matrix(A: np.array) -> np.array:
    """
    Apply a transformation element-wise to a matrix.
    """
    A = np.array([10**x for x in A])

    return A

def visualize_matrix(A: np.array, transform: bool = False):
    """
    Visualize matrix.
    Return plot object.
    """
    # Transform matrix
    if transform:
        A = transform_matrix(A)

    # Visualize matrix
    G = sns.heatmap(A, cmap = "mako", xticklabels = False, yticklabels = False)

    return G

# Create 1000 x 1000 matrix with random integer entries
test_matrix = np.random.randint(0, 100, size = (1000, 1000))

# Visualize and show matrix
G = visualize_matrix(test_matrix)
plt.show()




