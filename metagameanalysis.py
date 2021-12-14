import csv
from stattools import binomial_distribution
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

infolder = 'resources\\'
outfolder = 'output_data\\'


def create_from_csv(filename):
    decklists = []
    with open(infolder + filename) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            decklists.append(
                {'deckname': row[0], 'count': row[1], 'winrate': float(row[2])/100})

    return decklists


def binomialcalculation(deck, rounds, record):
    winrate = deck['winrate']
    bd = binomial_distribution()
    winning = bd.pmf(record, rounds, winrate)
    return winning


def binomial_analysis():
    # generate deck data
    deck_data = create_from_csv('standard_breakdown.csv')

    # tournament
    rounds = 12
    # number of wins needed for money
    record = 10

    # calculate percentage of winning
    for d in deck_data:
        d['binomialwin'] = binomialcalculation(d, rounds, record)

    # table data if needed
    headers = ['Deckname', 'Chance of winning 10 rounds']
    table = []
    for d in deck_data:
        table.append([d['deckname'], "{:.2%}".format(d['binomialwin'])])

    # build a bar chart
    decknames = []
    yvals = []
    for d in deck_data:
        decknames.append(d['deckname'])
        yvals.append(d['binomialwin'] * 100)

    y_pos = np.arange(len(tuple(decknames)))
    plt.barh(y_pos, yvals, align='center', alpha=0.5)
    plt.yticks(y_pos, tuple(decknames))
    plt.xlabel('Percentage')
    plt.title('Binomial wins')
    plt.show()

    with open(outfolder + 'binomialoutput.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in table:
            csvwriter.writerow(row)


binomial_analysis()
