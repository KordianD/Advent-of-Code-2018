all: clean test

fix:
	autopep8 solutions --recursive --in-place
	autopep8 tests --recursive --in-place

test:
	pytest -vv
	py.test --cov  solutions tests --cov-report term-missing
	flake8 solutions test --max-line-length 120
	pylint --rcfile=standard.rc --disable=missing-docstring solutions tests
	pyflakes .

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

.PHONY: clean test