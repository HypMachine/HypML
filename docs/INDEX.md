# HypML: Hypothesis Markup Language

HypML is an open standard for specifying a machine learning task (a *hyp*othesis). Using a .hypml document, you can separate the tasks of algorithmic design and implementation.

You can read more about the project [here](../README.md).

## Basic Structure

HypML has three required sections:

- [task](#task)
- [target](#target)
- [features](#features)

Here's a simple example:

	task: classification
	
	target:
	  Positive class label: 1
	  Negative class label: 0
	
	features:
	  Feature 1:
	    type: float
	  Feature 2:
	    type: bool
	  Feature 3:
	    type: float

You can also extend your HypML document with these optional sections:

- [meta](#meta)
- [metrics](#metrics)

### Comments

	# Comments are cool too!

You can indicate a line in your HypML document is a comment by starting it with the `#` character. You can use comments to include additional information for anyone reading your HypML document, however these lines will be ignored during processing. 

## Sections

### task

This section specifies details of the machine learning task to be implemented.

#### Classification

	task: classification

Specifies your hypothesis as a classification task. This means your [target](#target) will need to include at least two class labels.

#### Regression

	task: regression

Specifies your hypothesis as a regression task. This means your [target](#target) will need be a single continuous number.

### target

TODO

### features

	features:
	  Name of Feature 1:
	    type: Type of Feature 1
	  Name of Feature 2:
	    type: Type of Feature 2

Here you can represent each of your features by name and indicate the type of the feature.

You must specify at least 1 feature, and you must specify the type of each.

Available types:

- integer `1, -2, 300, 42131, -10`
- float `1.001, -2.23, 400123.2393, -0.0001`
- bool `1, 0, True, False`
- string `a, b, c, d` (assumed as categorical text)
- text `aaa aaa aaa, bb bbbb bbbbb, c ccc cc` (assumed free-text)

### meta

	meta:
	  title: Idea v1
	  version: 1
	  author: Blair Hudson
	  date: 20181105
	  description: My awesome hypothesis 


If you include the meta section, you must include at least a title.

Available meta properties:

- title `Short hypothesis name`
- version `1, 2, 3.0, 3.2` (any integer or float)
- author `Your name`
- date `20180101` (YYYYMMDD)
- description `Longer format description of what your hypothesis is about`

### metrics

	metrics:
	  metric 1:
	    min: 0.9
	  metric 2:
	    max: 0.2
	  metric 3:
	    min: 0.4
	    max: 0.6
	  metric 4

You can include any number of metrics, specifying a minimum, maximum or both minimum and maximum values to be expected, or neither if the metric is simply for information.

Available metrics:

- accuracy
- auc