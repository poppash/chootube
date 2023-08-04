.PHONY: test tests

shell:
	poetry shell	

test:
	poetry run python -m pytest

tests: test # alias
