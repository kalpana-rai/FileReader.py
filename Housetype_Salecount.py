import csv                                                   #Arbeiten mit Datein : csv Module

def getmssubclasses():
    mssubclass = {}                                         # leer Dict.
    with open('MSSubClass.csv', newline="") as csv_file:    # csv Modul benötigt den Parameter 'newline = ""'
        csv_reader = csv.reader(csv_file, delimiter=',')    # delimiter ist das Trennzeichen
        rowcount = 0
        for row in csv_reader:                              # csv_reader ist ein "iterator"
            if rowcount != 0:
                mssubclass[row[0]] = row[1]
            rowcount += 1
    return mssubclass                                       # rückgabewerte als dict


def gettransactionsper_mssubclass(mssubclassid):            # passing (mssubclassid) to get the count of similar id
    count = 0
    rowcount = 0
    with open('Transaction.csv', mode="r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            if (rowcount != 0) and (int(mssubclassid) == int(row['MSSubClass'])):
                count += 1
            rowcount += 1
    return count


def getsales_perhousetype():
    mssubclass = getmssubclasses()
    dictn = {}
    for mssubclassid, desc in mssubclass.items():
        dictn[desc] = gettransactionsper_mssubclass(mssubclassid) #
    return dictn
