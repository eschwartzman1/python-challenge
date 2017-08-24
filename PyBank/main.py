# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
import collections
csvpath = os.path.join('budget_data_1.csv')

# Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # next(csvfile)
    # print collections.counter(line.rstrip().rpartition('    ')[-1])

   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skips the header
    next(csvreader)

    total_months = []
    total_revenue = []
    average_change = []
    greatest_increase = []
    greatest_decrease = []

    month_count = collections.Counter()
    for Date, total_months in csvreader
        month_count.update([Date])
        total_months.append(float(total_months))

    total = sum(total_months)

    revenue_total = collections.Counter()
    for Revenue, total_revenue in csvreader
        revenue_total.update([Revenue])
        total_revenue.append(float(total_revenue))

    total = sum(total_revenue)
  
  
  
  
  
  
  
  
  
   #  Each row is read as a row
    # for row in csvreader:
        # print(row)
        # print(row[0])











    # new_csv = os.path.join('solved.csv')
    #     with open(new_csv, 'w') as new_csv:
    #         csvwriter = csv.writer(new_csv)
    #         # Define column headers
    #         columns = ["Total Months", "Total Revenue", "Average Revenue Change", "Greatest Increase in Revenue", "Greatest Decrease in Revenue"]
    #         # Define CSV dictionary writer. fieldnames refers to the list of column headers
    #         writer = csv.DictWriter(bank_data, delimiter=',', fieldnames=columns)
    #         # Write the column headers
    #         writer.writeheader()

    #         # Enumerate adds a counter to an iterable
    #         for i, row in enumerate(csvreader):
    #             if i != 1:
    #                 row.append()

    