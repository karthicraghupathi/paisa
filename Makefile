init:
	pyenv local paisa
	pip install --upgrade pip

requirements:
	pip install -r requirements.txt

test:
	python tests/test_basic.py

.PHONY: init requirements test
