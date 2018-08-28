init:
	pip install -r requirements.txt

test:
	python tests/test_basic.py

.PHONY: init test
