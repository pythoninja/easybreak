#!/usr/bin/env python
import argparse

from easybrake.handler import handle_generate
from easybrake import __version__


def get_cli_parser():
    parser = argparse.ArgumentParser(
        description="Utility to generate handbrake commands for batch processing",
        allow_abbrev=True,
    )

    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    subparser = parser.add_subparsers(
        help="generate the commands to run with shell", required=True
    )

    generate = subparser.add_parser("generate")
    generate.add_argument(
        "--input-dir",
        type=str,
        required=True,
        help="source directory where video files located",
    )
    generate.add_argument(
        "--output-dir",
        type=str,
        required=True,
        help="directory where result would be saved",
    )
    generate.add_argument(
        "--preset-path",
        type=str,
        required=True,
        help="path to the preset json file (exported from desktop app)",
    )
    generate.set_defaults(func=handle_generate)

    return parser


def run_cli():
    cli_parser: argparse.ArgumentParser = get_cli_parser()
    args: argparse.Namespace = cli_parser.parse_args()

    args.func(args)
