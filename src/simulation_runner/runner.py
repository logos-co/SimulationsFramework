# Python Imports
import os

# Project Imports
from src.utilities.env_variables import BINARY_PATH, CONFIGURATION_SETTINGS, SHARED_FOLDER
from src.utilities.files.json.json_utils import write_json


def run_simulation(arguments_config: dict, simulation_config: dict):

    write_json(simulation_config, CONFIGURATION_SETTINGS)

    os.system(BINARY_PATH
              + " -f " + arguments_config["output-format"]
              + " -i " + CONFIGURATION_SETTINGS + " -o "
              + arguments_config["output-file"])

    os.system("mv " + arguments_config["output-file"] + "." + arguments_config["output-format"] + " " + SHARED_FOLDER)
