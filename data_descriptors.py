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


##### CLINICAL DATA #####
cdpre = pd.read_csv('data/clinical/clinical_2wbs.csv')
cdpost = pd.read_csv('data/clinical/clinical_2was.csv')
cdpost3 = pd.read_csv('data/clinical/clinical_3mas.csv')

# # Rename column "YES" to "S"
# cdpre = cdpre.rename(columns={'YES': 'S'})
# cdpost = cdpost.rename(columns={'YES': 'S'})
# cdpost3 = cdpost3.rename(columns={'YES': 'S'})

# # Save to csv
# cdpre.to_csv('data/clinical/clinical_2wbs.csv', index=False)
# cdpost.to_csv('data/clinical/clinical_2was.csv', index=False)
# cdpost3.to_csv('data/clinical/clinical_3mas.csv', index=False)


# For each dataframe:
# 1. Group by GROUP column
# 2. Aggregate by mean and std for columns 3, 4 and 5
# 3. Round to 2 decimals

# PRE
cdpre_grouped = cdpre.groupby('GROUP').agg({'WEIGHT': [np.mean, np.std], 'NASALITY TEST': [np.mean, np.std], 'NASOMETRY': [np.mean, np.std]})
cdpre_grouped = cdpre_grouped.round(2)

# POST
cdpost_grouped = cdpost.groupby('GROUP').agg({'WEIGHT2': [np.mean, np.std], 'NASALITY TEST2': [np.mean, np.std], 'NASOMETRY2': [np.mean, np.std]})
cdpost_grouped = cdpost_grouped.round(2)

# POST3
cdpost3_grouped = cdpost3.groupby('GROUP').agg({'WEIGHT3': [np.mean, np.std], 'NASALITY TEST3': [np.mean, np.std], 'NASOMETRY3': [np.mean, np.std]})
cdpost3_grouped = cdpost3_grouped.round(2)

# Do the same for G R A B S columns
# PRE
cdpre_grabs_grouped = cdpre.groupby('GROUP').agg({'G': [np.mean, np.std], 'R': [np.mean, np.std], 'A': [np.mean, np.std], 'B': [np.mean, np.std], 'S': [np.mean, np.std]})
cdpre_grabs_grouped = cdpre_grabs_grouped.round(2)

# POST
cdpost_grabs_grouped = cdpost.groupby('GROUP').agg({'G': [np.mean, np.std], 'R': [np.mean, np.std], 'A': [np.mean, np.std], 'B': [np.mean, np.std], 'S': [np.mean, np.std]})
cdpost_grabs_grouped = cdpost_grabs_grouped.round(2)

# POST3
cdpost3_grabs_grouped = cdpost3.groupby('GROUP').agg({'G': [np.mean, np.std], 'R': [np.mean, np.std], 'A': [np.mean, np.std], 'B': [np.mean, np.std], 'S': [np.mean, np.std]})
cdpost3_grabs_grouped = cdpost3_grabs_grouped.round(2)


audio_columns = ['ID','a', 'e', 'i', 'o', 'u', 'agua', 'brasero',
       'dia', 'mesa', 'speech', 'un', 'a1', 'a2', 'a3']

# Concat all pds
cd = pd.concat([cdpre.loc[:, audio_columns], cdpost.loc[:, audio_columns], cdpost3.loc[:, audio_columns]], axis=0)
# total audios available
total_audios = cd.shape[0]*(cd.shape[1]-1) - cd.isnull().sum().sum()

# Percentage of missing data
missing_data = cd.isnull().sum().sum() / (cd.shape[0] * cd.shape[1])

# Group by ID and count the number of audios per patient (exclude the NaNs)
cd_grouped = cd.groupby('ID').count().dropna(axis=1, how='all')
# Get the mean and std of the number of audios per patient (exclude the NaNs)
cd_grouped = cd_grouped.agg({col: [np.mean, np.std] for col in cd_grouped.columns})

# Get percetage of audio missing per material
cd_missing = cd.isnull().sum() / cd.shape[0]


# ============================== Explain karma algorithm and what are we doing here ==============================
# Read the .mat file extracted by karma at data/audios/control/a/1/control_ses1_a_0012.mat
import scipy.io as sio
mat_contents = sio.loadmat('data/audios/control/a/1/control_ses1_a_0012.mat')



