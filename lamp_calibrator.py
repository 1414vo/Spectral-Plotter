import numpy as np
from astropy.io import fits
def get_equation_from_lamp(path, lamp_wavelengths, spectrum_y):
    # Loading lamp file
    lamp = fits.open(path)
    lamp_data, lamp_hdr = lamp[0].data, lamp[0].header
    lamp_1d = lamp_data[spectrum_y,:]

    # Get lamp peaks
    peaks = get_main_peaks(lamp_1d)

    # Calibrate x-dependcy by fitting a line from maxima and wavelengths
    poly = np.polyfit(peaks,lamp_wavelengths,1)
    a, b = poly[0], poly[1]
    return lambda x: a*x + b

def get_main_peaks(graph):

    # Get graph peaks
    lamp_len = len(graph)
    peaks = np.array([])
    for i in range(lamp_len):
        if i != 0 and i != lamp_len - 1:
            # Local maximum check
            cond1 = float(graph[i]) - float(graph[i - 1]) < 0
            cond2 = float(graph[i + 1]) - float(graph[i]) < 0
            # Check if local maximum is not noise (edit if there are more lines to fit)
            cond3 = graph[i] > 3000
            if (cond1 != cond2) and cond3:
                peaks = np.append(peaks, i) 
    return peaks