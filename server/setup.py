from setuptools import setup, find_packages

f = open('requirements.txt', 'r')

requires = f.read().split('\n')

f.close()

setup(name='api',
      version='0.1',
      description='',
      install_requires=requires,
      packages=find_packages(),
      include_package_data=True,
      author='',
      author_email='',
      url='',
     )
