from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ibanity',
    version='0.0.1a1',
    description='Python wrapper for the Ibanity API',
    long_description=long_description,
    url='https://github.com/ibanity/ibanity-python',
    author='Isabel NV',
    author_email='support@ibanity.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[''],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
