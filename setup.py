import setuptools
from distutils.core import Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mutable_int-hevangel", # Replace with your own username
    version="0.0.3",
    author="Horace Chan",
    author_email="git@horace.org",
    description="Mutable Integer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hevangel/mutable_int",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    ext_modules = [Extension('mutable_int_utils', ['mutable_int_utils.c'])]
)
