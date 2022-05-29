#!python
"""
Yapper cli interface for invoking the methods in the handler module.
"""
import argparse

from yapper import handler

# prepare args
arg_parser = argparse.ArgumentParser(description="Load TOML configuration file for yapper.")
arg_parser.add_argument(
    "--config", type=str, help="Relative or absolute file path to the configuration file.", default=None, required=False
)


def parse_cli():
    """Command Line Interface to yapper."""
    args = arg_parser.parse_args()
    config_file = handler.load_config(args)
    yapper_config = handler.process_config(config_file)
    handler.main(yapper_config)


if __name__ == "__main__":
    parse_cli()
