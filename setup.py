from setuptools import setup, find_packages

setup(
    name='hydra_openapi_parser',
    version='0.2.0',
    packages=find_packages(),
    license='MIT',
    description='A Parser from OpenAPI to Hydra specs',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/HTTP-APIs/hydra-openapi-parser',
    zip_safe=False
)
