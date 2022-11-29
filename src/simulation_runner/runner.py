# Python Imports
import os
import shutil
import random
from typing import Generator

# Project Imports
from src.utilities.env_variables import BINARY_PATH, CONFIGURATION_SETTINGS, SHARED_FOLDER
from src.utilities.files.json.json_utils import write_json


class SimulationRunner:

    def __init__(self, arguments_config: dict, simulation_config: dict):
        self._arguments_config = arguments_config
        self._base_simulation_config = simulation_config
        random.seed(self._base_simulation_config["seed"])

    def run_simulation(self):

        output_path = self._create_folder()

        seeds_generator = self._create_seeds_generator()

        for seed in seeds_generator:
            self._base_simulation_config["seed"] = seed

            write_json(self._base_simulation_config, CONFIGURATION_SETTINGS)

            file_format = self._arguments_config["output-format"]
            output_name = self._arguments_config["output-file"] + "_" + str(seed)

            os.system(f"{BINARY_PATH} -f {file_format} -i {CONFIGURATION_SETTINGS} -o {output_name}")

            os.system(f"mv {output_name}.{file_format} {output_path}")

    def _create_folder(self):
        output_path = SHARED_FOLDER + self._arguments_config["output-folder"]

        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.makedirs(output_path)

        return output_path

    def _create_seeds_generator(self) -> Generator[int, None, None]:
        # Rust binary seed uses u64 int
        seeds = (random.randint(0, 2 ** 64) for _ in range(self._arguments_config["number-of-simulations"]))

        return seeds
