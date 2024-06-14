import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Fruits-Classification-Project"
SRC_REPO = "fruitsClassifier"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
