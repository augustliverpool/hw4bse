import sys
import os
import pytest
import pandas as pd
from datetime import date
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw4 import count_simba
def test_count_simba():
    strings = ["Simba is a lion", "SIMBA and Nala", "No lion here"]
    assert count_simba(strings) == 2, "Should count 2 occurrences of 'simba'"