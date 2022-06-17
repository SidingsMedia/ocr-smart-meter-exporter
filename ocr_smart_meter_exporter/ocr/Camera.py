# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from typing import Any

import cv2
import numpy


class Camera:
    """
    A class representing the camera to be used
    """
    def __init__(self, cam_port: int, log: Any, image_path: str = "") -> None:
        """
        __init__ Create instance of camera

        :param cam_port: Port camera is accessible on
        :type cam_port: int
        :param log: Logging instance
        :type log: Any
        :param image_path: If defined, the specified image will be used
            instead of the camera, defaults to ""
        :type image_path: str, optional
        """

        self._image: numpy.ndarray

        if image_path:
            self._use_image = True
            self._image = cv2.imread(image_path)
        else: 
            self._use_image = False
        
        if not self._use_image:
            self._camera = cv2.VideoCapture(cam_port)
            self._camera.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
            self._camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

        self._log = log

        # Make an initial capture to populate _image
        self.capture()
        

    def capture(self, show: bool = False) -> numpy.ndarray:
        """
        capture Capture image from camera

        Capture the current frame from the specified camera and return
        it. No preprocessing is completed on this image, this must be
        done after.

        :param show: Should the image be shown to the user, defaults to False
        :type show: bool, optional
        :return: Image
        :rtype: numpy.ndarray
        """

        if self._use_image:
            self._log.info("CAMERA", "Using preloaded image instead of camera")
            return self._image

        self._log.debug("CAMERA" , "Capturing image")
        result, self._image = self._camera.read()

        if result:
            if show:
                self._log.info("CAMERA", "Waiting for window to close before continuing")
                self._show("capture")
            return self._image
        else:
            self._log.warn("CAMERA", "Failed to capture image")

    def preprocess(self, show: bool = False) -> numpy.ndarray:
        """
        preprocess Preprocess image to normalize ready for processing

        Run a series of processing steps to normalize the image and
        convert to grayscale

        :param show: Should the image be shown after each step?, defaults to False
        :type show: bool, optional
        :return: Image
        :rtype: numpy.ndarray
        """

        self._log.debug("CAMERA", "Starting image preprocessing")
        
        self._image = self._toGrayscale(self._image, show)
        self._image = self._opening(self._image, show)
        canny = self._canny(self._image, show)
        
        return self._image

    def _toGrayscale(self, image: numpy.ndarray, show: bool = False) -> numpy.ndarray:
        """
        _toGrayscale Convert _image to grayscale

        :param image: Image to perform processing on
        :type image: numpy.ndarray
        :param show: Should the image be shown?, defaults to False
        :type show: bool, optional
        :return: Processed image
        :rtype: numpy.ndarray
        """

        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)

        if show:
            self._show("grayscale", image)

        return image
    
    def _opening(self, image: numpy.ndarray, show: bool = False) -> numpy.ndarray:
        """
        _opening Perform opening operation on image

        Perform an erosion operation followed by a dilation operation on
        the image

        :param image: Image to perform processing on
        :type image: numpy.ndarray
        :param show: Should the image be shown?, defaults to False
        :type show: bool, optional
        :return: Processed image
        :rtype: numpy.ndarray
        """

        kernel = numpy.ones((5,5),numpy.uint8)
        image =  cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        
        if show:
            self._show("opening", image)

        return image

    def _canny(self, image: numpy.ndarray, show: bool = False) -> numpy.ndarray:
        """
        _canny Perform canny edge detection

        Perform canny edge dectection on the image with the following
        thresholds, 24, 25

        :param image: Image to perform processing on
        :type image: numpy.ndarray
        :param show: Should the image be show, defaults to False
        :type show: bool, optional
        :return: Processed image
        :rtype: numpy.ndarray
        """

        image = cv2.Canny(image, 24, 25)

        if show:
            self._show("canny", image)

        return image

    def _show(self, name: str, image: numpy.ndarray = None) -> None:
        """
        _show Show the image using the built in browser

        To exit the user can press any key or in most cases the X button
        of the window. Note, this will block the process until the user
        exits.

        :param image: Image to perform processing on, defaults to self._image
        :type image: numpy.ndarray, optional
        :param name: Name of window
        :type name: str
        """

        if image is None:
            image = self._image

        image = cv2.resize(image, (1920, 1080))
        cv2.imshow(name, image)
        cv2.waitKey(0)
