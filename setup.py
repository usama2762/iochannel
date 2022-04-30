from setuptools import setup

from io_channel import __version__

setup(
    name='io_channel',
    version=__version__,

    url='https://github.com/aixplain/io_channel',
    author='Usama Jamil',
    author_email='usamajamil77@gmail.com',

    py_modules=['io_channel'],
    install_requires=[
        'boto3'
    ],
)
