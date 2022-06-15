# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from typing import Any


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

    def get(self) -> int:
        """
        get Get the current value displayed

        :return: Value read on the meter in watts
        :rtype: int
        """
        
        self._log.info("OCR", "Getting current meter value")

        # Testing value
        return 0