#!/usr/bin/python

import csv

stats = {}
stats['signed'] = {}
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

past_fields = {
    'assignmentsigned': 'CAA',
    'licensesigned': 'CLA',
    'dcosigned': 'DCO',
    'othersigned': 'Other',
    'othersame': 'in=out',
    'othernopolicy': 'No policy'
}

years = []

# Calculate stats from survey results
with open('data/developer_survey_results.csv', 'rb') as csvfile:
    results = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in results:
        years.append([ int(float(row['yearsflossdeveloper'])), int(float(row['yearsdeveloper'])) ])

        for keyname in past_fields:
            resultkey = past_fields[keyname]
            if not resultkey in stats['signed']:
                stats['signed'][resultkey] = {'yes': 0, 'total': 0}
            if row[keyname] == 'Yes':
                stats['signed'][resultkey]['yes'] += 1
                stats['signed'][resultkey]['total'] += 1
            if row[keyname] == 'No':
                stats['signed'][resultkey]['total'] += 1
            if row[keyname] == "I don't know":
                stats['signed'][resultkey]['total'] += 1

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

past_columns = ['CAA', 'CLA', 'DCO', 'in=out', 'No policy', 'Other' ]
for keyname in past_columns:
    print 'processing ' + keyname
    print 'total is %d ' % stats['signed'][keyname]['total']
    percentage = float(stats['signed'][keyname]['yes']) / float(stats['signed'][keyname]['total']) * 100
    line = "%s,%d,%d,%.2f\n" % (keyname,stats['signed'][keyname]['yes'], stats['signed'][keyname]['total'], percentage)
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

dat_file = open('graphs/experience.dat', 'w')
dat_file.write("# yearsflossdeveloper, yearsdeveloper\n")
for pair in years:
    line = "%d,%d\n" % (pair[0], pair[1])
    dat_file.write(line)

dat_file.close()
