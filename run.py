#!/usr/env/python3

# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

"""
Call this file to start the application
"""

import sys

from ocr_smart_meter_exporter import Application

def main() -> int:
    """
    main Entry point

    Entrypoint to the application

    :return: Exit code
    :rtype: int
    """

    app = Application()

    # Start app with catch all exception to log errors. This does not
    # provide any cleanup. This should be included in the main
    # application.
    try:
        r_type = app.run()
    except Exception as e:
        print(e)
        r_type = 1
        
    return r_type

if __name__ == "__main__":
    sys.exit(main())