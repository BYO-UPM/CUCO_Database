# Script to modify the names of the audio files in the data_final/audios folder to match the codificatino followed in the paper.


# Read clinical data
import pandas as pd
import re
import os

cdpre = pd.read_csv('data/data_final/clinical/clinical_2wbs.csv')
cdpost = pd.read_csv('data/data_final/clinical/clinical_2was.csv')
cdpost3 = pd.read_csv('data/data_final/clinical/clinical_3mas.csv')

# From colum 14 to the end there are the paths
cdpre_paths = cdpre.iloc[:, 14:]
cdpost_paths = cdpost.iloc[:, 13:]
cdpost3_paths = cdpost3.iloc[:, 13:]


# For each path in the dataframe, rename the file to match the paper description:
# 1. "control" to "Contr"
# 2. "Cens" to "FESS"
# 3. "Septo" to "Sept"
# 4. "Amig" to "Tonsill"


# For each path in the dataframe, rename the file to match the paper description:

# PRE
for i in range(cdpre_paths.shape[1]):
    for j in range(cdpre_paths.shape[0]):
        # Get the old path
        old_path = cdpre_paths.iloc[j, i]
        # IF nan continue
        if pd.isnull(old_path):
            continue
        # Get the new path
        new_path = re.sub('control', 'Contr', old_path)
        new_path = re.sub('Cens', 'FESS', new_path)
        new_path = re.sub('cens', 'FESS', new_path)
        new_path = re.sub('fess', 'FESS', new_path)
        new_path = re.sub('septo', 'Sept', new_path)
        new_path = re.sub('sept', 'Sept', new_path)
        new_path = re.sub('Amig', 'Tonsill', new_path)
        new_path = re.sub('amig', 'Tonsill', new_path)
        new_path = re.sub('tonsill', 'Tonsill', new_path)
        # Substitute "data" for "data/data_final"
        new_path = re.sub('data/audios', './data/data_final/audios', new_path)

        # Check if the path exists
        if not os.path.exists(new_path):
            print('Path does not exist: {}'.format(new_path))
            continue
        # Rename the file
        cdpre_paths.iloc[j, i] = new_path

# Subtitue the paths in the dataframe original
cdpre.iloc[:, 14:] = cdpre_paths

# POST
for i in range(cdpost_paths.shape[1]):
    for j in range(cdpost_paths.shape[0]):
        # Get the old path
        old_path = cdpost_paths.iloc[j, i]
        # IF nan continue
        if pd.isnull(old_path):
            continue
        # Get the new path
        new_path = re.sub('control', 'Contr', old_path)
        new_path = re.sub('Cens', 'FESS', new_path)
        new_path = re.sub('cens', 'FESS', new_path)
        new_path = re.sub('fess', 'FESS', new_path)
        new_path = re.sub('septo', 'Sept', new_path)
        new_path = re.sub('sept', 'Sept', new_path)
        new_path = re.sub('Amig', 'Tonsill', new_path)
        new_path = re.sub('amig', 'Tonsill', new_path)
        new_path = re.sub('tonsill', 'Tonsill', new_path)
        # Substitute "data" for "data/data_final"
        new_path = re.sub('data/audios', './data/data_final/audios', new_path)

        # Check if the path exists
        if not os.path.exists(new_path):
            print('Path does not exist: {}'.format(new_path))
            continue
        # Rename the file
        cdpost_paths.iloc[j, i] = new_path

# Subtitue the paths in the dataframe original
cdpost.iloc[:, 13:] = cdpost_paths

# POST3
for i in range(cdpost3_paths.shape[1]):
    for j in range(cdpost3_paths.shape[0]):
        # Get the old path
        old_path = cdpost3_paths.iloc[j, i]
        # IF nan continue
        if pd.isnull(old_path):
            continue
        # Get the new path
        new_path = re.sub('control', 'Contr', old_path)
        new_path = re.sub('Cens', 'FESS', new_path)
        new_path = re.sub('cens', 'FESS', new_path)
        new_path = re.sub('fess', 'FESS', new_path)
        new_path = re.sub('septo', 'Sept', new_path)
        new_path = re.sub('sept', 'Sept', new_path)
        new_path = re.sub('Amig', 'Tonsill', new_path)
        new_path = re.sub('amig', 'Tonsill', new_path)
        new_path = re.sub('tonsill', 'Tonsill', new_path)
        # Substitute "data" for "data/data_final"
        new_path = re.sub('data/audios', './data/data_final/audios', new_path)

        # Check if the path exists
        if not os.path.exists(new_path):
            print('Path does not exist: {}'.format(new_path))
            continue
        # Rename the file
        cdpost3_paths.iloc[j, i] = new_path

