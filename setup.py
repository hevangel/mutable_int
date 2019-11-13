from setuptools import setup, find_packages, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    #name="mutableint-hevangel", 
    name="mutableint", 
    version="0.2",
    author="Horace Chan",
    author_email="git@horace.org",
    description="Mutable Integer package, a subclass of int",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hevangel/mutable_int",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['wheel'],
    python_requires='>=3.5',
    ext_modules = [Extension('_mutableint', ['_mutableint.c'])]
)
