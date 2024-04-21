## Chapter 2. Compiling and Running Cython


### The Cython Compilation Pipeline

Two stages:

- First stage handled by the `cython` compiler, transforms Cython source into optimised, platform-independent C, C++
    - Managed by `cythonize`

- Second stage compiles C, C++ into a shared library, using a standard C, C++ compiler (.so, Unix, .pyd extension on Windows)
    - Full-fledged Python module, named _extension module_
    - Managed by `distutils`