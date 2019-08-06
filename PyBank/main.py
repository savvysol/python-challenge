# Modules
import os
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

filename = "budget_data.csv"
filename_out = "PyBank_Output.csv"
foldername = "Resources"

# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)
filepath_out = os.path.join("..", foldername, filename_out)
#print(f"The file path is found here: {filepath}")

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
    totalchange = 0
    total_amount = 0
    maxamount = 0
    minamount = 10000000000000000
    maxchange = float(0)
    minhchage = float(0)
    
    for row in csvreader:
        totalrecords += 1
        total_amount = total_amount + float(row[1])
        thismonth =     row[0]
  
        if float(row[1]) > maxamount:
            maxamount = float(row[1])
            maxmonth = str(row[0])

        if float(row[1]) < minamount:
            minamount = float(row[1])
            minmonth = str(row[0])

    # Create a Header Row
    headerrow = ['Month','Amount','Notes']
    maxrow = [maxmonth,locale.currency(maxamount, grouping=True),'This month had the highest gain.']
    minrow = [minmonth,locale.currency(minamount, grouping=True),'This month had the highest loss.']

       
    print(f"""
        FINANCIAL ANALYSIS
        ----------------------------------------------
        There are {totalrecords} records in this file.
        This is a {col_count}C x {totalrecords}R table.
        The Grand Total over all {totalrecords} entries is {locale.currency(total_amount, grouping=True)}.
        The max amount is {locale.currency(maxamount, grouping=True)} in {maxmonth}.
        The min amount is {locale.currency(minamount, grouping=True)} in {minmonth}.
        {maxrow}
        {minrow}
        
        """)