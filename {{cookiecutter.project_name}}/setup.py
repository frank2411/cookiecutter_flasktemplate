import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="{{cookiecutter.project_name}}",
    version="0.1",
    author="Francesco Perna",
    description="{{cookiecutter.long_project_name}} API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.project_repository_url}}",
    python_requires=">=3.6",
    package_dir={"{{cookiecutter.project_name}}": "{{cookiecutter.project_name}}_api"},
    packages=setuptools.find_packages(exclude=["tests", "migrations"]),
    install_requires=requirements,
)
