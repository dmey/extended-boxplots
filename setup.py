# Extended BoxPlots (https://github.com/dmey/extended-boxplots)
# Copyright 2018 D. Meyer. Licensed under MIT.

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Extended-BoxPlots',
    packages=['extended_boxplots'],
    version='0.1.0',
    license='MIT',
    description='Generator of extended box plots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='dmey',
    author_email='dmey@users.noreply.github.com',
    url='https://github.com/dmey/extended-boxplots',
    keywords=['graph', 'plottings', 'statistics'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    platforms=['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    python_requires='>=3.5',
)
