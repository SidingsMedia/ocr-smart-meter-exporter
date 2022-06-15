#!/usr/env/python3

# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

"""
Call this file to start the application
"""

import sys
import os

from ocr_smart_meter_exporter import Application

def main() -> None:
    """
    main Entry point

    Entrypoint to the application
    """

    app = Application()
    app.run()

if __name__ == "__main__":
    main()