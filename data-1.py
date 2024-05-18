import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
import pandas as pd 
import random
import math
import time
import datetime
import itertools
from scipy.optimize import curve_fit
from numpy import exp, linspace, random
deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
deaths_df.to_csv("data_1.csv")
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
confirmed_df.to_csv("data_2.csv")
recoveries_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
recoveries_df.to_csv("data_3.csv")
print(deaths_df.shape)
print(deaths_df.describe())
print(confirmed_df.head())
italy_cases = []
for i in dates:
    confirmed_sum = confirmed[i].sum()
    death_sum = deaths[i].sum()
    recovered_sum = recoveries[i].sum()
plt.figure(figsize=(16, 9))
plt.plot(adjusted_dates, italy_cases)
plt.title('italy # of Coronavirus Cases Over Time', size=20)
plt.xlabel('Days Since 1/21/2020', size=20)
plt.ylabel('# of Cases', size=20)
plt.xticks(size=20)
plt.yticks(size=20)
plt.show()

