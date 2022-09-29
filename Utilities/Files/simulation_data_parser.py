# Python Imports
import os.path

# Project Imports
from Utilities.Files.SimulationDataTypes.JsonDataSimulationHandler import JsonDataSimulationHandler
from Utilities.Files.SimulationDataTypes.CsvDataSimulationHandler import CsvDataSimulationHandler
from Utilities.Files.SimulationDataTypes.ParquetSimulationDataHandler import ParquetDataSimulationHandler

handlers = {'.csv': CsvDataSimulationHandler,
            '.json': JsonDataSimulationHandler,
            'parquet': ParquetDataSimulationHandler
            }


class SimulationDataParser:

    def __init__(self, file_path):
        self._file_path = file_path
        self._file_extension = None

    def read_content(self):
        # Check file exists
        self._check_file()
        # Check extension
        self._check_extension()
        # Get correct handler
        handler = self._get_data_handler()
        # Load content
        handler.load_data()
        # Convert it to dataframe
        dataframe = handler.convert_into_dataframe()
        # Return

    def _check_file(self):
        exists = os.path.exists(self._file_path)

        if not exists:
            print(f"File {self._file_path} does not exists.")
            exit(1)

    def _check_extension(self):
        return os.path.splitext(self._file_path)[1]

    def _get_data_handler(self):
        handler = handlers.get(self._file_extension)

        return handler()





