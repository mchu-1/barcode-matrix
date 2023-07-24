# conftest.py

"""Configuration file for pytests."""

import pytest
import numpy as np
from unittest import mock

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
def mock_stuffer() -> str:
    mock_stuffer = "GGTCTCGCTCCGTACCAAGACTTCGAATTC"

    return mock_stuffer

@pytest.fixture
def mock_seq(mock_ref, mock_barcode, mock_stuffer) -> str:
    mock_seq = mock_ref + mock_barcode + mock_stuffer

    return mock_seq

@pytest.fixture
def mock_base() -> np.array:
    mock_base = np.array([["A","C"],
                         ["T","G"]])

    return mock_base

@pytest.fixture
def mock_barcodes(mock_ref, mock_stuffer) -> np.array:
    mock_barcodes = np.array([["AA","AC","CA","CC"],
                        ["AT","AG","CT","CG"],
                        ["TA","TC","GA","GC"],
                        ["TT","TG","GT","GG"]])

    mock_barcodes = np.char.add(np.char.add(mock_ref, mock_barcodes), mock_stuffer)

    return mock_barcodes

@pytest.fixture
def mock_matrix() -> np.ndarray:
    mock_matrix = np.array([[1,2,3,4],
                           [4,1,1,1],
                           [3,0,0,3],
                           [0,1,2,3]])

    return mock_matrix

@pytest.fixture
def mock_sequences(mock_barcodes, mock_matrix) -> list[str]:
    mock_sequences = []
    for i in range(4):
        for j in range(4):
            mock_sequences += [mock_barcodes[i,j]] * mock_matrix[i,j]

    np.random.shuffle(mock_sequences)

    return mock_sequences

@pytest.fixture
def mock_settings() -> dict:
    mock_settings = {"ref": "AATTAAGAAGTCTACAGGAATGGTGAGACC",
                    "k": 2,
                    "g11": "A",
                    "g12": "C",
                    "g21": "T",
                    "g22": "G"}

    return mock_settings

@pytest.fixture
def mock_get_sequences_from_file(mock_sequences):
    with mock.patch("src.process.get_sequences_from_file", return_value=mock_sequences) as mock_data:
        yield mock_data

@pytest.fixture
def mock_get_settings_from_file(mock_settings):
    with mock.patch("src.matrix.read_settings", return_value=mock_settings) as mock_config:
        yield mock_config














