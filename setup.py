from distutils.core import setup

setup(
    name='ds18b20',
    python_requires='>=3.8',
    author='Martin Privat',
    version='0.0.1',
    packages=['ds18b20'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='read from DS18B20 one-wire temperature sensor',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial", 
    ]
)