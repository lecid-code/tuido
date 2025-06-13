"""Setup script for TUIDO - Terminal-based Todo List Manager
This script uses setuptools to package the TUIDO application, including its dependencies
and entry points.
"""

from setuptools import find_packages, setup

setup(
    name="tuido",
    version="1.0.0",
    author="Ramzi Sayyid",
    author_email="code@lecid.me",
    description="A terminal-based todo list manager",
    long_description=(
        open("README.md", encoding="utf-8").read()
        if open("README.md", encoding="utf-8")
        else ""
    ),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "rich",
        "humanize",
    ],
    entry_points={
        "console_scripts": [
            "tuido=tuido.__main__:main",  # command_name=package.module:function
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