# Subtitue the paths in the dataframe original
cdpost3.iloc[:, 13:] = cdpost3_paths


# Substitute: "Septoplasty" for "Sept", "Amig" for "Tonsill", control for Contr
cdpre['GROUP'] = cdpre['GROUP'].str.replace('septoplasty', 'Sept')
cdpre['GROUP'] = cdpre['GROUP'].str.replace('tonsillectomy', 'Tonsill')
cdpre['GROUP'] = cdpre['GROUP'].str.replace('control', 'Contr')
cdpre['GROUP'] = cdpre['GROUP'].str.replace('fess', 'FESS')

cdpost['GROUP'] = cdpost['GROUP'].str.replace('septoplasty', 'Sept')
cdpost['GROUP'] = cdpost['GROUP'].str.replace('tonsillectomy', 'Tonsill')
cdpost['GROUP'] = cdpost['GROUP'].str.replace('control', 'Contr')
cdpost['GROUP'] = cdpost['GROUP'].str.replace('fess', 'FESS')

cdpost3['GROUP'] = cdpost3['GROUP'].str.replace('septoplasty', 'Sept')
cdpost3['GROUP'] = cdpost3['GROUP'].str.replace('tonsillectomy', 'Tonsill')
cdpost3['GROUP'] = cdpost3['GROUP'].str.replace('control', 'Contr')
cdpost3['GROUP'] = cdpost3['GROUP'].str.replace('fess', 'FESS')

# Store csv
cdpre.to_csv('data/data_final/clinical/clinical_2wbs.csv', index=False)
cdpost.to_csv('data/data_final/clinical/clinical_2was.csv', index=False)
cdpost3.to_csv('data/data_final/clinical/clinical_3mas.csv', index=False)



# read Audio features and rename groups to match the paper description
import pandas as pd
import re

# Read the csv
afpre = pd.read_csv('data/data_final/audio_features/audiofeatures_2wbs.csv')
afpost = pd.read_csv('data/data_final/audio_features/audiofeatures_2was.csv')
afpost3 = pd.read_csv('data/data_final/audio_features/audiofeatures_3mas.csv')

# Substitute: "Septoplasty" for "Sept", "Amig" for "Tonsill", control for Contr
afpre['GROUP'] = afpre['GROUP'].str.replace('Septoplasty', 'Sept')
afpre['GROUP'] = afpre['GROUP'].str.replace('Amig', 'Tonsill')
afpre['GROUP'] = afpre['GROUP'].str.replace('control', 'Contr')

afpost['GROUP'] = afpost['GROUP'].str.replace('Septoplasty', 'Sept')
afpost['GROUP'] = afpost['GROUP'].str.replace('Amig', 'Tonsill')
afpost['GROUP'] = afpost['GROUP'].str.replace('control', 'Contr')

afpost3['GROUP'] = afpost3['GROUP'].str.replace('Septoplasty', 'Sept')
afpost3['GROUP'] = afpost3['GROUP'].str.replace('Amig', 'Tonsill')
afpost3['GROUP'] = afpost3['GROUP'].str.replace('control', 'Contr')

# Store csv
afpre.to_csv('data/data_final/audio_features/audiofeatures_2wbs.csv', index=False)
afpost.to_csv('data/data_final/audio_features/audiofeatures_2was.csv', index=False)
afpost3.to_csv('data/data_final/audio_features/audiofeatures_3mas.csv', index=False)


# Do the same for metadata/demographic
import pandas as pd

# Read the csv
dm = pd.read_csv('data/data_final/metadata/demographic.csv')

# Substitute: "Septoplasty" for "Sept", "Amig" for "Tonsill", control for Contr
dm['GROUP'] = dm['GROUP'].str.replace('septoplasty', 'Sept')
dm['GROUP'] = dm['GROUP'].str.replace('tonsillectomy', 'Tonsill')
dm['GROUP'] = dm['GROUP'].str.replace('control', 'Contr')
dm['GROUP'] = dm['GROUP'].str.replace('fess', 'FESS')

# Store csv
dm.to_csv('data/data_final/metadata/demographic.csv', index=False)


