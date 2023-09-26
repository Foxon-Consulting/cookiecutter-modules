import contextlib
import os
from importlib import resources

import tomli

# Version of the package
__version__ = "0.0.1"

config = tomli.loads(
    resources.files("{{ cookiecutter.__folder_name_formatted }}").joinpath("config.toml").read_text()
)
