#!/usr/bin/env python3

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

cyalign_ext=Extension('eflomal', ['python/eflomal/eflomal.pyx'],
                      include_dirs=[numpy.get_include()])

setup(
    name='eflomal',
    version='0.1.5',
    author='Robert Östling',
    url='https://github.com/robertostling/eflomal',
    license='GNU GPLv3',
    install_requires=['numpy', 'Cython'],
    ext_modules=cythonize(cyalign_ext, language_level="3"),
    scripts=['align.py', 'makepriors.py', 'mergefiles.py']
)

