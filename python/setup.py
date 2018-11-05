import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
  name = 'hypml',
  packages = packages=setuptools.find_packages(),
  version = '0.0.2',
  description = 'A utility for loading valid Hypothesis Markup Language (.hypml) documents.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Blair Hudson',
  author_email = 'blairhudson@me.com',
  url = 'https://github.com/HypMachine/HypML', 
  download_url = '',
  keywords = ['data', 'machine', 'learning', 'science', 'algorithm', 'hypml'],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ],
  include_package_data=True
)