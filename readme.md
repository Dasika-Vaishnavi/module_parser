# steps to start a venv

* run - python -m venv myenv
* then - myenv\Scripts\activate
* install packages

# steps to use wsl cli

* start

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

* add in encryptor

import click

@click.command()
def cli():
    # Your code here

* install editable
pip install --editable .

* command to start 

encryption.

# create linux pkg

   pip install pyinstaller
      pyinstaller --onefile encryption.py
      pyinstaller --onefile encryptor_exe.py
         ./dist/encryption
-----
pip install cython
pip install setuptools    
python setup.py install   

First, you need to create a setup.py file in the module_parser directory. This file will use the setuptools and Cython.Build modules to compile the Python files. Here's an example of what the setup.py file could look like:
In this file, cythonize("*.py") tells Cython to compile all .py files in the current directory.
Once you have the setup.py file, you can run it with this command:
This command tells Python to run the setup.py file, which will compile all the .py files in the current directory. The build_ext command is used to build the extension modules described by the setup.py file, and the --inplace option tells it to put the output files in the current directory, instead of the usual build location.
After running this command, you should see .pyd files (on Windows) or .so files (on Unix-based systems) in the module_parser directory. These are the compiled versions of your Python files.
Please note that you need to have Cython installed to do this. If you don't have it installed, you can install it with pip install cython.

#### extract C code 
mkdir new_folder
find . -name "*.c" -exec cp {} new_folder \;

To compile Python code to C code using Cython and then convert the C code to a static library, follow these detailed steps. This process involves first creating a Cython file from your Python code, compiling this Cython code into C code, and finally, compiling the C code into a static library.

Step 1: Install Cython
First, make sure Cython is installed in your environment:

sh
Copy code
pip install cython
Step 2: Prepare Your Python Code
Create your Python code that you wish to compile. For example, you might have a file named example.pyx (the .pyx extension is commonly used for Cython files to differentiate them from pure Python .py files):

python
Copy code
# example.pyx
def hello_world():
    print("Hello, World!")
Step 3: Write a Cython setup.py File
Create a setup.py file in the same directory as your .pyx file. This script tells Cython how to compile your code:

python
Copy code
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("example.pyx", build_dir="build"),
    script_args=['build_ext', '--inplace']
)
Step 4: Compile the Cython Code to C
Run the setup.py script with Python. This will compile your Cython file (example.pyx) into a C file (example.c):

sh
Copy code
python setup.py
After running this, you'll have a C source file named example.c in your directory.

Step 5: Compile the C Code to a Static Library
The next step is to compile this C code into a static library file (.a for Unix-like systems, .lib for Windows). The exact command depends on your system and the compiler you are using.

On Unix-like Systems (using gcc):
sh
Copy code
gcc -c example.c -o example.o
ar rcs libexample.a example.o
This compiles the C code into an object file (example.o) and then creates a static library (libexample.a) from the object file.

On Windows (using cl from Visual Studio):
First, compile the C code to an object file:

cmd
Copy code
cl /c example.c
Then, use the lib tool to create a static library:

cmd
Copy code
lib example.obj -OUT:example.lib
Notes:
The .pyx file is a Cython file that can contain both standard Python code and Cython-specific enhancements.
The setup.py script uses Cython to compile the .pyx file into a .c file, which can then be compiled into an object file and finally into a static library.
The resulting static library (libexample.a or example.lib) can be linked with other C/C++ programs. However, remember that to use functionalities from Python/Cython in your C/C++ programs, you'll need to properly initialize the Python interpreter within those programs.

python setup.py install
python setup.py build
