import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

requires = []

tests_require = ["pytest", "pycov", "mypy"]

dev_require = ["flake8", "black"]

setup(
    name="TradingDataProvider",
    version="0.1.0",
    description="Get trading data",
    packages=["trading_data_provider"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extra_requires={"test": tests_require, "dev": dev_require},
)
