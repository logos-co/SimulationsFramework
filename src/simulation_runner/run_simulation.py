# Python Imports
import typer

# Project Imports
from src.utilities.files.json.simulation_config_parser import SimulationConfigParser
from runner import run_simulation


def main(
        # todo put in output format possible names (-f --output-format)
        output_format: str = typer.Option(..., "--output-format", "-f"),
        # input_settings: str = typer.Option(..., "--input-settings", "-i"),
        output_file: str = typer.Option(..., "--output-file", "-o")
):
    # Check config file
    input_settings = "/app/config_example.json"
    parser = SimulationConfigParser(input_settings)
    parser.read_content()
    # Calls simulation with configuration
    run_simulation(output_format, input_settings, output_file)


if __name__ == '__main__':
    typer.run(main)
