from setuptools import setup, find_packages

setup(
    name='InstaAPIX',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Destroyer Man',
    author_email='inquiry@destructioner.xyz',
    description='An API designed to do practically anything a normal user can do on Instagram but with more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cookie-rookie/InstaAPIX', 
)
