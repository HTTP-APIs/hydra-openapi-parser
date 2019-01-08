#!/usr/bin/env python
"""Setup script for Python Hydra Agent."""

from setuptools import setup

setup(name='hydra-openapi-parser',
      include_package_data=True,
      version='0.0.1',
      description='A Hydra agent using Python and Redis',
      author='W3C HYDRA development group',
      author_email='public-hydra@w3.org',
      url='https://github.com/HTTP-APIs/hydra-openapi-parser',
      python_requires='>=3',
      packages=find_packages(
          exclude=['hydra','examples','test*','python_whihydra_agent.egg-info']),
      package_dir={'hydra_parser':
                   'hydra_parser'},
)