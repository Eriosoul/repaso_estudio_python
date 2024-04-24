import csv

df = "nombres.csv"
data = [["Name", "Address", "Age"], ["Erio", "Toledo", "27"]]

with open(df, "w") as data_frame:
    writer = csv.writer(data_frame)
    writer.writerows(data)

print("Datos escritos...")
