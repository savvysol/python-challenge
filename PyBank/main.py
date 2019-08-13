# Modules
import os
import csv
import locale
import sys
locale.setlocale( locale.LC_ALL, '' )


# READ FILE
filename = "budget_data.csv"
foldername = "Resources"
# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)

# WRITE FILE
writefilename = "Savvy Financial Analysis.txt"
writefilepath = os.path.join("..",foldername,writefilename)


# Open the CSV, using the path, and Read it
with open(filepath, newline='',encoding="utf-8-sig") as csvfile:
    # After the file is opened, read it and notice the delimiter.
    csvreader = csv.reader(csvfile, delimiter=",")

    # Establish the Header Row and how many columns.
    csv_header = next(csvreader)
    col_count = len(csv_header)
    header = []
    
    # print(f"""
    
    # HEADER ROW:
    # ----------------------""")
    for h in range(col_count):
        header.append(str(csv_header[h]))
        print(f"    {h} - {header[h]}")
      
    
    # Let's initialize some lists.  Think of these like the Column Headers that we're going to populate with data.
    Month_Year = []
    PnL = []
    Change = []
    Year = []
    Month = []
    
    # Populate the lists with the delimited data.
    for row in csvreader:
        Month_Year.append(str(row[0]))
        PnL.append(float(row[1]))
        Year.append(int(row[0][-4:]))
        Month.append(str(row[0][:3]))
  
    for i in range(len(PnL)-1):
        Change.append(float(PnL[i+1]-PnL[i]))
    
    for i in range(len(Change)):
        if Change[i] == float(min(Change)):
            min_change = i+1

    for i in range(len(Change)):
        if Change[i] == max(Change):
            max_change = i+1

    Largest_Gain = float(max(PnL))
    Largest_Loss = float(min(PnL))

    for i in range(len(PnL)):
        if PnL[i] == Largest_Gain:
            Gain_Index = i

    for i in range(len(PnL)):
        if PnL[i] == Largest_Loss:
            Loss_Index = i


    last = int(len(Month))-1

        

print(f""" 
      
  ____       _   __     __ __     __ __   __                                          
 / ___|     / \  \ \   / / \ \   / / \ \ / /                                          
 \___ \    / \ \  \ \ / /   \ \ / /   \ \ /                                           
  ___) |  / / \ \  \ \ /     \ \ /     | |                                            
 |____/  /_/   \_\  \_/       \_/      |_|                                            
  _____   ___   _   _      _      _   _    ____   ___      _      _                     
 |  ___| |_ _| | \ | |    / \    | \ | |  / ___| |_ _|    / \    | |                    
 | |_     | |  |  \| |   / _ \   |  \| | | |      | |    / _ \   | |                    
 |  _|    | |  | |\  |  / ___ \  | |\  | | |___   | |   / ___ \  | |___                 
 |_|     |___| |_| \_| /_/   \_\ |_| \_|  \____| |___| /_/   \_\ |_____|                
     _      _   _      _      _      __   __  ____    ___   ____                        
    / \    | \ | |    / \    | |     \ \ / / / ___|  |_ _| / ___|                       
   / _ \   |  \| |   / _ \   | |      \ V /  \___ \   | |  \___ \                       
  / ___ \  | |\  |  / ___ \  | |___    | |    ___) |  | |   ___) |                      
 /_/   \_\ |_| \_| /_/   \_\ |_____|   |_|   |____/  |___| |____/                       
  _____   _____   _____   _____   _____   _____   _____   _____   _____   _____   _____ 
 |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
                                                                                      
                                                                                
    EXECUTIVE SUMMARY:
    -----------------------
    We looked at {len(PnL)} months of Profit & Loss Data,
    beginning in {Month[0]} of {Year[0]} and ending on {Month[last]} of {Year[last]}.
    The total gain/loss over the {Year[last]-Year[0]} years was {locale.currency(sum(PnL),grouping=True)}.

        GAINS
        ----------------------
        The largest gain of {locale.currency(Largest_Gain,grouping=True)} occurred in {Month_Year[Gain_Index]}.
        The was a change of {locale.currency(PnL[Gain_Index]-PnL[Gain_Index-1],grouping=True)} over the previous month ({Month_Year[Gain_Index-1]}/{locale.currency(PnL[Gain_Index-1],grouping=True)}).
    
        LOSSES
        ----------------------
        The largest loss of {locale.currency(Largest_Loss,grouping=True)} occurred in {Month_Year[Loss_Index]}.
        The was a change of {locale.currency(PnL[Loss_Index]-PnL[Loss_Index-1],grouping=True)} over the previous month ({Month_Year[Loss_Index-1]}/{locale.currency(PnL[Loss_Index-1],grouping=True)}).

        AVERAGES
        -------------------------------
        The average gain/loss was {locale.currency(sum(PnL)/len(PnL),grouping=True)}.
        The average change was {locale.currency(sum(Change)/len(Change),grouping=True)}.
 

    
""")

summary_data = []
header = ['Total Months','Total Amount','Largest Gain Month', 'Largest Gain Amount','Largest Loss Month','Largest Loss Amount','Average Gain/Loss','Average Change']
summary_data.append(len(PnL))
summary_data.append(locale.currency(sum(PnL),grouping=True))
summary_data.append(Month_Year[Gain_Index])
summary_data.append(locale.currency(Largest_Gain,grouping=True))
summary_data.append(Month_Year[Loss_Index])
summary_data.append(locale.currency(Largest_Loss,grouping=True))
summary_data.append(locale.currency(sum(PnL)/len(PnL),grouping=True))
summary_data.append(locale.currency(sum(Change)/len(Change),grouping=True))

financial_analysis_data = zip(header,summary_data)

# save the output file path
output_file = os.path.join("savvy_summary.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(financial_analysis_data)


