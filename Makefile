default: test

detox-test:
	detox

test: env
	.env/bin/py.test tests

coverage-test: env
	.env/bin/coverage run .env/bin/py.test -w tests

env: .env/.up-to-date

.env/.up-to-date: setup.py Makefile
	virtualenv .env
	.env/bin/pip install -e .
	.env/bin/pip install Sphinx==1.1.3 releases pytest
	touch .env/.up-to-date

doc: env
	.env/bin/python setup.py build_sphinx

.PHONY: doc

