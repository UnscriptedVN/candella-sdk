#
# Valid.rpy
# A Valid App
# A perfectly valid app.
#
# (C) 2021 Unscripted VN Team.
#

init 10 python:
    class Valid(CAApplication):
        """A perfectly valid app."""

        def __init__(self):
            CAApplication.__init__(
                self,
                app_path=AS_APPS_DIR + "Valid.aosapp/"
            )

            # Write other initialization stuff for your app here.

    # Initialize the app outside of the class block to make it visible.
    valid = Valid()
