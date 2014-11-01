#!/usr/bin/python

import csv

stats = {}
stats['signed'] = {'license': 0, 'assign': 0, 'dco': 0, 'other': 0, 'ltotal': 0, 'atotal': 0, 'dtotal': 0, 'ototal': 0}
stats['willing'] = {'license': 0, 'assign': 0, 'dco': 0, 'other': 0, 'ltotal': 0, 'atotal': 0, 'dtotal': 0, 'ototal': 0}

# Calculate stats from survey results
with open('data/developer_survey_results.csv', 'rb') as csvfile:
    results = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in results:
        #print int(float(row['yearsdeveloper']))
        #print int(float(row['yearsflossdeveloper']))
        #print row['developercomments']
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
