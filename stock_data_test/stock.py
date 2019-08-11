# Modules
import os
import csv
import locale
import sys
locale.setlocale( locale.LC_ALL, '' )


# READ FILE
filename = "2014_stock_data.csv"
foldername = "Resources"
# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)

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
    Ticker = []
    Date_Col = []
    Open = []
    Close = []
    Vol = []
    Uniq_Ticker = []
    Uniq_Vol = []
    totalvolume = 0
    
    # Populate the lists with the delimited data.
    for row in csvreader:
        Ticker.append(str(row[0]))
        Vol.append(float(row[6]))

    for i in range(len(Vol)-1):
        if Ticker[i] != Ticker[i+1]:
            Uniq_Ticker.append(Ticker[i])
            Uniq_Vol.append(float(totalvolume)+Vol[i]) 
            totalvolume = 0
        else:
            totalvolume += float(Vol[i])

    for i in range(len(Uniq_Ticker)):
        print(f"{i} - {Uniq_Ticker[i]} - {Uniq_Vol[i]}")

      