# matrix.py

"""Generates barcode matrix from file."""

from src import process
import numpy as np
import yaml

def initiate_matrix(k: int) -> np.array:
    """
    Initiate matrix with zero entries.
    """
    empty_matrix = np.zeros([2**k, 2**k])

    return empty_matrix


def define_base(g11, g12, g21, g22: int) -> np.array:
    """
    Define a base matrix.
    """
    base = np.array([[g11, g12], [g21, g22]])

    return base


def get_barcode(seq, ref: str, k: int) -> str:
    """
    Get barcode from string given a reference.
    """
    # Look ahead from reference
    barcode = seq.split(ref)[1][:k]

    return barcode


def get_indexes(barcode: str, base: np.array) -> list:
    """
    Get indexes of barcode by descent using the base case matrix.
    """
    # Length of barcode
    k = len(barcode)

    # Initiate indexes
    x, y = [0, 2**k], [0, 2**k]

    # Find indexes by limit descent
    for i in range(k):
        j = np.where(base == barcode[i])
        x = [x[0], (x[1] + x[0] - 1) / 2] if j[0] == 0 else [(x[1] + x[0] - 1) / 2 + 1, x[1]]
        y = [y[0], (y[1] + y[0] - 1) / 2] if j[1] == 0 else [(y[1] + y[0] - 1) / 2 + 1, y[1]]

    x = int(x[0])
    y = int(y[0])

    # Return indexes
    return [x, y]


def read_settings(config_f: str):
    """
    Generate settings dictionary from config YAML.
    """
    settings = yaml.safe_load(config_f)

    return settings


def generate_matrix(input_f, config_f: str) -> np.array:
    """
    Generate barcode matrix from input FASTQ and config YAML.
    """
    if input_f.split(".")[-1] != "fastq":
        raise ValueError("Input file must be in FASTQ format.")

    if config_f.split(".")[-1] != "yaml":
        raise ValueError("Config file must be in YAML format.")

    # Read sequences from input file
    sequences = process.get_sequences_from_file(input_f)

    # Read settings from config file
    settings = read_settings(config_f)
    ref = settings["ref"]
    k = settings["k"]
    g11, g12, g21, g22 = settings["g11"], settings["g12"], settings["g21"], settings["g22"]

    # Generate barcode matrix
    A = initiate_matrix(k)
    b = define_base(g11, g12, g21, g22)
    for seq in sequences:
        barcode = get_barcode(seq, ref, k)
        x, y = get_indexes(barcode, b)
        A[x, y] += 1

    A = A.astype(int)

    return A












