import pytest
import pandas as pd
from datetime import date
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw4 import sum_general_int_list
def test_sum_general_int_list():
    nested_list = [1, [2, [3, 4], 5], [6, [7]], 8]
    assert sum_general_int_list(nested_list) == 36, "Should sum to 36"
