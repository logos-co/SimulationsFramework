# Python Imports
import typer

# Project Imports
from src.plotter.run_plotter import run_plotter
from src.simulation_runner.runner import SimulationRunner
from src.utilities.files.json.simulation_config_parser import SimulationConfigParser


def main(
        run_type: str = typer.Option(..., "--run", "-r"),
        configuration_file: str = typer.Option(..., "--configuration-file", "-cf")
):
    parser = SimulationConfigParser(configuration_file)
    arguments_config, simulation_config, plotter_config = parser.read_content()
    # Calls depending on json config
    if run_type == "simulation":
        runner = SimulationRunner(arguments_config, simulation_config)
        runner.run_simulation()
    elif run_type == "plotter":
        run_plotter(arguments_config, plotter_config)
    else:
        runner = SimulationRunner(arguments_config, simulation_config)
        runner.run_simulation()
        run_plotter()


if __name__ == '__main__':
    typer.run(main)
