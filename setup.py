from setuptools import setup

setup(
    name='dahdipdk',
    version='0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'dahdi-run=main:tes',
        ],
    },
)
