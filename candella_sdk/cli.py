#
# cli.py
# Candella SDK
# 
# (C) 2021 Marquis Kurt.
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from sys import argv
from argparse import ArgumentParser
from typing import List, Optional
from cookiecutter.main import cookiecutter
from click.exceptions import Abort


def get_args(override: Optional[List[str]] = None):
    """Returns the namespace of parsed arguments.
    
    Arguments:
        override (list): A list of strings containing arguments to parse. Defaults to None and will use `sys.argv` if
            undefined.
    
    Returns:
        arguments (any): The parsed arguments as a namespace.
    """
    arguments = ArgumentParser(description="Boostrap Candella frameworks and apps.")
    arguments.add_argument("--action", help="The action to run.", required=True)
    arguments.add_argument("--type", help="The type of project to create.", nargs=1, default="application")
    return arguments.parse_args(override if override else argv[1:])


def create_project(proj: str):
    """Creates a project with a corresponding Cookiecutter template.
    
    Arguments:
        proj (str): The type of project to create.
    """
    if proj not in ["application", "service", "framework"]:
        print(f'The following is not a valid Candella project type: {proj}')
        return 1
    
    project_type = "app" if proj == "application" else proj
    cookiecutter(f"https://github.com/UnscriptedVN/candella-{project_type}-template.git")


def main():
    """Runs the main code for the SDK manager."""
    OPTIONS = get_args()

    if OPTIONS.action == "create":
        try:
            create_project(OPTIONS.type[0])
        except Abort:
            print("\nAbort.")

if __name__ == "__main__":
    main()