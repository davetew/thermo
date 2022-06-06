from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='thermoUtils',
    url='https://github.com/davetew/thermo',
    author='David Tew',
    author_email='davetew@alum.it.edy',
    # Needed to actually package something
    packages=['thermoUtils'],
    # Needed for dependencies
    install_requires=['cantera', 'numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Miscellaneous thermodynamic analysis utilities',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
