''' setup script '''
from distutils.core import setup

setup(
    name='WordBuilder',
    version='0.1.1',
    author='Mouse Reeve',
    author_email='mouse.reeve@gmail.com',

    packages=['app'],

    include_package_data=True,

    url='https://github.com/mouse-reeve/word-builder',
)

