# Guide 
---

## Starting a Virtual Environment in Python

1. Create the virtual environment:
   ```bash
   python -m venv myenv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source myenv/bin/activate
     ```
3. Install packages as needed using `pip install`.

## Using the WSL CLI to Create a Click Command

1. Start by creating your setup file:
   ```python
   from setuptools import setup

   setup(
       name='encryption',
       version='0.1',
       py_modules=['encryption'],
       install_requires=[
           'Click',
       ],
       entry_points='''
           [console_scripts]
           encryption=encryption:cli
       ''',
   )
   ```

2. Add an encryptor with Click:
   ```python
   import click

   @click.command()
   def cli():
       # Your code here
   ```

3. Install your package in editable mode to test changes:
   ```bash
   pip install --editable .
   ```

4. Use your command:
   ```bash
   encryption
   ```

## Creating a Linux Package with PyInstaller

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Create a single-file executable:
   ```bash
   pyinstaller --onefile encryption.py
   ```
3. Run your executable from the `dist` folder:
   ```bash
   ./dist/encryption
   ```

## Using Cython to Build C Extensions

1. Install necessary packages:
   ```bash
   pip install cython setuptools
   ```
2. Use the following `setup.py` to cythonize your Python file:
   ```python
   from distutils.core import setup
   from Cython.Build import cythonize

   setup(
       ext_modules = cythonize("path_to_your_python_file.py")
   )
   ```
3. Build your Cython extensions:
   ```bash
   python setup.py build_ext --inplace
   ```

## Extracting C Code and Compiling to a Static Library

1. Extract C code:
   ```bash
   mkdir new_folder
   find . -name "*.c" -exec cp {} new_folder \;
   ```
2. Prepare your Cython file (`example.pyx`) with your code.
3. Write a `setup.py` file for Cython compilation.
4. Compile Cython to C, and then to a static library:
   - Compile to C:
     ```bash
     python setup.py
     ```
   - On Unix-like systems, compile to a static library:
     ```bash
     gcc -c example.c -o example.o
     ar rcs libexample.a example.o
     ```
   - On Windows:
     - Compile to object file:
       ```cmd
       cl /c example.c
       ```
     - Create a static library:
       ```cmd
       lib example.obj -OUT:example.lib
       ```

5. Install your package:
   ```bash
   python setup.py install
   ```
6. Optionally, you can build your package with:
   ```bash
   python setup.py build
   ```

7. To find the Python header files (`python.h`), use:
   ```python
   import sysconfig
   print(sysconfig.get_path("include"))
   ```

This guide provides a comprehensive overview of the steps needed to set up a Python virtual environment, create a command-line interface (CLI) tool with Click, package your Python application using PyInstaller, and use Cython to compile Python code to C and then to a static library.


