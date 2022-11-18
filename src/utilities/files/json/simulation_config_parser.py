from src.utilities import env_variables
from src.utilities.files.json.json_utils import read_json, validate_json


class SimulationConfigParser:

    def __init__(self, file_path):
        self._file_path = file_path
        self._configuration = None

    def read_content(self):
        # Retrieve raw info
        json_configuration = read_json(self._file_path)

        # Retrieve valid schema
        json_schema = read_json(env_variables.schema_path)

        # Validate
        validate_json(json_configuration, json_schema)
        self._configuration = json_configuration
