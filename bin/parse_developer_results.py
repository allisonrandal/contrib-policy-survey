#!/usr/bin/python

import csv

stats = {}
stats['signed'] = {'license': 0, 'assign': 0, 'dco': 0, 'other': 0, 'ltotal': 0, 'atotal': 0, 'dtotal': 0, 'ototal': 0}
stats['future'] = {
    'license': {
        'total': 0,
        'willing': 0,
        'neutral': 0,
        'unwilling': 0
    },
    'assignment': {
        'total': 0,
        'willing': 0,
        'neutral': 0,
        'unwilling': 0
    },
    'dco': {
        'total': 0,
        'willing': 0,
        'neutral': 0,
        'unwilling': 0
    },
}

# Calculate stats from survey results
with open('data/developer_survey_results.csv', 'rb') as csvfile:
    results = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in results:
        if row['licensesigned'] == 'Yes':
            stats['signed']['license'] += 1
            stats['signed']['ltotal'] += 1

        if row['licensesigned'] == 'No':
            stats['signed']['ltotal'] += 1

        if row['assignmentsigned'] == 'Yes':
            stats['signed']['assign'] += 1
            stats['signed']['atotal'] += 1

        if row['assignmentsigned'] == 'No':
            stats['signed']['atotal'] += 1

        if row['dcosigned'] == 'Yes':
            stats['signed']['dco'] += 1
            stats['signed']['dtotal'] += 1

        if row['dcosigned'] == 'No':
            stats['signed']['dtotal'] += 1

        if row['othersigned'] == 'Yes':
            stats['signed']['other'] += 1
            stats['signed']['ototal'] += 1

        if row['othersigned'] == 'No':
            stats['signed']['ototal'] += 1

        for keyname in stats['future']:
            cellvalue = row[keyname+'willing']
            if not cellvalue:
                continue
            rating = int(float(cellvalue))
                
            stats['future'][keyname]['total'] += 1
            if rating == 3:
                stats['future'][keyname]['neutral'] += 1
            if rating >= 1 and rating < 3:
                stats['future'][keyname]['unwilling'] += 1
            if rating > 3 and rating <= 5:
                stats['future'][keyname]['willing'] += 1

# Write out stats suitable for graph generation
dat_file = open('graphs/signed.dat', 'w')
dat_file.write("# type,signed,total,percentage\n")

license_percentage = float(stats['signed']['license']) / float(stats['signed']['ltotal']) * 100
line = "CLA,%d,%d,%.2f\n" % (stats['signed']['license'], stats['signed']['ltotal'], license_percentage)
dat_file.write(line)

assign_percentage = float(stats['signed']['assign']) / float(stats['signed']['atotal']) * 100
line = "CAA,%d,%d,%.2f\n" % (stats['signed']['assign'], stats['signed']['atotal'], assign_percentage)
dat_file.write(line)

dco_percentage = float(stats['signed']['dco']) / float(stats['signed']['dtotal']) * 100
line = "DCO,%d,%d,%.2f\n" % (stats['signed']['dco'], stats['signed']['dtotal'], dco_percentage) 
dat_file.write(line)

other_percentage = float(stats['signed']['other']) / float(stats['signed']['ototal']) * 100
line = "Other,%d,%d,%.2f\n" % (stats['signed']['other'], stats['signed']['ototal'], other_percentage) 
dat_file.write(line)

dat_file.close()

dat_file = open('graphs/future.dat', 'w')
dat_file.write("# type,willing,neutral,unwilling,total\n")
for keyname in stats['future']:
    agtype = keyname
    if keyname == 'license':
        agtype = 'CLA'
    if keyname == 'assignment':
        agtype = 'CAA'
    total = float(stats['future'][keyname]['total'])
    neutral = float(stats['future'][keyname]['neutral']) / total * 100
    willing = float(stats['future'][keyname]['willing']) / total * 100
    unwilling = float(stats['future'][keyname]['unwilling']) / total * 100
    line = "%s,%.2f,%.2f,%.2f,%d\n" % (agtype.upper(), willing, neutral, unwilling, total) 
    dat_file.write(line)

dat_file.close()
