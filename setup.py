"""
Setup script for the NASA Universal API Tool.

This script installs the NASA Universal API Tool package.
"""

from setuptools import setup, find_packages

setup(
    name="nasa_api_tool",
    version="0.1.0",
    description="A comprehensive Python library for accessing NASA's APIs through a unified interface",
    author="NASA API Tool Team",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    python_requires=">=3.6",
)
