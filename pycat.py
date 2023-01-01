#!/usr/bin/env python3

import importlib
import os
from session import Session

import click


@click.command()
@click.option("--bind", default=os.environ.get('PYCAT_BIND', 'localhost'), help='Bind Address', show_default=True)
@click.argument("world", default=lambda: os.environ.get('PYCAT_WORLD'))
@click.argument("port", default=lambda: os.environ.get('PYCAT_PORT', 7777))
@click.argument('arg', default=lambda: os.environ.get('PYCAT_ARG', ""))
def main(world: str, port: str | int, arg: str, bind: str, **kwargs: str) -> None:
    if world:
        world_module = importlib.import_module('worlds.' + world)
    else:
        world_module = importlib.import_module('modular')
    port = int(port)
    ses = Session(world_module, port, arg, bind)
    ses.run()


if __name__ == '__main__':
    main.main()
