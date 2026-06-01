#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevForge-CLI 安装配置
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="devforge-cli",
    version="1.0.0",
    author="DevForge Team",
    author_email="dev@devforge.example.com",
    description="A Swiss Army Knife for Developers - Zero Dependencies, Offline, Privacy-First",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/DevForge-CLI",
    project_urls={
        "Bug Reports": "https://github.com/gitstq/DevForge-CLI/issues",
        "Source": "https://github.com/gitstq/DevForge-CLI",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
    ],
    keywords="cli developer-tools utility swiss-army-knife offline zero-dependency",
    package_dir={"": "."},
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "devforge=devforge:main",
        ],
    },
    include_package_data=True,
)
