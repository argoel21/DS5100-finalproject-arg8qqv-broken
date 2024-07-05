from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    author='Anjali Goel',
    author_email='anjali.radhika.goel@gmail.com',
    description='A package for Monte Carlo simulation',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
)