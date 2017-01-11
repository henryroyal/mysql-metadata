from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mysql-metadata',
    version='0.0.1',
    description='a model for the mysql information_schema',
    long_description=long_description,
    url='https://github.com/henryroyal/src',
    author='Henry Royal',
    author_email='dev@hwr.io',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    keywords='mysql information_schema metadata schema query tool',
    packages=find_packages(),
    install_requires=open('requirements.txt', 'r').readlines(),
    entry_points={
        'console_scripts': [
            'runtest=script.test:main',
        ],
    }
)
