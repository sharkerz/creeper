#!/usr/bin/env python
import argparse
import re

from ghost import Ghost


# Regex for checking if a url is correct
regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Or ip
    r'(?::\d+)?'  # Optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def parse_arguments():
    """Gets the console arguments"""
    parser = argparse.ArgumentParser(
        description='Creates random requests to a target url')
    parser.add_argument(
        "url", type=valid_url, help=("Target url"))
    return vars(parser.parse_args())


def valid_url(url):
    """Checks that the given networks are defined in settings"""
    if not regex.match(url):
        raise argparse.ArgumentTypeError(
            "'{0}' is not a valid url".format(url))
    return url


if __name__ == "__main__":
    arg_dict = parse_arguments()
    ghost = Ghost()
