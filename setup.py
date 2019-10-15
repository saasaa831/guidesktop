# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='guiautomation',
    version='1.0',
    description='GUIAutomation for Windows',
    license='Apache 2.0',
    author='SaaSaa',
    author_email='saasaa831@gmail.com',
    keywords="windows gui automation",
    url='https://github.com/saasaa/GUIAutomation-for-Windows',
    platforms='Windows Only',
    packages=find_packages(),
    include_package_data=True,
    long_description='GUIAutomation for Windows. Supports Python3.4+, x86, x64',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'typing','comtypes>=1.1.7','pyautogui','psutil','Appium-Python-Client',
        ]
)

