# Project Imports
from src.utilities import env_variables
from src.utilities.files.json.json_utils import read_json, validate_json


class SimulationConfigParser:
    _file_path: str

    def __init__(self, file_path: str):
        self._file_path = file_path

    def read_content(self) -> tuple[dict, dict, dict]:
        # Retrieve raw info
        json_configuration = read_json(env_variables.SHARED_FOLDER + self._file_path)

        # Split two parts
        arguments_config = json_configuration["arguments"]
        simulation_config = json_configuration["simulation"]
        # plotter_config = json_configuration["plotter"]

        # Retrieve valid schemas
        arguments_json_schema = read_json(env_variables.ARGUMENTS_SCHEMA_PATH)
        config_json_schema = read_json(env_variables.CONFIGURATION_SCHEMA_PATH)
        # plotter_json_schema = read_json(env_variables.plotter_schema_path)

        # Validate
        validate_json(arguments_config, arguments_json_schema)
        validate_json(simulation_config, config_json_schema)
        # validate_json(plotter_config, plotter_json_schema)

        # return simulation_config, plotter_config
        return arguments_config, simulation_config, {}
