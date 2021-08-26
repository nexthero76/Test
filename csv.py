import os
import pandas as pd


# get csv file name list
path = r"./Engineering Test Files"
file_lists = []
for _, _, files in os.walk(path):
    for file_item in files:
        file_info = os.path.splitext(file_item)
        if file_info[0] != "Combined" and file_info[1] == ".csv":
            file_lists.append(file_item)
            
# get "Source IP" and "name" lists            
combined_dict={}
for file_item in file_lists:
    path = r"./Engineering Test Files/" + file_item
    file_name = os.path.splitext(file_item)[0]
    df = pd.read_csv(path)
    for item in df['Source IP']:
        combined_dict[item] = file_name

ip_index = []
for key in combined_dict.keys():
    first_elem = int(key.split('.')[0])
    ip_index.append(first_elem)

# update Combined.csv
data2 = {"Source IP": combined_dict.keys(), "Environment": combined_dict.values()}
combined_df = pd.DataFrame(data2,index=ip_index)
combined_df.sort_index().to_csv("./Engineering Test Files/Combined.csv", index=False)