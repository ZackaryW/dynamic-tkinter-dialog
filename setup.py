from setuptools import setup, find_packages

setup(
    name='dynTinkDialog',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A dynamic tkinter dialog',
    long_description=open('README.md').read(),
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
            'dynlog=dynTinkDialog.__init__:main',
        ],
    },  
    author='Zackary W'
)