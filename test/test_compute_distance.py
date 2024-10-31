import pytest
import pandas as pd
from datetime import date
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw4 import compute_distance
def test_compute_distance():
    coord_pairs = [((37.7749, -122.4194), (34.0522, -118.2437)),  
                   ((51.5074, -0.1278), (48.8566, 2.3522))]       
    result = compute_distance(coord_pairs)
    expected = [559.234, 343.556]  
    for r, e in zip(result, expected):
        assert round(r, 2) == round(e, 2), f"Expected {e}, but got {r}"

