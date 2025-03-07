#!/usr/bin/env python

from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            "egg_info.writers": [
                "playwright_setup.txt=inspect_multi_tool._util._playwright_setup:install_playwright_dependencies",
            ],
        },
    )