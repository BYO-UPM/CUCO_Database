# First version of the script to clean the metadata and translate it to english. Several modifications were done posteriorly using rename_files.py and rename_paths.py.



import pandas as pd

# ARguments
translate = True

# Read data which is in a xlsx
rawdata = pd.read_excel('data/raw_data/BBDDCUCO_Separados_Ene2017_kaldi_analisis_2.xlsx', sheet_name=None)

# Read the first 3 sheets
df1 = rawdata['Amig-Palad']
df2 = rawdata['CENS']
df3 = rawdata['Sept-Turb']
df4 = rawdata['Control']

# Concatenate the 3 sheets adding a new column with the name of the sheet
df1['Group'] = 'Tonsillectomy'
df2['Group'] = 'FESS'
df3['Group'] = 'Septoplasty'
df4['Group'] = 'Control'

# Concatenate the 3 sheets
df = pd.concat([df1, df2, df3, df4])

# Remove completely empty rows and columns
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')

# Remove "Nº Historia" column
df = df.drop(['Nº Historia'], axis=1)

# Removing "PRE/2S/3M" column
df = df.drop(['PRE/2S/3M'], axis=1)

# Set as index the
df = df.set_index(['ID'])

# Set all columns in capital letters
df.columns = [x.upper() for x in df.columns]


#  ================ Demographic data  =================
# Generate a sub dataframe with the demographic data []'edad', 'Genero', 'Talla', 'Fecha exploracion', 'Diagnostico', 'Grupo', 'Fumador', 'SAOS', 'CPAP', 'Vprofesional'"]
list_of_columns = ['edad', 'Genero', 'Talla', 'Fecha exploracion', 'Diagnostico', 'Group', 'Fumador', 'SAOS', 'CPAP', 'Vprofesional', 'Grado amigdalar', 'Fecha cirugía', 'COMENTARIO']
#Make upper
list_of_columns = [x.upper() for x in list_of_columns]
df_demographic = df[list_of_columns]

