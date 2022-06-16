# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from typing import Any
import os

from .Camera import Camera


class OCR:
    def __init__(self, logger: Any) -> None:
        """
        __init__ Create instance of OCR

        :param logger: Class to provide logging functionality. It MUST
            include the following methods:
             - debug
             - info
             - warn
             - error
            and each method MUST accept the following parameters
             - module
             - message
        :type logger: Any
        """

        self._log = logger
        self._log.debug("OCR", "Creating instance of OCR")

        # Process environment variables
        if "OCR_SHOW_CAPTURE" in os.environ:
            try:
                self._show_capture = bool(int(os.environ["OCR_SHOW_CAPTURE"]))
            except ValueError:
                self._log.warn("CAMERA", f"Invalid value for OCR_SHOW_CAPTURE \"{os.environ['OCR_SHOW_CAPTURE']}\". Accepted values are 0 and 1")
                self._show_capture = False
        else:
            self._show_capture = False

        self._camera = Camera(0, logger)

    def get(self) -> int:
        """
        get Get the current value displayed

        :return: Value read on the meter in watts
        :rtype: int
        """
        
        self._log.info("OCR", "Getting current meter value")

        self._camera.capture(self._show_capture)

        # Testing value
        return 0