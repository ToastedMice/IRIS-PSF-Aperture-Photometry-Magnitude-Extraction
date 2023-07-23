import sys
import tkinter as tk
from tkinter import filedialog
import math

def extract_data(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    magnitudes = []
    intensities = []
    backgrounds = []
    for line in lines:
        if line.startswith('Magnitude'):
            magnitude = line.split('=')[1].strip()
            magnitudes.append(magnitude)
        elif line.startswith('Intensity'):
            intensity = line.split('=')[1].strip()
            intensity = intensity.split('-')[0].strip()
            #background = intensity[1].strip()
            intensities.append(intensity)
            #background.append(background)

    with open(output_file, 'w') as f_out:
        f_out.write("Magnitudes:\n")
        for magnitude in magnitudes:
            f_out.write(magnitude + '\n')

        f_out.write("\Magnitudes (Only use these if the previous output has no data (These are converted from the intensities especially for the use with apeture photometry)):\n")
        for intensity in intensities:
            f_out.write(str(-2.5 * math.log10(float(intensity))) + '\n')

        #f_out.write("\nBackgrounds:\n")
        #for background in backgrounds:
        #    f_out.write(background + '\n')

    print(f"Successfully exported magnitudes to {output_file}")


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(title="Select Input File")
    output_file = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt")

    if input_file and output_file:
        extract_data(input_file, output_file)
    else:
        print("File selection cancelled.")


open_file_dialog()
