
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# reading file
data =pd.read_csv("BTC-USD.csv")

# adj close datas array, we will update the values
data_for_years = [0,1,2,3,4,5,6,7]

# years numpy array
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

# we will use it to keep the months of the year together
count = 12

for i in range(len(years)):
    if i != len(years)-1:
     data_for_years[i] = np.mean(data["Adj Close"][(count-12):count])
     count = count + 12
    else:  # we use else because for the last year, last year may not have 12 months.
     data_for_years[i] = np.mean(data["Adj Close"][(count - 12):])

plt.xlabel("Years")
plt.ylabel("Adj Close")
plt.plot(years, data_for_years)
plt.title("Mean Adjusted Close Values of BTC")
plt.show()





