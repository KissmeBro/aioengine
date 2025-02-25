from setuptools import setup, find_packages

setup(
    name="aioengine-python",  # تغییر نام بسته
    version="0.0.1",  # نسخه بسته
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "rich",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)