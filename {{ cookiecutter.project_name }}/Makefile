.PHONY: clean help install lint sync test test_integration test_unit

# set default goal to 'help' so nothing runs by accident
.DEFAULT_GOAL := help

## build project into wheel and sdist
build: clean
	@echo "building distribution archives..."
	uv build
	@echo "build complete. Artifacts are in the dist/ directory"

## delete compiled Python files and caches
clean:
	@echo "Cleaning up build and cache artifacts..."
	@# 1. Combined find for bytecode and pycaches (surgical & fast)
	@find . -type f -name "*.py[co]" -delete -o -type d -name "__pycache__" -delete
	@# 2. Remove tool-specific caches and build artifacts
	@rm -rf .ruff_cache .ty_cache .pytest_cache .uv_cache .coverage dist build *.egg-info
	@echo "Clean complete."

## sync environment
install: sync
sync:
	@echo "Syncing project dependencies..."
	uv sync
	@echo "Environment ready. Use 'uv run <command>' to execute."

## lint
lint:
	uv run ruff check --fix src tests
	uv run ruff format src tests
	uv run ty check src tests

## test all
test:
	uv run pytest tests/unit/ tests/integration/

# test integration
test_integration:
	uv run pytest tests/integration/

## test unit
test_unit:
	uv run pytest tests/unit/

## show this help message
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-19s\033[0m %s\n", $$1, $$2}'
