# conftest.py

"""Configuration file for pytests."""

import pytest
import numpy as np

@pytest.fixture
def mock_barcode() -> str:
    mock_barcode = "ACTG"

    return mock_barcode

@pytest.fixture
def mock_indexes() -> list:
    mock_indexes = [3, 5]

    return mock_indexes

@pytest.fixture
def mock_ref() -> str:
    mock_ref = "AATTAAGAAGTCTACAGGAATGGTGAGACC"

    return mock_ref

@pytest.fixture
def mock_seq(mock_ref, mock_barcode) -> str:
    mock_seq = mock_ref + mock_barcode + "GGTCTCGCTCCGTACCAAGACTTCGAATTC"

    return mock_seq

@pytest.fixture
def mock_base() -> np.array:
    mock_base = np.array([["A","C"],
                         ["T","G"]])

    return mock_base

@pytest.fixture
def mock_barcodes() -> np.array:
    mock_barcodes = np.array([["AA","AC","CA","CC"],
                        ["AT","AG","CT","CG"],
                        ["TA","TC","GA","GC"],
                        ["TT","TG","GT","GG"]])

    return mock_barcodes

@pytest.fixture
def mock_matrix() -> np.ndarray:
    mock_matrix = np.array([[1,2,3,4],
                           [4,1,1,1],
                           [3,0,0,3],
                           [0,1,2,3]])

    return mock_matrix








