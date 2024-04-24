import pandas as pd

df = "swimming_pools.csv"

data_frame = pd.read_csv(df)
print(data_frame)

# sin pandas
import csv

with open(df) as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    for row in csv_read:
        print(', '.join(row))
