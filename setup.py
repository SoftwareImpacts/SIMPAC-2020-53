# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='vanilla-option-pricing',
    version='0.1.0',
    description='Stochastic model for vanilla option pricing',
    python_requires='==3.*,>=3.7.0',
    project_urls={"documentation": "https://vanilla-option-pricing.readthedocs.io",
                  "homepage": "https://github.com/donlelef/vanilla-option-pricing",
                  "repository": "https://github.com/donlelef/vanilla-option-pricing"},
    author='Emanuele Fabbiani',
    author_email='donlelef@gmail.com',
    license='MIT',
    keywords='quantitative-finance option-pricing stochastic-models',
    classifiers=['Development Status :: 5 - Production/Stable', 'Intended Audience :: Education',
                 'Intended Audience :: Financial and Insurance Industry', 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent', 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8',
                 'Topic :: Scientific/Engineering :: Mathematics'],
    packages=['vanilla_option_pricing'],
    package_dir={"": "."},
    package_data={},
    install_requires=['numpy==1.*,>=1.19.2', 'pandas==1.*,>=1.1.3', 'py-lets-be-rational==1.*,>=1.0.1',
                      'py-vollib==1.*,>=1.0.1', 'scipy==1.*,>=1.5.2'],
    extras_require={
        "dev": ["appdirs==1.*,>=1.4.4", "dephell==0.*,>=0.8.3", "pytest==6.*,>=6.1.0", "pytest-cov==2.*,>=2.10.1",
                "sphinx==3.*,>=3.2.1", "sphinx-rtd-theme==0.*,>=0.5.0"]},
)