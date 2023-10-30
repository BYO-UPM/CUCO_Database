import pandas as pd
import numpy as np
import os

# ======================== Septoplasty ========================
# Formants
f_septo = pd.read_excel('data/audio_features/Sept_formants.xls', sheet_name=None)
f_septo_a1 = f_septo['a1']
f_septo_a2 = f_septo['a2']
f_septo_a3 = f_septo['a3']
# Merge all dfs into  one
f_septo = pd.concat((f_septo_a1, f_septo_a2, f_septo_a3))

# Remove duracion
f_septo = f_septo.drop(['Duracion'], axis=1)


# Other audio features
o_septo = pd.read_excel('data/audio_features/Sept.xls', sheet_name=None)
o_septo_a1 = o_septo['a1']
o_septo_a2 = o_septo['a2']
o_septo_a3 = o_septo['a3']
# Merge all dfs into  one
o_septo = pd.concat((o_septo_a1, o_septo_a2, o_septo_a3))

# Remove duracion
o_septo = o_septo.drop(['Duracion'], axis=1)

# Merge both on Nombre Archivo
septo = pd.merge(f_septo, o_septo, on='Nombre Archivo')

# Nombre Archivo is defined as: {group}_{session}_{audio_material}_{id}.wav
# Split Nombre Archivo into columns
septo['group'] = septo['Nombre Archivo'].str.split('_').str[0]
septo['session'] = septo['Nombre Archivo'].str.split('_').str[1]
septo['audio_material'] = septo['Nombre Archivo'].str.split('_').str[2]
septo['id'] = septo['Nombre Archivo'].str.split('_').str[3].str.split('.').str[0]

# Rename group values: Sept -> Septoplasty
septo['group'] = septo['group'].replace('Sept', 'Septoplasty')

# Make ID the index and make sure its integer
septo = septo.set_index('id')
septo.index = septo.index.astype(int)

# Substitute ses1 to 2wbs, ses2 to 2was, ses3 to 3mas
septo['session'] = septo['session'].replace('ses1', '2wbs')
septo['session'] = septo['session'].replace('ses2', '2was')
septo['session'] = septo['session'].replace('ses3', '3mas')

# Remove nombre archivo column
septo = septo.drop(['Nombre Archivo'], axis=1)

# Sort by index
septo = septo.sort_index()

# Make all column names to uppercase
septo.columns = septo.columns.str.upper()

# Split into 3 dfs by session
septo_2wbs = septo[septo['SESSION'] == '2wbs']
septo_2was = septo[septo['SESSION'] == '2was']
septo_3mas = septo[septo['SESSION'] == '3mas']

# Remove session column
septo_2wbs = septo_2wbs.drop(['SESSION'], axis=1)
septo_2was = septo_2was.drop(['SESSION'], axis=1)
septo_3mas = septo_3mas.drop(['SESSION'], axis=1)

# ======================== Control ========================
# Formants
f_control = pd.read_excel('data/audio_features/Control_formants.xls', sheet_name=None)
f_control_a1 = f_control['a1']
f_control_a2 = f_control['a2']
f_control_a3 = f_control['a3']
# Merge all dfs into  one
f_control = pd.concat((f_control_a1, f_control_a2, f_control_a3))

# Remove duracion
f_control = f_control.drop(['Duracion'], axis=1)

# Other audio features
o_control = pd.read_excel('data/audio_features/Control.xls', sheet_name=None)
o_control_a1 = o_control['a1']
o_control_a2 = o_control['a2']
o_control_a3 = o_control['a3']
# Merge all dfs into  one
o_control = pd.concat((o_control_a1, o_control_a2, o_control_a3))

# Remove duracion
o_control = o_control.drop(['Duracion'], axis=1)

# Merge both on Nombre Archivo
control = pd.merge(f_control, o_control, on='Nombre Archivo')

# Nombre Archivo is defined as: {group}_{session}_{audio_material}_{id}.wav
# Split Nombre Archivo into columns
control['group'] = control['Nombre Archivo'].str.split('_').str[0]
control['session'] = control['Nombre Archivo'].str.split('_').str[1]
control['audio_material'] = control['Nombre Archivo'].str.split('_').str[2]
control['id'] = control['Nombre Archivo'].str.split('_').str[3].str.split('.').str[0]

# Rename group values: Sept -> Septoplasty
control['group'] = control['group'].replace('Cont', 'Control')

# Make ID the index and make sure its integer
control = control.set_index('id')
control.index = control.index.astype(int)

# Substitute ses1 to 2wbs, ses2 to 2was, ses3 to 3mas
control['session'] = control['session'].replace('ses1', '2wbs')
control['session'] = control['session'].replace('ses2', '2was')
control['session'] = control['session'].replace('ses3', '3mas')

# Remove nombre archivo column
control = control.drop(['Nombre Archivo'], axis=1)

# Sort by index
control = control.sort_index()

# Make all column names to uppercase
control.columns = control.columns.str.upper()

# Split into 3 dfs by session
control_2wbs = control[control['SESSION'] == '2wbs']
control_2was = control[control['SESSION'] == '2was']
control_3mas = control[control['SESSION'] == '3mas']

# ======================== FESS ========================
# Formants
f_fess = pd.read_excel('data/audio_features/Cens_Formants.xls', sheet_name=None)
f_fess_a1 = f_fess['a1']
f_fess_a2 = f_fess['a2']
f_fess_a3 = f_fess['a3']

# Merge all dfs into  one
f_fess = pd.concat((f_fess_a1, f_fess_a2, f_fess_a3))

# Remove duracion
f_fess = f_fess.drop(['Duracion'], axis=1)

