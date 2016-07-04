#!env python
"""
cli entry point for pocha
"""

import os
import sys

import click

import discover
import runner

from reporters import get_reporter
from version import VERSION

@click.version_option(prog_name='pocha', version=VERSION)
@click.command()
@click.argument('path', default='test')
@click.option('--reporter', '-r',
              default='spec',
              type=click.Choice(['spec','dot','xunit']))
@click.option('--filter', '-f', 'expression', default=None)
def cli(path, reporter, expression):

    if os.path.exists(path):
        tests = discover.search(path, expression)
        reporter_object = get_reporter(reporter)()

        if runner.run_tests(tests, reporter_object):
            sys.exit(1)

    else:
        raise Exception('%s does not exist' % path)

if __name__ == '__main__':
    cli()