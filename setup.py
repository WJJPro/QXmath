from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension

ext_modules = cythonize(['pyqxmath.pyx'])
setup(ext_modules=ext_modules)