from setuptools import setup, find_packages

setup(
    name="tuido",
    version="1.0.0",
    author="Ramzi Sayyid",
    author_email="code@lecid.me",
    description="A terminal-based todo list manager",
    long_description=open("README.md").read() if open("README.md") else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "rich",
        "humanize",
    ],
    entry_points={
        "console_scripts": [
            "tuido=tuido.tuido:main",  # command_name=package.module:function
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)