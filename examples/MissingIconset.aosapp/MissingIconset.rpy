#
# MissingIconset.rpy
# Missing iconset
# Missing the iconset folder
#
# (C) 2021 Foo Bar.
#

init 10 python:
    class MissingIconset(CAApplication):
        """Missing the iconset folder"""

        def __init__(self):
            CAApplication.__init__(
                self,
                app_path=AS_APPS_DIR + "MissingIconset.aosapp/"
            )

            # Write other initialization stuff for your app here.

    # Initialize the app outside of the class block to make it visible.
    missingiconset = MissingIconset()
