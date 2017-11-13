# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

requires = [
    'attrs==17.3.0',
    'bleach==1.5.0',
    'enum34==1.1.6',
    'html5lib==0.9999999',
    'Markdown==2.6.9',
    'numpy==1.13.3',
    'protobuf==3.4.0',
    'six==1.11.0',
    'tensorflow==1.4.0',
    'tensorflow-tensorboard==0.4.0rc2',
    'Werkzeug==0.12.2',
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
    tests_require=['pytest', 'pytest-cov', 'pytest-sugar'],
    zip_safe=False
)
