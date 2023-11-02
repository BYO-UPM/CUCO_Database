#!/bin/bash

# Specify the path to the MATLAB executable
MATLAB_EXECUTABLE="matlab"

# Path to the MATLAB script
MATLAB_SCRIPT="/home/alexjorguer/GitHub/CUCOdb/karma_formantes_2.1/processAudio.m"

# Input parameters (modify as needed)
numFormants=3
numAntiF=0
peCoeff=0.5
wType='hamming'
wLengthMS=20
wOverlap=0.8
lpcOrder=12
zOrder=0
fs=7000
cepOrder=15
cepType=1
algFlag=2

# Directory containing the WAV files
AUDIO_DIR="data/audios"

# Find all WAV files in the directory and its subdirectories
wav_files=$(find "$AUDIO_DIR" -type f -name "*.wav")

# Loop through the found WAV files
for audio_file in $wav_files; do
    echo "Processing file: $audio_file"
    
    # Call MATLAB script to process the audio file
    $MATLAB_EXECUTABLE -nodisplay -nodesktop -r "addpath('/home/alexjorguer/GitHub/CUCOdb/karma_formantes_2.1'); processAudio('$audio_file', $numFormants, $numAntiF, struct('peCoeff', $peCoeff, 'wType', '$wType', 'wLengthMS', $wLengthMS, 'wOverlap', $wOverlap, 'lpcOrder', $lpcOrder, 'zOrder', $zOrder, 'fs', $fs), $cepOrder, $cepType, $algFlag); exit"
    
    echo "Processing completed for $audio_file"
done
