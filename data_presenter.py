import csv
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

open_file = open("CupcakeInvoices.csv")
# for line in open_file:
#     print(line)


myCsv = csv.reader(open_file)
# for line in myCsv:
#     print(line[2])
# open_file.seek(0,0)

# for line in myCsv:
#     quant = int(line[3])
#     price = float(line[4])
#     ans = quant*price
#     format_ans = "{:.2f}".format(ans)
#     print(f'Total for {line[0]} is {format_ans}')


# open_file.seek(0,0)
# ans = 0
# for line in myCsv:
#     quant = float(line[3])
#     price = float(line[4])
#     ans += quant*price

# format_ans = "{:.2f}".format(ans)
# print(format_ans)


# open_file.close()

A = 0
B = 0
C = 0

for line in myCsv:
    if line[2] == "Chocolate":
        chocTotal = int(line[3]) * float(line[4])
        A += chocTotal
    if line[2] == "Vanilla":
        vanTotal = int(line[3]) * float(line[4])
        B += vanTotal
    if line[2] == "Strawberry":
        strawTotal = int(line[3]) * float(line[4])
        C += strawTotal

# BAR GARPH
x = np.array(["Chocolate", "Vanilla", "Strawberry"])
y = np.array([A, B, C])
# plt.bar(x, y)
# plt.show()

# PIE CHART
labels = ["Chocolate", "Vanilla", "Strawberry"]
plt.pie(y, labels = labels)
plt.show()