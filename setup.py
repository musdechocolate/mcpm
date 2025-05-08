import os
import sqlite3
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name="mcpm",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mcpm=mcpm.cli:main", 
        ],
    },
    install_requires=[
        # Add your dependencies here
    ],
    description="Command-line tool for managing Model Context Protocols (MCPs).",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mcpm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)