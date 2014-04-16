#!/usr/bin/env python

from setuptools import setup
from diff_cover import VERSION, DESCRIPTION

REQUIREMENTS = [line.strip() for line in
                open("requirements.txt").readlines()]
# dev requirements are in a separate field, and -e should not be in them
DEPENDENCY_LINKS = [requirement[3:] for requirement in REQUIREMENTS
                    if 'http' in requirement]
REQUIREMENTS = [requirement for requirement in REQUIREMENTS
                if 'http' not in requirement]
setup(
    name='diff_cover',
    version=VERSION,
    author='edX',
    url='http://github.com/edx/diff-cover',
    description=DESCRIPTION,
    license='AGPL',
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU Affero General Public License v3',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 "Programming Language :: Python :: 3",
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Quality Assurance'],
    packages=['diff_cover'],
    package_data={'diff_cover': ['templates/*.txt', 'templates/*.html']},
    install_requires=REQUIREMENTS,
    depenency_links=DEPENDENCY_LINKS,
    entry_points={
        'console_scripts': ['diff-cover = diff_cover.tool:main',
                            'diff-quality = diff_cover.tool:main']
    }
)
