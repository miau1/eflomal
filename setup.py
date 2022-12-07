#!/usr/bin/env python3

from setuptools import setup, Extension
from setuptools.command.install import install
import subprocess
from Cython.Build import cythonize
import numpy


def compile_and_install_software():
    subprocess.check_call('make eflomal', shell=True)
    subprocess.check_call('make python-install', shell=True)


class CustomInstall(install):
    """Custom handler for the 'install' command."""
    def run(self):
        compile_and_install_software()
        super().run()


cyalign_ext=Extension('eflomal.cython', ['python/eflomal/eflomal.pyx'],
                      include_dirs=[numpy.get_include()])

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='eflomal',
    version='0.1',
    author='Robert Östling',
    url='https://github.com/robertostling/eflomal',
    license='GNU GPLv3',
    description='pip installable eflomal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'Cython'],
    ext_modules=cythonize(cyalign_ext, language_level='3'),
    package_data={
        'eflomal':['bin/eflomal']
    },
    packages=['eflomal'],
    package_dir = {'': 'python'},
    scripts=['align.py', 'makepriors.py', 'mergefiles.py'],
    cmdclass={'install': CustomInstall}
)
