
import os
import shutil

def find_and_copy_files(source_directory, target_directory):
    # Create the target directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file is a .txt file
            if file.endswith('.txt'):
                txt_file_path = os.path.join(root, file)
                wav_file_path = txt_file_path[:-4] + '.wav'
                
                # Check if the corresponding .wav file exists
                if os.path.exists(wav_file_path):
                    # Copy .txt and .wav files to the target directory
                    shutil.copy(txt_file_path, target_directory)
                    shutil.copy(wav_file_path, target_directory)

# Example usage
source_directory = './all_audios/'
target_directory = './monologues_transcripted'
find_and_copy_files(source_directory, target_directory)


def organize_files_by_name(source_directory):
    # Define the subfolders based on file name identifiers
    subfolders = ['pos2s', 'pre', 'pos3m']
    
    # Create subfolders if they don't exist
    for subfolder in subfolders:
        os.makedirs(os.path.join(source_directory, subfolder), exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Skip if we're looking at files in the already created subfolders
            if root != source_directory:
                continue
            
            # Move files based on the identifier in their names
            for identifier in subfolders:
                if f"_{identifier}." in file:
                    source_file_path = os.path.join(root, file)
                    target_file_path = os.path.join(source_directory, identifier, file)
                    
                    # Move the file to the corresponding subfolder
                    shutil.move(source_file_path, target_file_path)
                    break

# Example usage
source_directory = './monologues_transcripted'
organize_files_by_name(source_directory)

import os
import pandas as pd

def rename_files_based_on_excel(directory, excel_path):
    # Load the Excel file
    df = pd.read_excel(excel_path)

    # Create a mapping from internal patient ID to (real patient ID, intervention)
    mapping = {row[1][0]: (row[1][1], row[1][2]) for row in df.iterrows()}

    # Walk through the directory to find .txt and .wav files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') or file.endswith('.wav'):
                parts = file.split('_')
                if len(parts) < 2:
                    continue
                
                patient_id = int(parts[0])
                extension = parts[-1].split('.')[-1]
                # Get real patient ID and intervention from the mapping
                if patient_id in mapping:
                    real_patient_id, intervention = mapping[patient_id]

                    # Create the new filename and rename the file
                    new_filename = f"{intervention}_{real_patient_id}.{extension}"
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(root, new_filename)

                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{file}' to '{new_filename}'")

# Example usage
directory = '/monologues_transcripted'  # Directory containing the files
excel_path = '/trans.xlsx'  # Path to the Excel file
rename_files_based_on_excel(directory, excel_path)


import os

def homogenize_filenames(directory):
    # Mapping of original prefixes to the new ones
    prefix_mapping = {
        'AMIG': 'Tonsill',
        'CENS': 'Fess',
        'SEPT': 'Sept',
        'CONTROL': 'Contr'
    }
    
    # Walk through the directory to find files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Split the filename into parts
            name, ext = os.path.splitext(file)
            parts = name.split('_')
            if len(parts) != 2:
                continue  # Skip files that don't match the expected format
            
            prefix, patient_id = parts
            if prefix in prefix_mapping:
                # Rename the prefix according to the mapping
                new_prefix = prefix_mapping[prefix]
                # Format the patient ID with leading zeros
                new_patient_id = f"{int(patient_id):04d}"
                # Construct the new filename
                new_filename = f"{new_prefix}_{new_patient_id}{ext}"
                # Full path for old and new filenames
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{file}' to '{new_filename}'")

# Example usage
directory = 'monologues_transcripted'  # Directory containing the files
homogenize_filenames(directory)


