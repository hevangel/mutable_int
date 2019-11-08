from setuptools import setup, find_packages, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mutable_int-hevangel", # Replace with your own username
    version="0.0.6",
    author="Horace Chan",
    author_email="git@horace.org",
    description="Mutable Integer package",
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
    ext_modules = [Extension('_mutable_int', ['_mutable_int.c'])]
)
