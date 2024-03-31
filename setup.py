
from setuptools import setup, find_packages

setup(
    name='gradio888',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'gradio888=src.main:main',
        ],
    },
    python_requires='>=3.8',
    author='lzz',

)
