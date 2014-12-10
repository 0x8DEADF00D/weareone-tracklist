from setuptools import setup, find_packages
import os

workingDirectory = os.path.abspath(os.path.dirname(__file__))
readmeContent = open(os.path.join(workingDirectory, 'README.md')).read()

setup(name='weareone-tracklist',
      version='0.1',
      description='Tracklist parser for WeAreOne radios written in Python',
      long_description=readmeContent + '\n\n',
      author='Mostey',
      author_email='',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests',
          'beautifulsoup4',
          'python-dateutil'
      ],
      license="MIT",
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4'
      ],
      entry_points={
          'console_scripts': [
              'acquisition=acquisition:main'
          ]
      })