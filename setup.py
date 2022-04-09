import re
from setuptools import setup

# README will be shown on PyPi
with open('README.md') as file:
    readme = file.read()

# Track version number
with open('poilet/__init__.py') as file:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE)

setup(
    name='poilet',
    author='timmypidashev',
    url='https://github.com/timmypidashev/poilet',
    project_urls={
        'Discussions': 'https://github.com/timmypidashev/poilet/discussions',
        'Issues': 'https://github.com/timmypidashev/poilet/issues',
    },
    version=version,
    packages=['poilet'],
    license='MIT',
    description='Python variant of The Other Implementation of figLET',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.10.4',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10'
    ]
)
