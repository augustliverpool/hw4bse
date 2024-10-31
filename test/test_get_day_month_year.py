import pytest
import pandas as pd
from datetime import date
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw4 import  get_day_month_year


def test_get_day_month_year():
    dates = [date(2021, 1, 1), date(2022, 12, 31), date(2023, 6, 15)]
    result = get_day_month_year(dates)
    expected = pd.DataFrame({
        'day': [1, 31, 15],
        'month': [1, 12, 6],
        'year': [2021, 2022, 2023]
    })
    pd.testing.assert_frame_equal(result, expected)