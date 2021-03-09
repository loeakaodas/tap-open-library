#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-open-library",
    version="0.1.0",
    description="Singer.io tap for extracting data from Open Library Recent Changes API",
    author="Andrey Kabanov",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_open_library"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python==5.12.0",
        "requests==2.25.1",
    ],
    entry_points="""
    [console_scripts]
    tap-open-library=tap_open_library:main
    """,
    packages=["tap_open_library"],
    package_data={
        "schemas": ["tap_open_library/schemas/*.json"]
    },
    include_package_data=True,
)
