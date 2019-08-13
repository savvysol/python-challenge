# Modules
import os
import csv
import locale
import pandas as pd
locale.setlocale(locale.LC_ALL, 'en_US')

# READ FILE
filename = "election_data.csv"
foldername = "Resources"
# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)

# Open the CSV, using the path, and Read it
with open(filepath, newline='') as csvfile:
    # After the file is opened, read it and notice the delimiter.
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(type(csvreader))

    # Establish the Header Row and how many columns.
    csv_header = next(csvreader)
    col_count = len(csv_header)
    header = []
    
    # What are my header names
    # for h in range(col_count):
    #     header.append(str(csv_header[h]))
    #     print(f"    {h} - {header[h]}")

    # Let's initialize some lists.  Think of these like the Column Headers that we're going to populate with data.
    county_ = []
    candidates_ = []
    votes = 0

    # Populate the lists with the delimited data.
    for row in csvreader:
        county_.append(row[1])
        candidates_.append(row[2])
        votes += 1
    
    # Get unique lists from each list
    county = []
    candidate = []    

    # Get unique candidates
    for i in candidates_:
        if i not in candidate:
            candidate.append(i)
    
    # Get unique counties
    for i in county_:
        if i not in county:
            county.append(i)

    # Lists for the Results
    results_county = []
    results_candidate = []
    results_votes = []

    

    # print(county)
    # print(candidate)
        
    
    
    
    
print(f"""

----------------------------------------------------------------------------------  
 _______  __       _______   ______ .___________. __    ______   .__   __.      
 |   ____||  |     |   ____| /      ||           ||  |  /  __  \  |  \ |  |      
 |  |__   |  |     |  |__   |  ,----'`---|  |----`|  | |  |  |  | |   \|  |      
 |   __|  |  |     |   __|  |  |         |  |     |  | |  |  |  | |  . `  |      
 |  |____ |  `----.|  |____ |  `----.    |  |     |  | |  `--'  | |  |\   |      
 |_______||_______||_______| \______|    |__|     |__|  \______/  |__| \__|      
 .______       _______      _______. __    __   __      .___________.    _______.
 |   _  \     |   ____|    /       ||  |  |  | |  |     |           |   /       |
 |  |_)  |    |  |__      |   (----`|  |  |  | |  |     `---|  |----`  |   (----`
 |      /     |   __|      \   \    |  |  |  | |  |         |  |        \   \    
 |  |\  \----.|  |____ .----)   |   |  `--'  | |  `----.    |  |    .----)   |   
 | _| `._____||_______||_______/     \______/  |_______|    |__|    |_______/    
                                                                                 
----------------------------------------------------------------------------------- 
There were {locale.format_string("%d",votes/1000000,grouping=True)}M votes cast for {len(candidate)} candidates in {len(county)} counties.

Our Candidates are:""")
for i in candidate:
    print(f"     • {i}")

#--------------------------------------------------------------------------------------------
# Some addtiional Reporting at the County level.

print(f"""
Counties Reporting:
---------------------------""")

vote_count = 0
for c in county:
    for v in range(len(county_)):
        if county_[v] == c:
            vote_count += 1
    print(f"    {c} County had {locale.format_string('%d',vote_count,grouping=True)} votes for {round(vote_count/votes*100,2)}% of the votes.")
    vote_count = 0


for i in county:
    print(f"""
    {i} County Results:
    --------------------------- """)
    for c in candidate:
        for v in range(votes):
            if candidates_[v] == c and county_[v] == i:
                vote_count += 1
        print(f"        • {c} received {locale.format_string('%d',vote_count,grouping=True)} votes ({round(vote_count/votes*100,2)}%)")
        results_candidate.append(c)
        results_county.append(i)
        results_votes.append(vote_count)
        vote_count = 0

#--------------------------------------------------------------------------------------------

# Here is the official assiginment  
print(f"""
---------------------------------------
ELECTION RESULTS - OVERALL
---------------------------------------""")

most_votes = 0
for c in candidate:
    for v in range(votes):
        if candidates_[v] == c:
            vote_count += 1
    print(f"    {c}: {round(vote_count/votes*100,2)}% ({locale.format_string('%d',vote_count,grouping=True)})")
    if vote_count > most_votes:
        most_votes = vote_count
        winner = c
    vote_count = 0

print(f"""---------------------------------------
WINNER: {winner} with {locale.format_string('%d',most_votes,grouping=True)} votes.
---------------------------------------
""")

election_output = zip(results_candidate,results_county,results_votes)

# save the output file path
output_file = os.path.join("pypoll_output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Candidate','County','Total Votes Received'])
    writer.writerows(election_output)

    


    