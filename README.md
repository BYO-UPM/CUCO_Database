# CUCO Database

![CUCO Database Logo](your-logo.png) `<!-- Add your logo here if you have one -->`

Welcome to the CUCO Database repository! This is a comprehensive collection of code and data used for cleaning and calculating the CUCO database. The database comprises recordings of patients and control individuals, with voice samples taken at three different time points: 2 weeks before surgery, 2 weeks after surgery, and 3 months after surgery. The surgeries include FESS, Tonsillectomy, Septoplasty, and a control group.

## Repository Structure

The CUCO Database is organized into the following main folders:

- **audio-features**: Contains precalculated audio features such as formants and antiformants.
- **audios**: Raw audio data organized by type of surgery and audio said:
  - control
    - a, e, i, o, u, aeiou, a1, a2, a3, agua, braseo, concatenateread, dia, mesa, speech
  - fess
  - septo
  - tonsil
- **clinical**: Contains clinical data recorded at each hospital visit (three times: pre-surgery, post-surgery, 3 months post-surgery).
- **metadata**: Provides metadata for each patient in the database.
  - comments on the audio files
  - demographic data

## Installation

The CUCO Database is available on Zenodo with a Digital Object Identifier (DOI) to ensure easy access and citation. To access the database, follow these steps:

1. Visit the Zenodo page for the CUCO Database using the following link:
   [CUCO Database on Zenodo](https://zenodo.org/your-doi-here) not yet available ;)
2. You can download the dataset files and code directly from Zenodo.

For more information and specific setup instructions, refer to the dataset documentation on Zenodo.

**Note**: This repository contains the code used for cleaning and calculating the database.

## How to Cite

If you use the CUCO Database in your research or projects, we kindly request that you cite it to give credit to the contributors. Please use the following references to cite the database:

1. **Zenodo Dataset**: To cite the dataset available on Zenodo, use the provided DOI:
   1. Author(s). (Year). CUCO Database. Zenodo. DOI: [your-doi-here]
2. **Scientific Data Paper**: Additionally, we encourage you to cite the associated paper in XXXXX journal where the database is described in detail
   1. Author(s). (Year). Title of the Paper. Journal, Volume(Number), Page Numbers. DOI: [paper-doi-here]

Citing both the Zenodo dataset and the journal paper helps acknowledge the work of the contributors and ensures proper recognition in the academic community.

## Usage

Learn how to use the data and code in this repository:

* For using audio features, refer to the `audio-features` folder README.
* If you need raw audio data, explore the `audios` folder README.
* Access clinical data and usage instructions in the `clinical` folder README.

## License

Not yet

## Credits

We'd like to acknowledge and express our gratitude to everyone who has contributed to this project. Your efforts and support are highly appreciated.

## Contact Information

If you have questions or need further assistance, please feel free to reach out to us:

* Email: alejandro.guerrero@upm.es
* GitHub Issues: [Report an Issue](https://github.com/aguerrerolopez/CUCODB/issues)

Thank you for using the CUCO Database! We hope you find it valuable for your research and projects.
