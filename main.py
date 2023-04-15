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


# Calculate the average statements read and total reasons read for each team
team_stats = defaultdict(lambda: {'total_statements': 0, 'total_reasons': 0, 'count': 0})
for team_name, users in input1_data.items():
    for name in users:
        if name in input2_data:
            stats = input2_data[name]
            team_stats[team_name]['total_statements'] += stats['total_statements']
            team_stats[team_name]['total_reasons'] += stats['total_reasons']
            team_stats[team_name]['count'] += 1

team_averages = {}
for team_name, stats in team_stats.items():
    if stats['count'] > 0:
        average_statements = round(stats['total_statements'] / stats['count'],2)
        average_reasons = round(stats['total_reasons'] / stats['count'],2)
        team_averages[team_name] = {'average_statements': average_statements, 'average_reasons': average_reasons,'rank': average_statements+average_reasons}
