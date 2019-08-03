# Modules
import os
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

filename = "budget_data.csv"
foldername = "Resources"

# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)
print(f"The file path is found here: {filepath}")

# Open the CSV, using the path, and Read it
with open(filepath, newline='',encoding="utf-8-sig") as csvfile:
    # After the file is opened, read it and notice the delimiter.
    csvreader = csv.reader(csvfile, delimiter=",")

    # Establish the Header Row and how many columns.
    csv_header = next(csvreader)
    col_count = len(csv_header)
    
    print(f"There are {col_count} column(s) in this file.")
    print(f"The Header Row Looks like this:  {csv_header}")
    for header in range(col_count):
        print(f"{header} - {csv_header[header]}")

    # Let's find out how many rows/records are in this data set
    
    # Let's initialize some variables
    totalrecords = 0
    total_amount = 0

    
    for row in csvreader:
        totalrecords += 1
        total_amount = total_amount + float(row[1])
      
    print(f"""
        There are {totalrecords} records in this file.
        This is a {col_count}C x {totalrecords}R table.
        The Grand Total over all {totalrecords} entries is {locale.currency(total_amount, grouping=True)}.
        """)