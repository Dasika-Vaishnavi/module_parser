# steps to start a venv

* run - python -m venv myenv
* then - myenv\Scripts\activate
* install packages

# steps to use wsl cli

*start

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

*add in encryptor

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