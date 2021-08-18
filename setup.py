from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Reader Writer Lock'

# Setting up
setup(
    name="reader_writer_locks",
    version=VERSION,
    author="Viet Le",
    author_email="minhviet810business@gmail.com",
    license='MIT',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['concurrency', 'multithreading', 'multiprocessing'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)