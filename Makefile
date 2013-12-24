default: test

detox-test:
	detox

travis-test: test

test: env
	.env/bin/nosetests -w tests

coverage-test: env
	.env/bin/coverage run .env/bin/nosetests -w tests

env: .env/.up-to-date

.env/.up-to-date: setup.py Makefile
	virtualenv .env
	.env/bin/pip install -e .
	.env/bin/pip install Sphinx==1.1.3 releases nose
	touch .env/.up-to-date

doc: env
	.env/bin/python setup.py build_sphinx

.PHONY: doc

