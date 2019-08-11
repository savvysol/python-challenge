# Modules
import os
import csv

# READ FILE
filename = "2014_stock_data.csv"
foldername = "Resources"

# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join(".", filename)

# Open the CSV, using the path, and Read it
with open(filepath, newline='',encoding="utf-8-sig") as csvfile:
    
    # After the file is opened, read it and notice the delimiter.
    csvreader = csv.reader(csvfile, delimiter=",")

    # Establish the Header Row and how many columns.
    csv_header = next(csvreader)
    col_count = len(csv_header)
    header = []

    for h in range(col_count):
        header.append(str(csv_header[h]))
        print(f"    {h} - {header[h]}")

    # Let's initialize some lists.  Think of these like the Column Headers that we're going to populate with data.
    Col_A = []
    Col_B = []
    
   
      