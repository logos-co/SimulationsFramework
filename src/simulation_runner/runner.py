# Python Imports
import os

# Project Imports
from src.utilities.env_variables import binary_name


def run_simulation(output_format, input_settings, output_file):
    os.system(binary_name + " -f " + output_format + " -i " + input_settings + " -o " + output_file)
