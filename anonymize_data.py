import pandas as pd
from datetime import datetime
from googletrans import Translator


# Define the function to anonymize the surgery date
def anonymize_surgery_date(date_str):
    try:
        # First check if it is NaN, in that case, just skip
        if pd.isna(date_str):
            return date_str
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.replace(day=1).strftime("%m/%d/%Y")
    except ValueError:
        return date_str


# List of files to process
files = ["clinical_Ses1.csv", "clinical_Ses2.csv", "clinical_Ses3.csv"]

for file in files:
    # Read the CSV file
    df = pd.read_csv(file)

    # Check if "SURGERY DATE" column exists
    if "SURGERY DATE" in df.columns:
        # Apply the anonymization function to the column
        df["SURGERY DATE"] = df["SURGERY DATE"].apply(anonymize_surgery_date)

        # Save the modified dataframe back to CSV
        df.to_csv(file, index=False)

print("Anonymization complete.")


# Initialize the Google Translator
translator = Translator()

# files = ["audio_comments.csv"]


def translate_to_english(text):
    try:
        if isinstance(text, str):
            translated = translator.translate(text, dest="en")
            return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text
    return text


for file in files:
    # Read the CSV file
    df = pd.read_csv(file)

    # Apply the translation function to all cells
    df = df.applymap(translate_to_english)

    # Save the modified dataframe back to CSV
    df.to_csv(file, index=False)

print("Translation to English complete.")
