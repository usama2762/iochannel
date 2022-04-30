from setuptools import setup

from iochannel import __version__

setup(
    name='iochannel',
    version=__version__,

    url='https://github.com/aixplain/iochannel',
    author='Usama Jamil',
    author_email='usamajamil77@gmail.com',

    py_modules=['iochannel'],
    install_requires=[
        'boto3'
    ],
)
