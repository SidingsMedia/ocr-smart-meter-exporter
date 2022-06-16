# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

"""
Main entry point for CLI access and development for the UK smart meter
OCR package. There is no real use to use this package directly other
than for development or debugging. This is not designed for production
usage by any means.
"""

assert len( __package__ ) > 0, """
The '__main__' module does not seem to have been run in the context of a
runnable package ... did you forget to add the '-m' flag?
Usage: python3 -m ocr
"""

import sys

from .OCR import OCR

class Log:
    """
    A basic log provider for testing

    This should not be used for production usage and is only really
    suitable for use in development and testing of this module.
    """
    def debug(module: str, message: str) -> None:
        print(f"[{module}] DEBUG: {message}")

    def info(module: str, message: str) -> None:
        print(f"[{module}] INFO: {message}")

    def warn(module: str, message: str) -> None:
        print(f"[{module}] WARN: {message}")
    
    def error(module: str, message: str) -> None:
        print(f"[{module}] ERROR: {message}")

def main() -> int:
    """
    main Entry point

    Entrypoint to the application

    :return: Status code 0 = success, any other code indicates faliure
    :rtype: int
    """

    app = OCR(Log)
    print(app.get())
    return 0

if __name__ == "__main__":
    sys.exit(main())
