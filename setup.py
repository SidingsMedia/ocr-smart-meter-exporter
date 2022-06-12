# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from setuptools import setup, find_packages

from ocr_smart_meter_exporter import __version__

setup(
    name=__version__.__title__,
    version=__version__.__version__,
    author=__version__.__author__,
    author_email=__version__.__author_email__,
    url=__version__.__url__,
    license=__version__.__license__,
    description=__version__.__description__,
    packages=find_packages(),
    scripts=[
        "run.py",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: System :: Monitoring",
        "Typing :: Typed",
    ],
)
