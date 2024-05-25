import logging

logging.getLogger().setLevel(logging.DEBUG)

from . import config


def _{{cookiecutter.__first_script_name_formatted}}(argA, argB):

    from examples.example1 import get_cat_name, dog_name

    # How to access to the dog name and cat name from another module
    logging.debug(
        f"Form Mouodle: The dog name is {dog_name} and the cat name is {get_cat_name()}"
    )

    # Example how to access config toml file
    logging.debug(f"from config file: {config}")

    # Return arguments
    return {
        "argA": argA,
        "argB": argB,
    }


def main():
    import argparse

    script_parser = argparse.ArgumentParser(
        prog="{{cookiecutter.__first_script_name_formatted}}",
        description="{{cookiecutter.__first_script_name_formatted}} script",
    )

    script_parser.add_argument(
        "-a",
        "--argA",
        action="store",
        metavar="arg1",
        help="{{cookiecutter.__first_script_name_formatted}} argA",
        required=True,
    )

    script_parser.add_argument(
        "-b",
        "--argB",
        action="store",
        metavar="color",
        help="{{cookiecutter.__first_script_name_formatted}} color",
        required=True,
    )

    result = _{{cookiecutter.__first_script_name_formatted}}(**vars(script_parser.parse_args()))

    # Example how to access config toml file
    logging.debug(config)

    # Using **vars() to convert Namespace to dict
    logging.debug(result)

    return result


if __name__ == "__main__":
    main()
