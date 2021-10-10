from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="pyunit",
    version="1.5",
    packages=find_packages(),
    author="tomoki1",
    url="https://github.com/tomoki171923/python-util",
    description="python utility code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=_requires_from_file("requirements.txt"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)
