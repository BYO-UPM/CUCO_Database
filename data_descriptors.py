import pandas as pd
import numpy as np


##### DEMOGRAPHIC DATA #####

# read demographic data
dm = pd.read_csv('data/metadata/demographic.csv')

# Make all texts of all columns lowercase
dm = dm.apply(lambda x: x.astype(str).str.lower())

# Merge "COMMENT" and "COMMENT.1" columns
dm['COMMENT'] = dm['COMMENT'] + dm['COMMENT.1']

# Remove "COMMENT.1" column
dm = dm.drop('COMMENT.1', axis=1)

# Subtitute all "nan" strings with np.nan, check also "nat" and "na"
dm = dm.replace('nan', np.nan)
dm = dm.replace('nat', np.nan)
dm = dm.replace('na', np.nan)
dm = dm.replace("nannan", np.nan)

# Remove columns with full nan
dm = dm.dropna(axis=1, how='all')

# Total number of patients
total_patients = dm.shape[0]

# Make AGE column to dtype int64
dm['AGE'] = dm['AGE'].astype('int64')
# Make SIZE column to dtype int64
dm['SIZE'] = dm['SIZE'].astype('int64')

# Group by "GROUP" and generate a new dataframe with:
# Number of Males in the group
# Number of Females in the group
# Age in mean +- std
# Size in mean +- std
dm_grouped = dm.groupby('GROUP').agg({'GENDER': lambda x: (x.value_counts(), x.nunique()), 'AGE': [np.mean, np.std], 'SIZE': [np.mean, np.std]})
# Round to 2 decimals
dm_grouped = dm_grouped.round(2)

groups = dm['GROUP'].unique()
for group in groups:
    print("Group: {}".format(group))
    # Select all the patients of the group
    patients = dm[dm['GROUP'] == group]
    # Get the number of males
    males = patients[patients["GENDER"]== "male"].shape[0]
    females = patients[patients["GENDER"]== "female"].shape[0]
    print(males)
    print(females)
    # Get % of missing data of all the other columns
    missing_data = patients.isnull().sum() / patients.shape[0]
    # Print the information
    print(missing_data)


# sTORE DEMOGRAPHIC DATA
dm.to_csv('data/metadata/demographic.csv', index=False)







