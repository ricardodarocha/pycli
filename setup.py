from setuptools import setup

setup(
    name = 'pycli',
    version = '0.1.0',
    description = 'teste',
    packages=['pycli'],
    entry_points = {
        'console_scripts': [
            'pycli = pycli.__main__:main']
    }
    
    
    
)