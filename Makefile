PYTHON=python

check:
	PYTHONPATH=$(PWD) $(PYTHON) -m testtools.run txfixtures.tests.test_tachandler

