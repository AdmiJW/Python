import csv
from datetime import datetime

#   Here we will be opening the stocks.csv from the very same directory with this python code
#   Using the csv python module and its method reader, pass in the file and obtain the reader object back
filepath = 'stocks.csv'
mycsv = open(filepath, newline='')
reader = csv.reader(mycsv)

#   Since the first row of the csv is the header, we simply just store it in a variable, and move the cursor to next row
#   Date, Open, High, Low, Close, Volume, Adj Close
header = next(reader)

#   Here we declare a datas Array, which is going to store all of the parsed values from CSV
datas = [header]

#   Process each row one by one, remember that CSV does not specify types (All are strings), so need to do
#   type conversions ourselves
for singlerow in reader:
    #   Parse the date and time from the row, and reformat it using methods from datetime module
    date = datetime.strptime(singlerow[0], '%m/%d/%Y').strftime('%d/%m/%Y')
    open_price = float(singlerow[1])
    high = float(singlerow[2])
    low = float(singlerow[3])
    close = float(singlerow[4])
    volume = int(singlerow[5])
    adj_close = float(singlerow[6])

    #   Now with all information obtained, append it all to the result array
    datas.append([date, open_price, high, low, close, volume, adj_close] )

#   Close the file to prevent memory leaks
mycsv.close()

#   All of the parsed information above, we are going to write it into a new file.
newfile = open('dailyreturns.csv', 'w', newline='')
#   Using the csv module's writer method, we are going to write the Date, and return rate data ONLY
writer = csv.writer(newfile)
#   Write down the header
writer.writerow(['Date','Return'])


for index in range(1, len(datas) - 1):
    date = datas[index][0]
    percent = "{:.2f}%".format( (datas[index][1] - datas[index + 1][1]) / datas[index + 1][1] * 100 )
    writer.writerow( [date, percent] )

newfile.close()
