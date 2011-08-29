import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

import import_utils

setup(
    name = "import-utils",
    version = import_utils.__version__,
    description = 'A module that supports simple programmatic module imports',
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    license = 'BSD',
    keywords = 'import, module',
    url = 'http://askbot.org',
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    long_description = import_utils.__doc__
)
