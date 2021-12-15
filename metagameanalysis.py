import csv
from stattools import binomial_distribution, geometric_distribution
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


def export_to_csv(filename, table):
    """Export data that is in table form to csv"""
    with open(outfolder + filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in table:
            csvwriter.writerow(row)


def binomialcalculation(deck, rounds, record):
    winrate = deck['winrate']
    bd = binomial_distribution()
    winning = bd.pmf(record, rounds, winrate)
    return winning


def binomial_analysis(deck_data, rounds, record):
    # calculate percentage of winning
    for d in deck_data:
        d['binomialwin'] = binomialcalculation(d, rounds, record)

    # table data if needed
    headers = ['Deckname', 'Chance of winning 10 rounds']
    table = []
    for d in deck_data:
        table.append([d['deckname'], "{:.2%}".format(d['binomialwin'])])

    # build a bar chart
    # decknames = []
    # yvals = []
    # for d in deck_data:
    #     decknames.append(d['deckname'])
    #     yvals.append(d['binomialwin'] * 100)
    #
    # y_pos = np.arange(len(tuple(decknames)))
    # plt.barh(y_pos, yvals, align='center', alpha=0.5)
    # plt.yticks(y_pos, tuple(decknames))
    # plt.xlabel('Percentage')
    # plt.title('Binomial wins')
    # plt.show()

    export_to_csv('binomialoutput.csv', table)


def geometric_analysis(deck_data, rnd):
    gd = geometric_distribution()
    so = 'success on ' + str(rnd)
    soob = 'success on or before ' + str(rnd)
    sb = 'success before ' + str(rnd)
    sooa = 'success on or after ' + str(rnd)
    sa = 'success after ' + str(rnd)

    for d in deck_data:
        wr = d['winrate']
        d[so] = gd.pmf(rnd, wr)
        d[soob] = gd.success_onorbefore(rnd, wr)
        d[sb] = gd.success_before(rnd, wr)
        d[sooa] = gd.success_onorafter(rnd, wr)
        d[sa] = gd.success_after(rnd, wr)

    headers = ['Deckname', 'winrate', so, soob, sb, sooa, sa]
    table = []
    for d in deck_data:
        table.append([d['deckname'], "{:.2%}".format(d['winrate']), "{:.2%}".format(d[so]),
                      "{:.2%}".format(d[soob]), "{:.2%}".format(
                          d[sb]), "{:.2%}".format(d[sooa]),
                      "{:.2%}".format(d[sa])])

    export_to_csv('geometricoutput.csv', table)


