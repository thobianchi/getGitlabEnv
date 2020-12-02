# -*- coding: utf-8 -*-
"""

"""

import argparse
import logging
import sys

from gitlabctl import __version__

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def project(args):
    _logger.debug("sono in project")


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    root_parser = argparse.ArgumentParser(
        description="Gitlab CLI Application")
    subparsers = root_parser.add_subparsers(title="actions")
    root_parser.add_argument(
        "--version",
        action="version",
        version="gitlabctl {ver}".format(ver=__version__))
    root_parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    root_parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)

    project_parser = subparsers.add_parser(
        'project', help='interact with projects')
    project_parser.add_argument('get-env', help='get-env help')
    project_parser.set_defaults(func=project)
    return root_parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    args.func(args)
    _logger.info("Gitlabctl ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
