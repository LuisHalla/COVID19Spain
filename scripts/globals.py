from libs import *
from vac_data import *

# Data
df = pd.read_csv("../data/covid_clean.csv")
vac = pd.read_csv("../data/vac_clean.csv")


# 14-day-cumulative-incidence per 100.000
ci14 = df.groupby('date').positive.sum().rolling(14).sum() * 1e5 / sum(denominators.values())

# %ICU occupation out of 4404 beds
icu_ocup = df.groupby('date').icu.sum().rolling(14).sum() / 4404 * 100

# Waves
waves = pd.to_datetime(['2020-01-01', '2020-06-26', '2020-12-11', '2021-03-18', '2021-06-25', '2021-10-15', '2023-05-05'])

# Extra waves
wave6_end = pd.to_datetime('2022-04-01')

# Vacs
vac_percent = vac.groupby('date').sum().dose2.cumsum() / sum(denominators.values())*100
vac80 = vac_percent[(vac_percent>80) & (vac_percent<85)].index.values[0]
vac20 = vac_percent[(vac_percent>20) & (vac_percent<25)].index.values[0]
vac_stable = vac_percent.index[53] #2022-01-03
