from setuptools import setup
import sys

if not sys.version_info[0] == 3 and sys.version_info[1] < 5:
    sys.exit('Python < 3.5 is not supported')

version = '0.74.1'

setup(
    name='pepper-steam',
    packages=['steampy', 'test', 'examples', ],
    version=version,
    description='A Steam lib for trade automation',
    author='Luca Ambrosini',
    author_email='luca.ambro94@gmail.com',
    license='MIT',
    url='https://github.com/Ambros94/steam',
    download_url='https://github.com/Ambros94/steam/tarball/' + version,
    keywords=['steam', 'trade', ],
    classifiers=[],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rsa"
    ],
)
