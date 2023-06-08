import sys
from setuptools import setup, find_packages

requires = [
    'selenium',
    'argparse',
]

setup(
    name='Ghostgram',
    description=("Ghostgram automates the process of deleting all of your Instagram comments, since Instagram does not give the user the option to do this instantly."),
    version='0.1',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ghostgram=ghostgram.app:main'],
    },
    long_description=open('README.md').read(),
    keywords=['instagram', 'comments', 'deleter', 'footprint', 'selenium']
)
