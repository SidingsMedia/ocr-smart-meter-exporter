# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from typing import Any

import cv2


class Camera:
    """
    A class representing the camera to be used
    """
    def __init__(self, cam_port: int, log: Any) -> None:
        
        self._camera = cv2.VideoCapture(cam_port)
        self._camera.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
        self._camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)
        
        self._log = log

    def capture(self, show: bool = False):

        self._log.debug("CAMERA" , "Capturing image")
        result, image = self._camera.read()

        if result:
            if show:
                self._log.info("CAMERA", "Waiting for window to close before continuing")
                self._show("capture", image)
            return image
        else:
            self._log.warn("CAMERA", "Failed to capture image")

    def _show(self, name: str, image: Any) -> None:
        """
        _show Show the image using the built in browser

        To exit the user can press any key or in most cases the X button
        of the window. Note, this will block the process until the user
        exits.

        :param name: Name of window
        :type name: str
        :param image: Image to show
        :type image: Any
        """

        cv2.imshow(name, image)
        cv2.waitKey(0)
