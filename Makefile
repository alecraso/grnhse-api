.DEFAULT_GOAL := build

.PHONY: venv
venv:
	python -m venv ./venv || virtualenv venv

.PHONY: build
build:
	python setup.py sdist

.PHONY: install
install:
	python setup.py install

.PHONY: clean
clean:
	find . -iname '*.pyc' -delete
