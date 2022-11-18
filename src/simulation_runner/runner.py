# Python Imports
import os

# Project Imports
from src.utilities.env_variables import binary_path, configuration_settings, shared_folder
from src.utilities.files.json.json_utils import write_json


def run_simulation(arguments_config: dict, simulation_config: dict):

    write_json(simulation_config, configuration_settings)

    os.system(binary_path
              + " -f " + arguments_config["output-format"]
              + " -i " + configuration_settings + " -o "
              + arguments_config["output-file"])

    os.system("mv " + arguments_config["output-file"] + "." + arguments_config["output-format"] + " " + shared_folder)
