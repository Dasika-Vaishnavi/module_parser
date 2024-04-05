from setuptools import setup

setup(
    name='encryption',
    version='0.1',
    py_modules=['encryption'],
    install_requires=[
        'cryptography',
    ],
    entry_points='''
        [console_scripts]
        aes_encryption=encryption:aes_cli
        caesar_encryption=encryption:caesar_cli
    ''',
)

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("*.py")
)