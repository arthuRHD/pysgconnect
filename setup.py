from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="pysgconnect",
    version="2.2.2",
    url="https://github.com/societe-generale/pysgconnect",
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Utilities to interact with SGConnect",
    python_requires=">=3.10",
    platforms="any",
    classifiers=["Programming Language :: Python :: 3"],
)
