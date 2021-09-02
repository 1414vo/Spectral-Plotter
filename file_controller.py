from astropy.io import fits
from pathlib import Path

def write_file(path, data):
    # Save the master image 2D array as a fits file, ...
    hdu=fits.PrimaryHDU(data)
    hdulist=fits.HDUList([hdu])
    # ... check the directory the file is in and create it if it does not exist
    directory = get_directory_from_path(path)
    if directory != '':
        Path(directory).mkdir(parents=True, exist_ok=True)
    # ... and write it to the desired location
    hdulist.writeto(path, overwrite=True)

def get_directory_from_path(path):
    # Find the last occurrence of a forward slash (change in directory)
    last_occurrence = path.rfind('/')
    # Return the path up to that directory
    if last_occurrence == -1:
        return ''
    else:
        return path[:last_occurrence]