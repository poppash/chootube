.PHONY: format shell test tests

format:
	poetry run black ./src ./tests && \
	poetry run isort ./src ./tests

lint:
	poetry run flake8 ./src ./tests && \
	poetry run mypy ./src ./tests

shell:
	poetry shell	

suite: format lint test

test:
	poetry run python -m pytest

tests: test # alias
