#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Nibras Ar Rakib",
    author_email='nibras.rakib@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="One of the objectives of this project is to develop Python code that can perform various mathematical operations that are essential for deep learning. These include linear algebra, calculus, statistics, optimization, and numerical methods.",
    entry_points={
        'console_scripts': [
            'deeplearning_math=deeplearning_math.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='deeplearning_math',
    name='deeplearning_math',
    packages=find_packages(include=['deeplearning_math', 'deeplearning_math.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/nibrasrakib/deeplearning_math',
    version='0.1.0',
    zip_safe=False,
)
