#
# {{ cookiecutter.name.replace(" ", "") }}.rpy
# {{ cookiecutter.product_name }}
# {{ cookiecutter.description }}
#
# (C) {{ cookiecutter.year }} {{ cookiecutter.author_name }}.
#

init 10 python:
    class {{ cookiecutter.name.replace(" ", "") }}(CAApplication):
        """{{ cookiecutter.description }}"""

        def __init__(self):
            CAApplication.__init__(
                self,
                app_path=AS_APPS_DIR + "{{ cookiecutter.name.replace(" ", "") }}.aosapp/"
            )

            # Write other initialization stuff for your app here.

    # Initialize the app outside of the class block to make it visible.
    {{ cookiecutter.name.lower().replace(" ", "") }} = {{ cookiecutter.name.replace(" ", "") }}()
