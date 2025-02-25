from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="aioengine-python",
    version="0.0.4",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "rich",
        "pydantic"
    ],
    description="Asynchronous engine for search engines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="stone",
    author_email="manybot.00@gmail.com",
    url="https://github.com/KissmeBro/aioengine",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)