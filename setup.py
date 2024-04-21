# On Unix
# python setup.py build_ext --inplace
# To run on Windows (Visual Studio compiler, but there can be others like --compiler=mingw32 -DMS_WIN64)
# python setup.py build_ext -i --compiler=msvc

from distutils.core import setup
from Cython.Build import cythonize

# Two stages of compilation in one line!
setup(ext_modules=cythonize('fib.pyx'))