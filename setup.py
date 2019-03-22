from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Maphefo/mypackage',
    author='Mmaphefo Seseni',
    author_email='michel.seseni@gmail.com'
)
