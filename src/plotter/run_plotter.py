# Python Imports
import seaborn as sns
import matplotlib.pyplot as plt

# Project Imports
from src.utilities.env_variables import SHARED_FOLDER
from src.utilities.files.simulation_data_parser import SimulationDataParser


def run_plotter(arguments_config: dict, plotter_config: dict):
    file_name = f"{arguments_config['output-file']}.{arguments_config['output-format']}"
    # Read file given in arguments config
    parser = SimulationDataParser()
    polars_df = parser.read_content(SHARED_FOLDER + file_name)

    pandas_df = polars_df.to_pandas()

    # Loop through all plots given in plotting section
    for plot, options in plotter_config.items():
        print(plot)
        print(options)
        method = getattr(sns, plot)
        method(pandas_df, **options["plot_options"])
        plt.savefig(SHARED_FOLDER + options["save_options"]["name"])
