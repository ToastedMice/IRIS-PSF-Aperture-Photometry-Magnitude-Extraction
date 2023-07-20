import sys
import tkinter as tk
from tkinter import filedialog

def extract_data(input_file, output_file):
    magnitudes = []
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()
    with open(output_file, 'w') as f_out:
        f_out.write("Magnitudes:\n")
        for line in lines:
            if line.startswith('Magnitude'):
                magnitude = line.split('=')[1].strip()
                magnitudes.append(magnitude)
                if len(magnitudes) == 5:
                    print(magnitudes)
                    int_magnitudes = []
                    for magnitudestr in magnitudes:
                        int_magnitudes.append(float(magnitudestr))
                    average = round(sum(int_magnitudes) / len(int_magnitudes), 3)
                    f_out.write(str(average) + '\n')
                    magnitudes = []        

    print(f"Successfully exported magnitudes and intensities to {output_file}")


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
