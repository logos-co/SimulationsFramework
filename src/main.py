# Python Imports
import typer


def main(
        run_type: str = typer.Option(..., "--run", "-r"),
):
    # Calls depending on json config
    pass


if __name__ == '__main__':
    print("test")
    # typer.run(main)
