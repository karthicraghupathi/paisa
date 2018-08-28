from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='paisa',
    version='0.0.1',
    description='A simple abstracted omni-processor payment library in python.',
    long_description=readme,
    author='Karthic Raghupathi',
    author_email='karthicr@gmail.com',
    url='https://github.com/karthicraghupathi/paisa',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
