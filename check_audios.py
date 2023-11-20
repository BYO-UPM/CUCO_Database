# This code was used to check if the audios /a/ were extracted from /aeiou/ correctly


import librosa

# Read "data/audios/control/aeiou/control_ses1_aeiou_0012.wav"
audio_path = 'data/audios/control/aeiou/1/control_ses1_aeiou_0012.wav'

# Load audio file with librosa
audio, sr = librosa.load(audio_path, sr=44100)

# Check if the first part of the audio (correponding to the /a/ vowel) is equal to the audio located in "data/audios/control/a/1/control_ses1_a_0012.wav"
audio_a, sr_a = librosa.load('data/audios/control/a/1/control_ses1_a_0012.wav', sr=44100)

audio1 = audio[:len(audio_a)*2]
audio2 = audio_a

# Concatenate 50k 0s to audio 2
import numpy as np
audio2 = np.concatenate((np.zeros(55000), audio2))

# plot both audios
from matplotlib import pyplot as plt
plt.plot(audio1)
plt.plot(audio2)


