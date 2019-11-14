import csv

months = []
revenue = []

with open('budget_data.csv', 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for column in csvread:
        months.append(column[0])
        revenue.append(int(column[1]))
 
total_revenue = 0
g_inc = revenue[0]
g_dec = revenue[0]
num_months = len(months)

for rev in range(len(revenue)):

    if revenue[rev] >= g_inc:
        g_inc = revenue[rev]
        g_inc_month = months[rev]

    elif revenue[rev] <= g_dec:
        g_dec = revenue[rev]
        g_dec_month = months[rev]
    total_revenue += revenue[rev]

avg_change = round(total_revenue/num_months, 2)

results = ("Financial Analysis\n"
          " \n"
          'Number of months: ' + str(num_months) + '\n'
          'Total Revenue: $' + str(total_revenue) + '\n'
          'Average Change: $' + str(avg_change) + '\n'
          'Greatest Increase in Revenue: ' + g_inc_month + ' ($' + str(g_inc) + ')'+ '\n'
          'Greatest Decrease in Revenue: ' + g_dec_month + ' ($' + str(g_dec) + ')'+ '\n')
print(results)


with open('financial_analysis.txt', 'w') as outfile:
    outfile.write(results)
