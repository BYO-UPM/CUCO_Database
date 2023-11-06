import os


# Check if the karma process is finished

# To do so, lets walk all the data/audios path and check if for each .wav there exists a .png and .mat with the same name
def check_if_karma_finished():
    # Get the path to the data/audios folder
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'audios')
    # Get all the files (the folder contain subforlders) use os.walk
    files = []
    wav_files = []
    png_files = []
    mat_files = []
    for (dirpath, dirnames, filenames) in os.walk(data_path):
        # Add to each list the files with the corresponding extension
        files.extend(filenames)
        wav_files.extend([f for f in filenames if f.endswith('.wav')])
        png_files.extend([f for f in filenames if f.endswith('.png')])
        mat_files.extend([f for f in filenames if f.endswith('.mat')])

    # Check if the number of files is the same
    if len(wav_files) == len(png_files) == len(mat_files):
        # If so, return True
        return True
    else:
        # If not, get which files are missing using intersect
        missing_png_files = list(set(wav_files) - set(png_files))
        missing_mat_files = list(set(wav_files) - set(mat_files))
        return False



    
if __name__ == '__main__':
    # Check if the karma process is finished
    if check_if_karma_finished():
        # If so, print a message
        print('Karma process finished')
    else:
        # If not, print a message
        print('Karma process not finished')