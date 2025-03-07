#!/usr/bin/env python

import os
import subprocess
import sys

from setuptools.command.develop import develop
from setuptools.command.install import install


def _install_playwright_dependencies():
    """Install Playwright browsers and system dependencies."""
    print("Installing Playwright browsers...")
    subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

    print("Installing Playwright system dependencies...")
    subprocess.run([sys.executable, "-m", "playwright", "install-deps"], check=True)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        try:
            _install_playwright_dependencies()
        except Exception as e:
            print(f"Error during Playwright setup: {e}", file=sys.stderr)
            print(
                "You may need to run 'playwright install' and 'playwright install-deps' manually after installation"
            )


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        develop.run(self)
        try:
            _install_playwright_dependencies()
        except Exception as e:
            print(f"Error during Playwright setup: {e}", file=sys.stderr)
            print(
                "You may need to run 'playwright install' and 'playwright install-deps' manually after installation"
            )