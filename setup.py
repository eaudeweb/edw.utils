from setuptools import setup


version = __import__('edw.utils', fromlist=['__version__']).__version__

setup(
    name='edw.utils',
    version=version,
    url='https://github.com/eaudeweb/edw.utils',
    license='Apache',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=['edw.utils'],
    # this is unnecessary, because Python3-only
    #namespace_packages=['edw'],
)
