# Python Imports
import os

# Project Imports
from Utilities.env_variables import binary_path


def run_simulation(output_format, input_settings, output_file):
    os.system(binary_path + " -f " + output_format + " -i " + input_settings + " -o " + output_file)
