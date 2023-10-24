import pandas as pd

# ARguments
translate = False

# Read data which is in a xlsx
rawdata = pd.read_excel('data/metadata/BBDDCUCO_Separados_Ene2017_kaldi_analisis_2.xlsx', sheet_name=None)

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
list_of_columns = ['edad', 'Genero', 'Talla', 'Fecha exploracion', 'Diagnostico', 'Grupo', 'Fumador', 'SAOS', 'CPAP', 'Vprofesional', 'Grado amigdalar', 'Fecha cirugía', 'COMENTARIO']
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
    df_demographic['Gender'] = df_demographic['Gender'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

    df_demographic['Diagnosis'] = df_demographic['Diagnosis'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)


# Add tc senos column
df_demographic['CT sinuses (lund-Mackay)'] = df["TC SENOS (LUND-MACKAY)"]

# Describe the data:
# How many patients are there?
# How many categorical and numerical variables are there?
# How many missing values are there?
# How many patients are there for each diagnosis?


# ================== Clinical data: first attendance (2 weeks before surgery) ==================
# Generate a sub dataframe with the clinical data [ 'Fecha exploracion', 'Peso', 'GRABS.1', 'Test Nasalidad', 'Nasometria", 'OTROS' ]
listofc = ['Group', 'Fecha exploracion', 'Peso', 'GRABS.1', 'Test nasalidad', 'Nasometria', 'OTROS']
#Make upper
listofc = [x.upper() for x in listofc]
df_c1 = df[listofc]

# For control people fill up GRABS.1 with five 00000
df_c1.loc[df_c1['GROUP'] == 'Control', 'GRABS.1'] = '00000'

# Make GRABS.1 to str
df_c1['GRABS.1'] = df_c1['GRABS.1'].astype(str)

# Split grabs.1 into G R A B S
df_c1['G'] = df_c1['GRABS.1'].str[0]
df_c1['R'] = df_c1['GRABS.1'].str[1]
df_c1['A'] = df_c1['GRABS.1'].str[2]
df_c1['B'] = df_c1['GRABS.1'].str[3]
df_c1['S'] = df_c1['GRABS.1'].str[4]

# Remove GRABS.1
df_c1 = df_c1.drop(['GRABS.1'], axis=1)


if translate:
    from googletrans import Translator

    translator = Translator()
    column_names = list(df_c1.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_c1.columns = column_names

    # Translater Gender and Diagnosis to english
    df_c1['OTROS'] = df_demographic['OTROS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

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

    # Translater Gender and Diagnosis to english
    df_c2['OTROS'] = df_demographic['OTROS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text)

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
    column_names = list(df_c2.columns)
    column_names = translator.translate(column_names, src='es', dest='en')
    column_names = [i.text for i in column_names]
    df_c2.columns = column_names

    # Translater Gender and Diagnosis to english
    df_c2['OTROS'] = df_demographic['OTROS'].apply(translator.translate, src='es', dest='en').apply(lambda x: x.text) 

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


# ================== STORE DATAFRAMES ==================
# Store the dataframes
df_demographic.to_csv('data/metadata/demographic.csv')
df_c1.to_csv('data/metadata/clinical_2wbs.csv')
df_c2.to_csv('data/metadata/clinical_2was.csv')
df_c3.to_csv('data/metadata/clinical_3mas.csv')
df_random.to_csv('data/metadata/audio_comments.csv')

