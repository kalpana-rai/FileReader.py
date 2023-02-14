import csv                                                   #Arbeiten mit Datein : csv Module

def getpricelist_peryear(year):                           # Erstellen einer Preisliste, die einem Jahr entspricht
    prices = []
    rowcount = 0
    with open('Transaction.csv', mode="r", newline="") as csv_file:  #open the csv file in read mode
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            if (rowcount != 0) and (row['YrSold'] == year):      # if condition
                prices.append(int(row['SalePrice']))             # sales price value in der Liste angehängt
            rowcount += 1
    return prices

def getavgsalesprice_peryear():
    years = ['2006', '2007', '2008', '2009', '2010']
    dicto = {}
    for year in years:
        listo = getpricelist_peryear(year)                  # get price list for corresponding year
        if len(listo) != 0:
            dicto[year] = sum(listo)/len(listo)             # creating dictionary with year as key and avg as value
    return dicto





