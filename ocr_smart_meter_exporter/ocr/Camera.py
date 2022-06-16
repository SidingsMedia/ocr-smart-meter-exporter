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
        cv2.imshow(name, image)

        wait_time = 1000
        while cv2.getWindowProperty(name, cv2.WND_PROP_VISIBLE) >= 1:
            key_code = cv2.waitKey(wait_time)
            if (key_code & 0xFF) == ord("q"):
                cv2.destroyWindow(name)
                break
