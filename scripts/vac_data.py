from libs import *

# Vaccination data 2020-12-28 to 2023-05-08
vac = pd.read_csv("../data/vac.csv")

# Filter Spain, 60+ years old and columns of interest
country_filter = (vac.ReportingCountry=='ES')
age_filter = ((vac.TargetGroup=='Age60_69') | (vac.TargetGroup=='Age70_79') | (vac.TargetGroup=='Age80+'))
vac = vac.loc[country_filter & age_filter][['YearWeekISO', 'FirstDose', 'SecondDose', 'TargetGroup', 'Denominator']]
    
# Change YearWeekISO to Y-m-d
date_Ymd = []

for i, date in enumerate(vac.YearWeekISO):
    date_Ymd.append(datetime.datetime.strptime(date + '-1', "%G-W%V-%u").date())
    
vac['date'] = date_Ymd

# Rename colums and ages to better match those of df
vac.rename(columns = {'TargetGroup': 'age', 'FirstDose': 'dose1' , 'SecondDose': 'dose2'}, inplace=True)
vac['age'].replace({'Age60_69': '60-69', 'Age70_79': '70-79', 'Age80+': '80+'}, inplace=True)

# Save denominators of 60+ years old
denominators = {}

for age in vac.age.unique():
    denominators[age] = vac[(vac.age==age)].Denominator.unique()[0]

# Order by date
vac = vac.sort_values('date')

# Group by date and age (for the same age group, there are multiple entries in the same week, and there shouldn't)
vac = vac.groupby(['date', 'age'], as_index=False).sum()

# Index on date
vac.set_index(vac.date, inplace=True)

# Select columns of interest
vac = vac[['age', 'dose1', 'dose2']]

# Export data
vac.to_csv('../data/vac_clean.csv')
