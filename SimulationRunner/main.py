# Python Imports
import typer

# Project Imports
from Utilities.file_parser import ConfigurationFileParser


def main(
        # todo put in output format possible names (-f --output-format)
        output_format: str = typer.Argument("parquet"),
        input_settings: str = typer.Option(..., "--input-settings", "-i"),
        output_file: str = typer.Option(..., "--output-file", "-o")
):
    # Check config file
    parser = ConfigurationFileParser(input_settings)
    config = parser.read_content()
    # Calls simulation with configuration


if __name__ == '__main__':
    typer.run(main)

    # Run simulation with arguments

    pass
