# Project Imports
from src.utilities import env_variables
from src.utilities.files.json.json_utils import read_json, validate_json


class SimulationConfigParser:
    _file_path: str

    def __init__(self, file_path: str):
        self._file_path = file_path

    def read_content(self) -> tuple[dict, dict, dict]:  # todo check variable length
        # Retrieve raw info
        json_configuration = read_json(env_variables.SHARED_FOLDER + self._file_path)

        # Split parts
        configurations = self._split_configuration(json_configuration)

        # Retrieve valid schemas
        schemas = self._retrieve_schemas()

        validate_info = tuple(zip(configurations, schemas))

        # Validate
        self._validate_configurations(validate_info)

        return configurations

    def _split_configuration(self, json_configuration: dict):
        arguments_config = json_configuration[env_variables.ARGUMENTS_BLOCK]
        simulation_config = json_configuration[env_variables.SIMULATION_BLOCK]
        plotter_config = json_configuration[env_variables.PLOTTER_BLOCK]

        return arguments_config, simulation_config, plotter_config

    def _retrieve_schemas(self):
        arguments_json_schema = read_json(env_variables.ARGUMENTS_SCHEMA_PATH)
        config_json_schema = read_json(env_variables.CONFIGURATION_SCHEMA_PATH)
        plotter_json_schema = read_json(env_variables.PLOTTER_SCHEMA_PATH)

        return arguments_json_schema, config_json_schema, plotter_json_schema

    def _validate_configurations(self, validate_info):
        for jsons in validate_info:
            validate_json(jsons[0], jsons[1])
