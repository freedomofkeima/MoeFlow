# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

requires = [
    'attrs==17.3.0',
]

console_scripts = [
    'app = moeflow.cmds.main:main',
]

setup(
    name='MoeFlow',
    version='0.0.1',
    author='Iskandar Setiadi',
    author_email='iskandarsetiadi@gmail.com',
    url='https://github.com/freedomofkeima/MoeFlow',
    description='Anime characters recognition website, powered by TensorFlow',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src'
    },
    install_requires=requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Environment :: Web Environment"
    ],
    entry_points={'console_scripts': console_scripts},
    extras_require={
        'tests': ['pytest', 'pytest-cov', 'pytest-sugar']
    },
    zip_safe=False
)
