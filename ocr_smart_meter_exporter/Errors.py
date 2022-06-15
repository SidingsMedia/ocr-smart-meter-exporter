# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from .Logging import log


class FatalError(Exception):
    """
    FatalError Class to represent a fatal error that is returned to the user
    """

    def __init__(self, message: str = "A fatal error occured") -> None:
        log.error("APPLICATION", message)
        super().__init__()
