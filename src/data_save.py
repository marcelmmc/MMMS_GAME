import mark
import csv
from definitions import *

#--------------------------------------------------
# Data Save
#--------------------------------------------------
def create_csv_file(file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        field = ['Time_Difference', 'side_to_side', 'keyboard']
        writer.writerow(field)

def save_data(file_name, data):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for input in data:
            writer.writerow(input)


mock_data = [(0.1, 'a', 'MX S'), (0.15, 'k', 'MX S'), (0.2, 'a', 'MX S'), (0.25, 'k', 'MX S'), (0.3, 'a', 'MX S'), (0.35, 'k', 'MX S'), (0.4, 'a', 'MX S'), (0.45, 'k', 'MX S'), (0.5, 'a', 'MX S'), (0.55, 'k', 'MX S'), (0.6, 'a', 'MX S'), (0.65, 'k', 'MX S'), (0.7, 'a', 'MX S'), (0.75, 'k', 'MX S'), (0.8, 'a', 'MX S'), (0.85, 'k', 'MX S'), (0.9, 'a', 'MX S'), (0.95, 'k', 'MX S'), (1.0, 'a', 'MX S'), (1.05, 'k', 'MX S'), (1.1, 'a', 'MX S'), (1.15, 'k', 'MX S'), (1.2, 'a', 'MX S'), (1.25, 'k', 'MX S'), (1.3, 'a', 'MX S'), (1.35, 'k', 'MX S'), (1.4, 'a', 'MX S'), (1.45, 'k', 'MX S'), (1.5, 'a', 'MX S'), (1.55, 'k', 'MX S'), (1.6, 'a', 'MX S'), (1.65, 'k', 'MX S'), (1.7, 'a', 'MX S'), (1.75, 'k', 'MX S'), (1.8, 'a', 'MX S'), (1.85, 'k', 'MX S'), (1.9, 'a', 'MX S'), (1.95, 'k', 'MX S'), (2.0, 'a', 'MX S'), (2.05, 'k', 'MX S'), (2.1, 'a', 'MX S'), (2.15, 'k', 'MX S'), (2.2, 'a', 'MX S'), (2.25, 'k','')]
#--------------------------------------------------
# Data Processing
#--------------------------------------------------
data = []
#keys_side
def key_side_to_side(key1, key2):
    key1_l = key1.lower()
    key2_l = key2.lower()
    if key1_l in rights_key:
        if key2_l in rights_key:
            return Side.RIGHT_RIGHT
        elif key2_l in lefts_key:
            return Side.RIGHT_LEFT
        else:
            return Side.RIGHT
    elif key1_l in lefts_key:
        if key2_l in rights_key:
            return Side.LEFT_RIGHT
        elif key2_l in lefts_key:
            return Side.LEFT_LEFT
        else:
            return Side.LEFT
    else:
        return Side.ERROR
    
#modify data with side_to_side
def modify_data(data, sides):
    for i in range(len(data)):
        if i == 0:
            si
        else:
            data[i,1].append(key_side_to_side(data[i-1][1],data[i][1]))
    return data

