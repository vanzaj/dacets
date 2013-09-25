from distutils.core import setup

from dacets import (__title__, __version__, __author__, __license__)

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email='vanzaj@gmail.com',
    packages=['dacets', 'dacets.tests'],
    scripts=['bin/dct'],
    url='http://dacets.net/',
    license=__license__,
    description='facets of (research) datasets',
    long_description=open('README.md').read(),
    keywords = ['scientific data management', 'electronic data capture'],
    classifier = [
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'Topic :: Science/Research :: Data Management',
            'License :: OSI Approved :: BSD License',
        ],
    install_requires=[
        'Sphinx >= 1.1.3',
        'PyYAML >= 3.10',
    ],
)