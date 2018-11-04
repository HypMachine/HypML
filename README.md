# HypML: Hypothesis Markup Language

HypML is an open standard for specifying a machine learning task (a *hyp*othesis). Using a .hypml document, you can separate the tasks of algorithmic design and implementation.

## What is a .hypml file?

A `.hypml` specifies all of the things you need to know about a machine learning task prior to implementation. Currently, this includes the type of task (such as classification), the target (including descriptive information about the labels), and the features used as input.

## What does a .hypml file look like?

HypML is a human-readable plain-text file, which is based on  [YAML](https://en.wikipedia.org/wiki/YAML)with a strict set of validation rules to keep the correct format.


## How do I write a .hypml file?

Further documentation about the structure and options available of .hypml is coming soon!


## Working for .hypml files in Python

The `hypml` Python package is a utility for loading and validating .hypml files.

### Installing from GitHub

While HypML is still under development, you can install it directly using the following command:

	pip install git+https://github.com/HypMachine/HypML.git#subdirectory=python

### Usage

You can view a Jupyter notebook demonstrating basic usage of `hypml` [here](https://github.com/HypMachine/HypML/blob/master/python/Basic%20Usage.ipynb).