# Releasing to PyPi

Increment the version in `setup.py`.

Remove the following directories:

* build/
* dist/
* \*.egg-info/

You can build the release by running:

	python setup.py sdist bdist_wheel

Check your configuration in `~/.pypirc` and then run:

	twine upload dist/*

Done! (You might like to do a GitHub Release to match the version specified.)

You can check your release by running:

	pip install --upgrade package