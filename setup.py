#!/usr/bin/env python
from setuptools import setup

requires = ['mutagen']

entry_points = {
    'console_scripts': [
        'slideshow = slideshow:main',
    ]
}

#README = open('README.rst').read()
#CHANGELOG = open('docs/changelog.rst').read()

setup(
    name='slideshow',
    version='0.0.1',
    url='http://www.finklabs.org/',
    author='Mark Fink',
    author_email='mark@finklabs.de',
    description="slideshow is a tool to create a video slideshow from images.",
    #long_description=README + '\n' + CHANGELOG,
    long_description="slideshow is a tool to create a video slideshow from images.",
    packages=[],
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities'
    ],
    #test_suite='buccaneer.tests',
)
