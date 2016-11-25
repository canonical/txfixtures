PYTHON=python

check:
	PYTHONPATH=$(PWD) $(PYTHON) -m testtools.run txfixtures.tests.test_tachandler

check-doc:
	$(MAKE) -C doc doctest

html:
	$(MAKE) -C doc html

.PHONY: check check-doc html
