#!python
import argparse

from yapper import handler


# prepare args
arg_parser = argparse.ArgumentParser(description='Load YAML configuration file for yapper.')
arg_parser.add_argument('--config',
                        type=str,
                        help='Relative file path to the configuration file.',
                        default=None,
                        required=False)


def cli():
    """ """
    args = arg_parser.parse_args()
    config_file = handler.load_config(args)
    yap_config = handler.process_config(config_file)
    handler.main(yap_config)


if __name__ == '__main__':
    cli()
