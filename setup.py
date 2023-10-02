import setuptools
import os

with open("description.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Mi_paquete',
    version='0.1.0',
    description='A compilation of Humai utility functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Sonia-deleo/Mi_paquete.git',
    license='MIT',
    packages=['Mi_paquete'],
    install_requires=['requests'],
)