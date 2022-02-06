import datetime
class Record:
    issuance_date = datetime
    clean_bid = -1
    clean_ask = -1
    last_price = -1

def remove_prefix(str, prefix):
    return str[str.startswith(prefix) and len(prefix):]


import csv
from xxlimited import Str
import matplotlib.pyplot as plt

with open('sample-input.csv', 'r') as csvfile:
    data_reader = csv.reader(csvfile)

    record_array = []
    i = 0
    rec = Record()
    for row in data_reader:
 
        for j in range(len(row)):
            if row[j].startswith('DIs'):
                issuance_date_str = remove_prefix(row[j], 'DIs')
                rec.issuance_date = datetime.datetime.strptime(issuance_date_str, '%Y%m%d').date()
            elif row[j].startswith('BPr'):
                rec.clean_bid = remove_prefix(row[j], 'BPr')
            elif row[j].startswith('APl'):
                rec.clean_ask = remove_prefix(row[j], 'APl')
            elif row[j].startswith('Pl'):
                rec.last_price = remove_prefix(row[j], 'Pl')

        i+=1
        if (i%10) == 0:
            record_array.append(rec)
            del rec
            rec = Record()

for record in record_array:
    print(record.issuance_date)
    print(record.clean_bid)
    print(record.clean_ask)
    print(record.last_price)
    plt.scatter(record.issuance_date, record.clean_bid, c="blue", edgecolor="black", linewidths=1, marker = "o", alpha = 0.8, label = "Clean Bid")
    plt.scatter(record.issuance_date, record.clean_ask, c="red", edgecolor="black", linewidths=1, marker = "o", alpha = 0.8, label="Clean Ask")
    plt.scatter(record.issuance_date, record.last_price, c="grey", edgecolor="black", linewidths=1, marker = "o", alpha = 0.8, label="Last Price")

plt.grid()
plt.legend()
plt.show()