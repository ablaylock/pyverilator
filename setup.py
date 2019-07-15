# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# here = path.abspath(path.dirname(__file__))
# TODO write a readme
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name='PyVerilator',
    version='0.0.0.dev1',
    description='Python-based REPL interface for Verilator objects',
    # long_description=long_description,
    url='https://github.com/csail-csg/pyverilator',
    author='CSAIL CSG',
    author_email='acwright@mit.edu, bthom@mit.edu',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Verilator Wrapper Verilog',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    extras_require={
        'dev': [], # ['check-manifest'],
        'test': [], # ['coverage'],
    },
    entry_points={
        # If we ever want to add an executable script, this is where it goes
    },
    project_urls={
        'Bug Reports': 'https://github.com/csail-csg/pyverilator/issues',
        'Source': 'https://github.com/csail-csg/pyverilator',
    },
)