if translate:
    # REname all column names to english
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_demographic.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_demographic.columns = column_names

    # Translater Gender and Diagnosis to english
    df_demographic['GENDER'] = df_demographic['GENDER'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

    df_demographic['DIAGNOSIS'] = df_demographic['DIAGNOSIS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)


# Add tc senos column
df_demographic['CT SINUSES (LUND-MACKAY)'] = df["TC SENOS (LUND-MACKAY)"]




# ================== Clinical data: first attendance (2 weeks before surgery) ==================
# Generate a sub dataframe with the clinical data [ 'Fecha exploracion', 'Peso', 'GRABS.1', 'Test Nasalidad', 'Nasometria", 'OTROS' ]
listofc = ['Group', 'Fecha exploracion', 'Peso', 'GRABS', 'Test nasalidad', 'Nasometria', 'OTROS']
#Make upper
listofc = [x.upper() for x in listofc]
df_c1 = df[listofc]

# For control people fill up GRABS.1 with five 00000
df_c1.loc[df_c1['GROUP'] == 'Control', 'GRABS'] = '00000'

# Make GRABS.1 to str
df_c1['GRABS'] = df_c1['GRABS'].astype(str)

# if GRABS.1 is "0" substitute it with "00000"
df_c1.loc[df_c1['GRABS'] == '0', 'GRABS'] = "00000"
df_c1.loc[df_c1['GRABS'] == '0.0', 'GRABS'] = "00000"

# Subtitute nan with -----
df_c1 = df_c1.replace('nan', '-----')

# Split grabs.1 into G R A B S
df_c1['G'] = df_c1['GRABS'].str[0]
df_c1['R'] = df_c1['GRABS'].str[1]
df_c1['A'] = df_c1['GRABS'].str[2]
df_c1['B'] = df_c1['GRABS'].str[3]
df_c1['S'] = df_c1['GRABS'].str[4]

# Remove GRABS.1
df_c1 = df_c1.drop(['GRABS'], axis=1)


if translate:
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_c1.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_c1.columns = column_names

    # The translator miss-translating A and S columns, we modify them manually
    df_c1 = df_c1.rename(columns={'TO': 'A', 'YES': 'S'})

    # Translater Gender and Diagnosis to english
    df_c1['OTROS'] = df_c1['OTHERS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

# New column that says 2 weeks before surgery
df_c1['time'] = '2wbs'
# Make all columns to capital letters
df_c1.columns = [x.upper() for x in df_c1.columns]

# ================== Clinical data: 2 weeks after surgery ==================
# Generate a sub dataframe with the clinical data [ 'Fecha exploracion', 'Peso', 'GRABS.1', 'Test Nasalidad', 'Nasometria", 'OTROS' ]
lc = ['Group', 'Fecha exploracion2', 'Peso2', 'GRABS2', 'Test nasalidad2', 'Nasometria2', 'OTROS2']
#Make upper
lc = [x.upper() for x in lc]
df_c2 = df[lc]

# For control people fill up GRABS.1 with five 00000
df_c2.loc[df_c2['GROUP'] == 'Control', 'GRABS2'] = '00000'

# Make GRABS.1 to str
df_c2['GRABS2'] = df_c2['GRABS2'].astype(str)

# if GRABS.1 is "0" substitute it with "00000"
df_c2.loc[df_c2['GRABS2'] == '0', 'GRABS2'] = "00000"
df_c2.loc[df_c2['GRABS2'] == '0.0', 'GRABS2'] = "00000"

# Subtitute nan with -----
df_c2 = df_c2.replace('nan', '-----')

# Split grabs.1 into G R A B S
df_c2['G'] = df_c2['GRABS2'].str[0]
df_c2['R'] = df_c2['GRABS2'].str[1]
df_c2['A'] = df_c2['GRABS2'].str[2]
df_c2['B'] = df_c2['GRABS2'].str[3]
df_c2['S'] = df_c2['GRABS2'].str[4]

# Remove GRABS.1
df_c2 = df_c2.drop(['GRABS2'], axis=1)

if translate:
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_c2.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_c2.columns = column_names

    # The translator miss-translating A and S columns, we modify them manually
    df_c2 = df_c2.rename(columns={'TO': 'A', 'YES': 'S'})

    # Translater Gender and Diagnosis to english
    df_c2['OTHERS2'] = df_c2['OTHERS2'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

# New column that says 2 weeks after surgery
df_c2['time'] = '2was'
# Make all columns to capital letters
df_c2.columns = [x.upper() for x in df_c2.columns]

# ================== Clinical data: 3 months after surgery ==================
# Generate a sub dataframe with the clinical data [ 'Fecha exploracion', 'Peso', 'GRABS.1', 'Test Nasalidad', 'Nasometria", 'OTROS' ]
lc = ['Group', 'Fecha exploracion3', 'Peso3', 'GRABS3', 'Test nasalidad3', 'Nasometria3', 'OTROS3']
#Make upper
lc = [x.upper() for x in lc]
df_c3 = df[lc]

# For control people fill up GRABS.1 with five 00000
df_c3.loc[df_c3['GROUP'] == 'Control', 'GRABS3'] = '00000'

# Make GRABS.1 to str
df_c3['GRABS3'] = df_c3['GRABS3'].astype(str)

# if GRABS.1 is "0" substitute it with "00000"
df_c3.loc[df_c3['GRABS3'] == '0', 'GRABS3'] = "00000"
df_c3.loc[df_c3['GRABS3'] == '0.0', 'GRABS3'] = "00000"

# Subtitute nan with -----
df_c3 = df_c3.replace('nan', '-----')

# Split grabs.1 into G R A B S
df_c3['G'] = df_c3['GRABS3'].str[0]
df_c3['R'] = df_c3['GRABS3'].str[1]
df_c3['A'] = df_c3['GRABS3'].str[2]
df_c3['B'] = df_c3['GRABS3'].str[3]
df_c3['S'] = df_c3['GRABS3'].str[4]


# Remove GRABS.1
df_c3 = df_c3.drop(['GRABS3'], axis=1)

if translate:
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_c3.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_c3.columns = column_names

    # The translator miss-translating A and S columns, we modify them manually
    df_c3 = df_c3.rename(columns={'TO': 'A', 'YES': 'S'})

    # Translater Gender and Diagnosis to english
    df_c3['OTHERS3'] = df_c3['OTHERS3'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text) 

# New column that says 2 weeks after surgery
df_c3['time'] = '3mas'
# Make all columns to capital letters
df_c3.columns = [x.upper() for x in df_c3.columns]

# ================== Random stuff ==================
# Get all columns that are not in the other dataframes
df_random = df.loc[:, ~df.columns.isin(df_c1.columns)]
df_random = df_random.loc[:, ~df_random.columns.isin(df_c2.columns)]
df_random = df_random.loc[:, ~df_random.columns.isin(df_c3.columns)]
df_random = df_random.loc[:, ~df_random.columns.isin(df_demographic.columns)]

# Remove the first 4 columns and last column
df_random = df_random.iloc[:, 4:-1]


# Add group column
df_random['GROUP'] = df['GROUP']

if translate:
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_random.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_random.columns = column_names

    # Translater Gender and Diagnosis to english
    df_random['DIAGNOSIS'] = df_random['DIAGNOSIS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text) 


# ================== PATHS TO RAW AUDIO DATA ==================
# For each clinical df, lets add the raw audio paths
import numpy as np
# The audio path is constructed as follows:
# /data/audios/{group}/{audio_material}/{clinical_session}/{group}_ses{clinical_session}_{audio_material}_{id}.wav

# The audio material is: a, e, i, o, u, aeiou, agua, brasero, concatenateread, dia, mesa, speech, u, un

# Add a new column for each audio material
audio_materials = ['a', 'e', 'i', 'o', 'u', 'agua', 'brasero', 'dia', 'mesa', 'speech', 'u', 'un']
for audio_material in audio_materials:
    df_c1[audio_material] = np.nan
    df_c2[audio_material] = np.nan
    df_c3[audio_material] = np.nan


# Lets walk the path
import os
from os import walk

not_found_ids = []
for (dirpath, dirnames, filenames) in walk('data/audios'):
    # Skip the data/audios/*/raw/** folders
    if 'raw' in dirpath:
        continue
    for filename in filenames:
        if filename.endswith('.wav'):
            # Get the group
            group = filename.split('_')[0]
            # Subtitute group for the correct group name
            if group == 'Amig':
                group = 'Tonsillectomy'
            elif group == 'Cens':
                group = 'FESS'
            elif group == 'Sept':
                group = 'Septoplasty'
            elif group == 'control':
                group = 'Control'
            # Get the audio material and make it lower
            audio_material = filename.split('_')[2].lower()
            # Get the clinical session
            clinical_session = filename.split('_')[1]
            # Get the id
            id = int(filename.split('_')[3].split('.')[0])
            # Get the path
            path = os.path.join(dirpath, filename)

            # Use clinical session to select the correct dataframe
            if clinical_session == 'ses1':
                df_c = df_c1
            elif clinical_session == 'ses2':
                df_c = df_c2
            elif clinical_session == 'ses3':
                df_c = df_c3

            # Check if id exists in the dataframe
            if id in df_c.index:
                # Add to df_c[audio_material] the path, the id is the index
                df_c.loc[id, audio_material] = path
            else:
                print('id {} not in dataframe'.format(id))
                not_found_ids.append(id)

# Remove duplicates from not_found_ids
not_found_ids = list(set(not_found_ids))

# Check if there exists any audio_material with nan path
incomplete_ids = []
for audio_material in audio_materials:
    if df_c1[audio_material].isnull().values.any():
        print('There are nan values in df_c1[{}]'.format(audio_material))
        incomplete_ids.append(list(df_c1[df_c1[audio_material].isnull()].index))
    if df_c2[audio_material].isnull().values.any():
        print('There are nan values in df_c2[{}]'.format(audio_material))
        incomplete_ids.append(list(df_c2[df_c2[audio_material].isnull()].index))
    if df_c3[audio_material].isnull().values.any():
        print('There are nan values in df_c3[{}]'.format(audio_material))
        incomplete_ids.append(list(df_c3[df_c3[audio_material].isnull()].index))

# Remove duplicates from incomplete_ids
incomplete_ids_c1 = list(set(incomplete_ids[0]))
incomplete_ids_c2 = list(set(incomplete_ids[1]))
incomplete_ids_c3 = list(set(incomplete_ids[2]))

# Print % of incomplete patients for clinical visit
print('Percentage of incomplete patients for clinical visit 1: {}'.format(len(incomplete_ids_c1)/len(df_c1.index)))
print('Percentage of incomplete patients for clinical visit 2: {}'.format(len(incomplete_ids_c2)/len(df_c2.index)))
print('Percentage of incomplete patients for clinical visit 3: {}'.format(len(incomplete_ids_c3)/len(df_c3.index)))


# ================== STORE DATAFRAMES ==================
# Normalise all nan values to np.nan (NaN, "-", "nan", "nannan", "nat", "na")
def replace_nan(df):
    df = df.replace('nan', np.nan)
    df = df.replace('nannan', np.nan)
    df = df.replace('nat', np.nan)
    df = df.replace('na', np.nan)
    df = df.replace('-', np.nan)
    df = df.replace('-', np.nan)
    df = df.replace('', np.nan)
    df = df.replace(' ', np.nan)

    return df

df_demographic = replace_nan(df_demographic)
df_c1 = replace_nan(df_c1)
df_c2 = replace_nan(df_c2)
df_c3 = replace_nan(df_c3)
df_random = replace_nan(df_random)




# Sort all dataframes by id
df_demographic = df_demographic.sort_index()
df_c1 = df_c1.sort_index()
df_c2 = df_c2.sort_index()
df_c3 = df_c3.sort_index()
df_random = df_random.sort_index()

# Make all dataframes lowercase
df_demographic = df_demographic.apply(lambda x: x.astype(str).str.lower())
df_c1 = df_c1.apply(lambda x: x.astype(str).str.lower())
df_c2 = df_c2.apply(lambda x: x.astype(str).str.lower())
df_c3 = df_c3.apply(lambda x: x.astype(str).str.lower())
df_random = df_random.apply(lambda x: x.astype(str).str.lower())

# Store the dataframes
df_demographic.to_csv('data/metadata/demographic.csv')
df_c1.to_csv('data/clinical/clinical_2wbs.csv')
df_c2.to_csv('data/clinical/clinical_2was.csv')
df_c3.to_csv('data/clinical/clinical_3mas.csv')
df_random.to_csv('data/metadata/audio_comments.csv')


