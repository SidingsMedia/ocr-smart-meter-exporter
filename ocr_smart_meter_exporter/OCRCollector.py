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

        value = self._ocr.get()

        current_usage = GaugeMetricFamily("electricity_current_usage", "The current usage as read from the camera")
        current_usage.add_metric([], abs(value))

        current_import = GaugeMetricFamily("electricity_current_import", "The current import as read from the camera")
        if value >= 0:
            current_import.add_metric([], value)
        else:
            current_import.add_metric([], 0)
        
        current_export = GaugeMetricFamily("electricity_current_export", "The current export to the grid as read from the camera")
        if value <= 0:
            current_export.add_metric([], abs(value))
        else:
            current_export.add_metric([], 0)

        yield current_usage
        yield current_import
        yield current_export
