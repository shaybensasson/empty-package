from setuptools import find_packages, setup

setup(
    name="empty-package",
    author="Neurohelp",
    author_email="neurohelp@neuro-help.com",
    description="A simple package for testing console scripts.",
    version="1.0.1",  # type: ignore
    packages=find_packages(),
    entry_points={"console_scripts": ["empty-package = empty_package.program:main"]},
    extras_require={"dev": ["pre-commit"]},
)
