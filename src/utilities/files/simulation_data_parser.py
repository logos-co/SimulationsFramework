# Python Imports
import os.path

import polars

# Project Imports
from src.utilities.files.simulation_data_types.json_data_simulation_handler import JsonDataSimulationHandler
from src.utilities.files.simulation_data_types.csv_data_simulation_handler import CsvDataSimulationHandler
from src.utilities.files.simulation_data_types.parquet_simulation_data_handler import ParquetDataSimulationHandler

handlers = {'.csv': CsvDataSimulationHandler,
            '.json': JsonDataSimulationHandler,
            '.parquet': ParquetDataSimulationHandler
            }


class SimulationDataParser:

    def __init__(self):
        self._file_path = None
        self._file_extension = None

    def read_content(self, file_path: str) -> polars.DataFrame:
        self._file_path = file_path
        # Check file exists
        self._check_file()
        # Check extension
        self._check_extension()
        # Get correct handler
        handler = self._get_data_handler()
        # Load content
        polars_df = handler.load_data(self._file_path)
        # Return
        return polars_df

    def _check_file(self):
        exists = os.path.exists(self._file_path)

        if not exists:
            print(f"File {self._file_path} does not exists.")
            exit(1)

    def _check_extension(self):
        self._file_extension = os.path.splitext(self._file_path)[1]

    def _get_data_handler(self):
        handler = handlers.get(self._file_extension)

        return handler()





