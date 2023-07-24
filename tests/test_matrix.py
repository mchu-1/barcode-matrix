# test_matrix.py

"""Unit tests for matrix.py"""

from src import matrix
from conftest import *

### Test barcode lookup
def test_get_barcode(mock_seq, mock_ref, mock_barcode):
    assert matrix.get_barcode(mock_seq, mock_ref, len(mock_barcode)) == mock_barcode

### Test matrix indexing
def test_get_indexes(mock_barcode, mock_base, mock_indexes):
    assert matrix.get_indexes(mock_barcode, mock_base) == mock_indexes

### Test matrix generation
def test_generate_matrix(mock_get_sequences_from_file, mock_get_settings_from_file, mock_matrix):
    A = matrix.generate_matrix("mock_input.fastq", "mock_config.yaml")
    assert np.array_equal(A, mock_matrix)







