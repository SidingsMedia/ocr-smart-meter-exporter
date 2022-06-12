# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import os
import datetime

class Logging:
    """
    Unified logging

    This class provides unified and consistent logging across the entire
    application in order to aid processing using external tools. Based
    upon
    https://github.com/louislam/uptime-kuma/blob/39aa0a7f07644ecdd99e0a8ddacbbb24e2afd931/src/util.ts#L61-L148
    """

    
    hide_logs:list[str]

    def __init__(self) -> None:
        if os.environ("OCR_EXPORTER_HIDE_LOG"):
            hidden_logs = os.environ("OCR_EXPORTER_HIDE_LOG").upper().split(',')
            self.hide_logs.append(hidden_logs)

    def log(self, module: str, msg: str, level: str) -> None:
        """
        log Create a log entry to stdout

        Create a standardised log entry to stdout with information on
        where it came from as well as the log level

        :param module: Section of application log originates from
        :type module: str
        :param msg: Log message
        :type msg: str
        :param level: Log level
        :type level: str
        """

        level = level.upper()
        current_time = datetime.time.isoformat()
        formatted_message = f"{current_time} [{module}] {level}: {msg}"

        if level not in self.hide_logs:
            print(formatted_message)

    def debug(self, module: str, msg: str) -> None:
        """
        debug Write debug log

        :param module: Section of application log originates from
        :type module: str
        :param msg: Log message
        :type msg: str
        """

        self.log(module, msg, "debug")

    def info(self, module: str, msg: str) -> None:
        """
        info Write info log

        :param module: Section of application log originates from
        :type module: str
        :param msg: Log message
        :type msg: str
        """

        self.log(module, msg, "info")

    def warn(self, module: str, msg: str) -> None:
        """
        warn Write warn log

        :param module: Section of application log originates from
        :type module: str
        :param msg: Log message
        :type msg: str
        """

        self.log(module, msg, "warn")

    def error(self, module: str, msg: str) -> None:
        """
        error Write error log

        :param module: Section of application log originates from
        :type module: str
        :param msg: Log message
        :type msg: str
        """

        self.log(module, msg, "error")


log = Logging()