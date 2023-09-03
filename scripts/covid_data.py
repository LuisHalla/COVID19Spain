from libs import *

# Covid19 data +60 years olds from 2020-01-01 to 2023-05-05
df = pd.read_csv("../data/covid.csv")

# Rename columns
df.rename(columns = {'provincia_iso': 'code',
                     'sexo': 'sex',
                     'grupo_edad': 'age',
                     'fecha': 'date',
                     'num_casos': 'positive',
                     'num_hosp': 'hosp',
                     'num_uci': 'icu',
                     'num_def': 'death'},
          inplace = True)

# Indexing on date and converting to datetime format Y-m-d 
df.set_index(pd.to_datetime(df.date, format='%Y-%m-%d'), inplace=True)

# Dropping date column
df.drop(columns='date', inplace=True)

# Export data
df.to_csv('../data/covid_clean.csv')
