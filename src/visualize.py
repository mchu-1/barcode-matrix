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
    A = special.softmax(A)

    return A

def visualize_matrix(A: np.array, transform: bool = False, upper: float = 6.5*10**-5):
    """
    Visualize matrix.
    Return plot object.
    """
    # Transform matrix
    if transform:
        A = transform_matrix(A)

    # Visualize matrix with fixed upper bound on colormap
    G = sns.heatmap(A, cmap = "viridis", xticklabels = False, yticklabels = False, vmin = 0, vmax = upper)

    return G

# Create 1000 x 1000 matrix with random integer entries
test_matrix = np.random.randint(0, 100, size = (1000, 1000))

# Visualize and show matrix
G = visualize_matrix(test_matrix, transform=True)
plt.show()




