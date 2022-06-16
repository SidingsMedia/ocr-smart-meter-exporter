# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from prometheus_client.core import GaugeMetricFamily

from .Logging import log
from .ocr import OCR
 
 
class OCRCollector(object):

    def __init__(self, ocr_processor: OCR) -> None:
        """
        __init__ Create instance of collector

        :param ocr_processor: Instance of OCR handler responsible for
            capturing and processing images.
        :type ocr_processor: OCR
        """
        self._ocr = ocr_processor

    def collect(self):
        """
        collect Collect method for Prometheus exporter

        :yield: Current usage guage
        :rtype: GuageMetricFamily
        """

        log.debug("OCRCollector", "Call made to exporter")

        current_usage = GaugeMetricFamily("current_usage", "The current usage as read from the camera")
        current_usage.add_metric([], self._ocr.get())

        yield current_usage
