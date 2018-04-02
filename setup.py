import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-dms",
    version="0.1",
    packages=find_packages(),
    license="GPL-3.0",
    include_package_data = True,
    description="A Django templatetag for degree-minute-second notation",
    long_description=("A Django templatetag for degree-minute-second notation."
                      " It displays decimal angle values in a human readable "
                      "format in the degree-minute-second notation. It's main "
                      "purpose is to proivide human readable values for the "
                      "geographical information - longitude and latitude."),
    author="Cezar Pendarovski",
    author_email="cezarpendarovski@web.de",
    maintainer="Cezar Pendarovski",
    maintainer_email="cezarpendarovski@web.de",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
