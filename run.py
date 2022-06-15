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

    :return: Status code 0 = success, any other code indicates faliure
    :rtype: int
    """

    app = Application()
    return(app.run())

if __name__ == "__main__":
    sys.exit(main())