% processAllAudioFiles.m
% Script to launch the karma_byo algorithm to extract formants and their trajectories from all WAV files in a directory
function processAllAudioFiles(audioDir, numFormants, numAntiF, aParams, cepOrder, cepType, algFlag)
    % Add any required paths
    addpath(genpath('./GitHub/CUCOdb/karma_formantes_2.1'));

    % Find all WAV files in the specified directory and its subdirectories
    wavFiles = dir(fullfile(audioDir, '**', '*.wav'));
    
    % Loop through the found WAV files
    for i = 1:numel(wavFiles)

        audioFile = fullfile(wavFiles(i).folder, wavFiles(i).name);
        disp(['Processing file: ', audioFile]);

        % Check if a corresponding .png file already exists
        pngFile = strrep(audioFile, '.wav', '.png');
        matFile = strrep(audioFile, '.wav', '.mat');
        
        %if exist(pngFile, 'file') && exist(matFile, 'file')
        %    disp('Skipping: .png and .mat files already exist.');
        %else
            % Call the processAudio function for each file
        processAudio(audioFile, numFormants, numAntiF, aParams, cepOrder, cepType, algFlag);
            
        disp(['Processing completed for: ', audioFile]);
        %end
    end
end


