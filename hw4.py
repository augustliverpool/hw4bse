import pandas as pd
from datetime import date
from geopy.distance import geodesic

def count_simba(strings):
    count = 0
    for string in strings:
        count += string.lower().count("simba")
    return count

def get_day_month_year(dates):
    data = {
        'day': [],
        'month': [],
        'year': []
    }
    for d in dates:
        data['day'].append(d.day)
        data['month'].append(d.month)
        data['year'].append(d.year)
    
    return pd.DataFrame(data)

def compute_distance(coord_pairs):
    distances = []
    for (lat1, lon1), (lat2, lon2) in coord_pairs:
        distance = geodesic((lat1, lon1), (lat2, lon2)).kilometers
        distances.append(distance)
    return distances

def sum_general_int_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += sum_general_int_list(element)
    return total
