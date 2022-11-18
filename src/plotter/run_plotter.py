# Python Imports
import typer


def main(
        input_data: str = typer.Option(..., "--input-data", "-i"),
        plot_type: str = typer.Option(..., "--plot-type", "-p"),
        plot_settings: str = typer.Option(..., "--plot-settings", "-s"),
):
    # Parse data file
    print("")
    # Accept plot type

    # Handle Plot arguments


'''
import foo
bar = getattr(foo, 'bar')
result = bar()
'''

if __name__ == '__main__':
    typer.run(main)
