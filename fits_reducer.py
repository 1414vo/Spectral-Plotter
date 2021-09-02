from astropy.io import fits
import numpy as np
import glob
import file_controller as fc

def get_data_median(file_paths):
    get_data = lambda x: fits.open(x)[0].data
    return np.median([get_data(f) for f in file_paths], axis = 0)

def create_reduced(star_name):
    # Input file names
    input_files = glob.glob('data/' + star_name + '/*.fit')

    # Dark frame names
    dark_files = glob.glob('data/' + star_name + '/dark/*.fit')

    # Where the result will be saved
    output_location = 'data/' + star_name + '/results/' + star_name + '.fit'

    # Calculate the master dark and the median exposure
    master_dark = get_data_median(dark_files)
    data = get_data_median(input_files) - master_dark

    # Write the output to a file
    fc.write_file(output_location, data)
