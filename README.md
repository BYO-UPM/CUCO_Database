# CUCO Database

![CUCO Database Logo](logo_ai.png)

Welcome to the CUCO Database repository! This is a comprehensive collection of code and data used for cleaning and calculating the CUCO database. The database comprises recordings of patients and control individuals, with voice samples taken at three different time points: 2 weeks before surgery, 2 weeks after surgery, and 3 months after surgery. The surgeries include FESS, Tonsillectomy, Septoplasty, and a control group.

## Repository Structure

The CUCO Database is organized into the following main folders:

- **Audio Features**: Contains precalculated audio features such as formants and antiformants. For each audio file located in "Audios" there exists a .png image and a .pkl dictionary containing the frequency and bandwidth values for formant and antiformant trajectories of each speech waveform. A Kalman-based autoregressive moving average approach is employed [1-3].
  - [1]   D. D. Mehta, D. Rudoy, and P. J. Wolfe, "Kalman-based autoregressive
    moving average modeling and inference for formant and antiformant tracking,"
    The Journal of the Acoustical Society of America, vol. 132, no. 3, pp. 1732-1746, 2012.
  - [2]   D. Rudoy, D. N. Spendley, and P. J. Wolfe, "Conditionally linear
    Gaussian models for estimating vocal tract resonances," Proceedings of
    Interspeech, Antwerp, Belgium, 2007.
  - [3]   D. Rudoy, "Nonstationary time series modeling with application to speech
    signal processing," Doctor of Philosophy thesis, School of Engineering
    and Applied Sciences, Harvard University, Cambridge, MA, 2010.
    Chapter 3.
- **audios**: Raw audio data organized by type of surgery and audio said:
  - Contr
    - a, e, i, o, u, aeiou, a1, a2, a3, agua, braseo, concatenateread, dia, mesa, speech
  - Fess
  - Sept
  - Tonsill
- **Clinical**: Contains clinical data recorded at each hospital visit (three times: pre-surgery, post-surgery, 3 months post-surgery).
- **Metadata**: Provides metadata for each patient in the database.
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
