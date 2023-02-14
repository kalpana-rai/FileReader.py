import csv

def getneighborhoods():
    nghbrhds = {}                                                   # empty dict
    with open('Neighborhood.csv', newline="") as csv_file:           # open csv file for reading
        csv_reader = csv.reader(csv_file, delimiter=',')            # create a variable for CSV reader object
        for row in csv_reader:
            nghbrhds[row[0]] = row[1]
    return nghbrhds


def getpricelistperneighborhood(neighborhood):
    prices = []
    rowcount = 0
    with open('Transaction.csv', mode="r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")          # creating dict
        for row in csv_reader:
            if (rowcount != 0) and (row['Neighborhood'] == neighborhood):
                prices.append(int(row['SalePrice']))
            rowcount += 1
    return prices


def getavgsalesprice_perneighborhood():
    neighbrs = getneighborhoods()
    dicto = {}
    for key, value in neighbrs.items():
        listo = getpricelistperneighborhood(key)        # calling this function and assigning data to listo variable
        if len(listo) != 0:
            dicto[key] = sum(listo)/len(listo)  # neighborhood as key, average salesprice as value
    return dicto




