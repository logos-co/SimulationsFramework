import abc
from abc import ABC


class BaseDataSimulationHandler(ABC):

    def __init__(self):
        self._data = None

    @abc.abstractmethod
    def load_data(self, path):
        pass

    @abc.abstractmethod
    def convert_into_dataframe(self):
        pass
