from sys import argv
from argparse import ArgumentParser
from typing import List, Optional
from cookiecutter.main import cookiecutter
from click.exceptions import Abort


def get_args(override: Optional[List] = None):
    arguments = ArgumentParser(description="Boostrap Candella frameworks and apps.")
    arguments.add_argument("--action", help="The action to run.", required=True)
    arguments.add_argument("--type", help="The type of project to create.", nargs=1, default="application")
    return arguments.parse_args(override if override else argv[1:])


def create_project(app_type: str):
    if app_type == "application":
        cookiecutter('cookiecutter-candella-app')
    elif app_type == "service":
        cookiecutter('cookiecutter-candella-service')
    elif app_type == "framework":
        cookiecutter('cookiecutter-candella-framework')
    else:
        print(f"The following is not a valid project type: {app_type}")

def main():
    OPTIONS = get_args()

    if OPTIONS.action == "create":
        try:
            create_project(OPTIONS.type[0])
        except Abort:
            print("\nAbort.")

if __name__ == "__main__":
    main()