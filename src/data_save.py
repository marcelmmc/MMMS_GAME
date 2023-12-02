#import mark
import csv
from definitions import *

print("Data Save")
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
def side_calculations(data):
    """"
    dict_data = [{'timestamp':i[0], 'character':i[1], 'device_type':i[2]} for i in data]
    frame = pd.DataFrame(dict_data)
    """
    side = []
    for i in range(1, len(data)):
        side.append(key_side_to_side(data[i-1][1],data[i][1]))
    return side

#key time difference
def key_time_difference(data):
    time_difference = []
    for i in range(1, len(data)):
        time_difference.append(data[i][0]-data[i-1][0])
    return time_difference

#Type of keyboard

#Erase backspace and space
def clean_data(data):
    data_clean = data
    for i in range(len(data)):
        if data[i][1] != ' ' or data[i][1] != '':
            data_clean.append(data[i])
    return data_clean

#Create final data
def create_final_data(data):
    dataclean = clean_data(data)
    side = side_calculations(dataclean)
    time_difference = key_time_difference(dataclean)
    keyboard = data[0][2]
    final_data = []
    for i in range(len(side)):
        final_data.append((time_difference[i], side[i], keyboard))
    return final_data


#Running test
mock_data = [(0, '', 'MX S'),(0.1, 'a', 'MX S'), (0.15, 'k', 'MX S'), (0.2, 'a', 'MX S'), (0.25, 'k', 'MX S'), (0.3, 'a', 'MX S'), (0.35, 'k', 'MX S'), (0.4, 'a', 'MX S'), (0.45, 'k', 'MX S'), (0.5, 'a', 'MX S'), (0.55, 'k', 'MX S'), (0.6, 'a', 'MX S'), (0.65, 'k', 'MX S'), (0.7, 'a', 'MX S'), (0.75, 'k', 'MX S'), (0.8, 'a', 'MX S'), (0.85, 'k', 'MX S'), (0.9, 'a', 'MX S'), (0.95, 'k', 'MX S'), (1.0, 'a', 'MX S'), (1.05, 'k', 'MX S'), (1.1, 'a', 'MX S'), (1.15, 'k', 'MX S'), (1.2, 'a', 'MX S'), (1.25, 'k', 'MX S'), (1.3, 'a', 'MX S'), (1.35, 'k', 'MX S'), (1.4, 'a', 'MX S'), (1.45, 'k', 'MX S'), (1.5, 'a', 'MX S'), (1.55, 'k', 'MX S'), (1.6, 'a', 'MX S'), (1.65, 'k', 'MX S'), (1.7, 'a', 'MX S'), (1.75, 'k', 'MX S'), (1.8, 'a', 'MX S'), (1.85, 'k', 'MX S'), (1.9, 'a', 'MX S'), (1.95, 'k', 'MX S'), (2.0, 'a', 'MX S'), (2.05, 'k', 'MX S'), (2.1, 'a', 'MX S'), (2.15, 'k', 'MX S'), (2.2, 'a', 'MX S'), (2.25, 'k','')]
def run_test():
    print("Running test")
    file_name = "test.csv"
    create_csv_file(file_name)
    data = create_final_data(mock_data)
    save_data(file_name, data)
    print("Finished test")

run_test()

