import pandas as pd

# Read data which is in a xlsx
rawdata = pd.read_excel('data/metadata/BBDDCUCO_Separados_Ene2017_kaldi_analisis_2.xlsx', sheet_name=None)

# Read the first 3 sheets
df1 = rawdata['Amig-Palad']
df2 = rawdata['CENS']
df3 = rawdata['Sept-Turb']

# Concatenate the 3 sheets adding a new column with the name of the sheet
df1['sheet'] = 'Amig-Palad'
df2['sheet'] = 'CENS'
df3['sheet'] = 'Sept-Turb'

# Concatenate the 3 sheets
df = pd.concat([df1, df2, df3])

# Remove completely empty rows and columns
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')

# Remove "Nº Historia" column
df = df.drop(['Nº Historia'], axis=1)

# Removing "PRE/2S/3M" column
df = df.drop(['PRE/2S/3M'], axis=1)


# Set as index the "ID" and "sheet" columns
df = df.set_index(['ID', 'sheet'])


# Generate a sub dataframe with the demographic data []'edad', 'Genero', 'Peso', 'Talla', 'Fecha exploracion', 'Diagnostico', 'Grupo', 'Fumador', 'SAOS', 'CPAP', 'Vprofesional'"]
df_demographic = df[['edad', 'Genero', 'Peso', 'Talla', 'Fecha exploracion', 'Diagnostico', 'Grupo', 'Fumador', 'SAOS', 'CPAP', 'Vprofesional']]

# Translate to english all the columns
