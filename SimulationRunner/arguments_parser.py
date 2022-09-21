from argparse import ArgumentParser


def parse_arguments(arguments_file):
    """

    :param arguments_file:
    :return:
    """

    parser = ArgumentParser(description='Automatic framework to launch simulations')
    parser.add_argument('simulation_config', type=str, help='Simulation file configuration')

