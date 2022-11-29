# Python Imports
import polars as pl

# Project Imports
from src.utilities.files.simulation_data_types.base_data_simulation_handler import BaseDataSimulationHandler


class ParquetDataSimulationHandler(BaseDataSimulationHandler):

    def load_data(self, path: str) -> pl.DataFrame:
        polars_df = pl.read_parquet(path)

        return polars_df
