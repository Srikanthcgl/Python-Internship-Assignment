import csv
from collections import defaultdict

# Read the first input file and store the data in a dictionary
input1_data = {}
with open('input1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        team_name = row['Team Name']
        name = row['Name']
        if team_name not in input1_data:
            input1_data[team_name] = []
        input1_data[team_name].append(name)

# Read the second input file and store the data in a dictionary
input2_data = {}
with open('input2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['name']
        uid = int(row['uid']);
        total_statements = int(row['total_statements'])
        total_reasons = int(row['total_reasons'])
        input2_data[name] = {'name': name,'uid':uid, 'total_statements': total_statements, 'total_reasons': total_reasons}