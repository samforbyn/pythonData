import csv
from decimal import Decimal

# 1
open_file = open("CupcakeInvoices.csv")
# for line in open_file:
#     print(line)

# 2
myCsv = csv.reader(open_file)
# for line in myCsv:
#     # name1, name2, type, quantity, price = line
#     print(line[2])

#3
# for line in myCsv:
#     quant = float(line[3])
#     price = float(line[4])
#     ans = quant*price
#     format_ans = "{:.2f}".format(ans)
#     print(f'Total for {line[0]} is {format_ans}')

#4
ans = 0
for line in myCsv:
    quant = float(line[3])
    price = float(line[4])
    ans += quant*price
    format_ans = "{:.2f}".format(ans)
print(format_ans)

#5
open_file.close()