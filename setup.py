import os
import site
import sys
from distutils.sysconfig import get_python_lib

from setuptools import setup

setup(name='azuredevops',
    version='1.0',
    packages=['.utils', '.utils.spark_utils'])

