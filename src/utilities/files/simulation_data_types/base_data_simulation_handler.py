# Python Imports
import abc
from abc import ABC
import polars as pl


class BaseDataSimulationHandler(ABC):

    @abc.abstractmethod
    def load_data(self, path: str) -> pl.DataFrame:
        pass
