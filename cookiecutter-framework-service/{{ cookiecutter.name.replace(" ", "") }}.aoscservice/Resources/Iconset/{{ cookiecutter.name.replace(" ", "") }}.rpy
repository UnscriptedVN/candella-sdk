#
# {{ cookiecutter.name.replace(" ", "") }}.rpy
# {{ cookiecutter.name }}
#
# (C) {{ cookiecutter.year }} {{ cookiecutter.author_name }}.
#

init offset = 5
init python:
    class {{ cookiecutter.name.replace(" ", "") }}(CACoreService):
        """{{ cookiecutter.description }}"""


        def __init__(self):
            CACoreService.__init__(
                self,
                AS_CORESERVICES_DIR + "{{ cookiecutter.name.replace(" ", "") }}.aoscservice/"
            )

            # Initialize your core service here.

    # Initialize the service outside of the class.
    {{ cookiecutter.name.lower().replace(" ", "") }} = {{ cookiecutter.name.replace(" ", "") }}()
