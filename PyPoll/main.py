# Modules
import os
import csv

filename = "budget_data.csv"
foldername = "Resources"

# Set path for the file, assumes up one dir and down into 'foldername' to find 'filename'
filepath = os.path.join("..",foldername, filename)
print(f"The file path is found here: {filepath}")