# Other audio features
o_fess = pd.read_excel('data/audio_features/Cens.xls', sheet_name=None)
o_fess_a1 = o_fess['a1']
o_fess_a2 = o_fess['a2']
o_fess_a3 = o_fess['a3']

# Merge all dfs into  one
o_fess = pd.concat((o_fess_a1, o_fess_a2, o_fess_a3))

# Remove duracion
o_fess = o_fess.drop(['Duracion'], axis=1)

# Merge both on Nombre Archivo
fess = pd.merge(f_fess, o_fess, on='Nombre Archivo')

# Nombre Archivo is defined as: {group}_{session}_{audio_material}_{id}.wav
# Split Nombre Archivo into columns
fess['group'] = fess['Nombre Archivo'].str.split('_').str[0]
fess['session'] = fess['Nombre Archivo'].str.split('_').str[1]
fess['audio_material'] = fess['Nombre Archivo'].str.split('_').str[2]
fess['id'] = fess['Nombre Archivo'].str.split('_').str[3].str.split('.').str[0]

# Rename group values: Sept -> Septoplasty
fess['group'] = fess['group'].replace('Cens', 'FESS')

# Make ID the index and make sure its integer
fess = fess.set_index('id')
fess.index = fess.index.astype(int)

# Substitute ses1 to 2wbs, ses2 to 2was, ses3 to 3mas
fess['session'] = fess['session'].replace('ses1', '2wbs')
fess['session'] = fess['session'].replace('ses2', '2was')
fess['session'] = fess['session'].replace('ses3', '3mas')

# Remove nombre archivo column
fess = fess.drop(['Nombre Archivo'], axis=1)

# Sort by index
fess = fess.sort_index()

# Make all column names to uppercase
fess.columns = fess.columns.str.upper()

# Split into 3 dfs by session
fess_2wbs = fess[fess['SESSION'] == '2wbs']
fess_2was = fess[fess['SESSION'] == '2was']
fess_3mas = fess[fess['SESSION'] == '3mas']

# ======================== Tonsillectomy ========================
# Formants
f_tonsil = pd.read_excel('data/audio_features/Amigdalas_formants.xls', sheet_name=None)
f_tonsil_a1 = f_tonsil['a1']
f_tonsil_a2 = f_tonsil['a2']
f_tonsil_a3 = f_tonsil['a3']

# Merge all dfs into  one
f_tonsil = pd.concat((f_tonsil_a1, f_tonsil_a2, f_tonsil_a3))

# Remove duracion
f_tonsil = f_tonsil.drop(['Duracion'], axis=1)

# Other audio features
o_tonsil = pd.read_excel('data/audio_features/Amigdalas.xls', sheet_name=None)
o_tonsil_a1 = o_tonsil['a1']
o_tonsil_a2 = o_tonsil['a2']
o_tonsil_a3 = o_tonsil['a3']

# Merge all dfs into  one
o_tonsil = pd.concat((o_tonsil_a1, o_tonsil_a2, o_tonsil_a3))

# Remove duracion
o_tonsil = o_tonsil.drop(['Duracion'], axis=1)

# Merge both on Nombre Archivo
tonsil = pd.merge(f_tonsil, o_tonsil, on='Nombre Archivo')

# Nombre Archivo is defined as: {group}_{session}_{audio_material}_{id}.wav
# Split Nombre Archivo into columns
tonsil['group'] = tonsil['Nombre Archivo'].str.split('_').str[0]
tonsil['session'] = tonsil['Nombre Archivo'].str.split('_').str[1]
tonsil['audio_material'] = tonsil['Nombre Archivo'].str.split('_').str[2]
tonsil['id'] = tonsil['Nombre Archivo'].str.split('_').str[3].str.split('.').str[0]

# Rename group values: Sept -> Septoplasty
tonsil['group'] = tonsil['group'].replace('Amigdalas', 'Tonsillectomy')

# Make ID the index and make sure its integer
tonsil = tonsil.set_index('id')
tonsil.index = tonsil.index.astype(int)

# Substitute ses1 to 2wbs, ses2 to 2was, ses3 to 3mas
tonsil['session'] = tonsil['session'].replace('ses1', '2wbs')
tonsil['session'] = tonsil['session'].replace('ses2', '2was')
tonsil['session'] = tonsil['session'].replace('ses3', '3mas')

# Remove nombre archivo column
tonsil = tonsil.drop(['Nombre Archivo'], axis=1)

# Sort by index
tonsil = tonsil.sort_index()

# Make all column names to uppercase
tonsil.columns = tonsil.columns.str.upper()

# Split into 3 dfs by session
tonsil_2wbs = tonsil[tonsil['SESSION'] == '2wbs']
tonsil_2was = tonsil[tonsil['SESSION'] == '2was']
tonsil_3mas = tonsil[tonsil['SESSION'] == '3mas']

# ======================== Merge all ========================
# Merge all dfs of the same session
df_2wbs = pd.concat((septo_2wbs, control_2wbs, fess_2wbs, tonsil_2wbs))
df_2was = pd.concat((septo_2was, control_2was, fess_2was, tonsil_2was))
df_3mas = pd.concat((septo_3mas, control_3mas, fess_3mas, tonsil_3mas))


# ======================== Save to csv ========================
# Save to csv as audiofeatures_{session}.csv
df_2wbs.to_csv('data/audio_features/audiofeatures_2wbs.csv')
df_2was.to_csv('data/audio_features/audiofeatures_2was.csv')
df_3mas.to_csv('data/audio_features/audiofeatures_3mas.csv')

















