# Rename all files to match the paper description


# Read all audio files and folders under "data/data_final/audios". Then for each folder and file, rename:
# 1. "control" to "Contr"
# 2. "Cens" to "FESS"
# 3. "Septo" to "Sept"
# 4. "Amig" to "Tonsill"

import os
import shutil
import re

# Get the path to the data/audios folder
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data_final', 'audios')

# Get the full path to each filename
full_path= [os.path.join(dirpath, f) for (dirpath, dirnames, filenames) in os.walk(data_path) for f in filenames]


# For each filename, rename the file
for f in full_path:
    # Get the new name
    new_name = re.sub('control', 'Contr', f)
    new_name = re.sub('Cens', 'FESS', new_name)
    new_name = re.sub('Septo', 'Sept', new_name)
    new_name = re.sub('Amig', 'Tonsill', new_name)
    # Rename the file
    shutil.move(f, new_name)
