# Parse the data into a better CSV for type, sales, date, and region

import pandas as pd

daily0 = pd.read_csv('data\daily_sales_data_0.csv')
daily1 = pd.read_csv('data\daily_sales_data_1.csv')
daily2 = pd.read_csv('data\daily_sales_data_2.csv')

# merge together csvs
concatenatedData = pd.concat([daily0, daily1, daily2])
df = pd.DataFrame(concatenatedData)

# get only pink morsels
pinkMorsel = df.loc[df['product'] == 'pink morsel']

dates = []
sales = []
regions = []

# get values needed from each entry and append to arrays
for entry in pinkMorsel.values:
    price = float(entry[1][1:])  # $3.00 -> 3.00
    quantity = entry[2]
    date = entry[3]
    region = entry[4]
    value = price * quantity
    dates.append(date)
    sales.append(value)
    regions.append(region)

# create objects to store array values
d = {'date': dates, 'sales': sales, 'region': regions}
filteredDf = pd.DataFrame(data=d)
# turn into CSV
filteredDf.to_csv('formattedDataset.csv', index=False)
