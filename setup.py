# setup.py

from setuptools import setup, find_packages

setup(
    name='chip',
    version='0.1',
    packages=find_packages(),
    package_data={'chip': ['config.ini']},
    entry_points={
        'console_scripts': [
            'chip=chip.main:main',
        ],
    }
)
