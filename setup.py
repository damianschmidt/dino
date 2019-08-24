from setuptools import setup, find_packages

setup(
    name='dino',
    packages=find_packages(),
    install_requires=[
        'pygame', 'graphviz', 'matplotlib', 'numpy', 'neat-python'
    ],
)