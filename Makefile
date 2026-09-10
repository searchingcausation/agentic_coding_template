# Overridable interpreter: make PYTHON=python3.12 check
PYTHON ?= python3
# Bare `make` prints the target list instead of running the first target.
.DEFAULT_GOAL := help

# Declared phony because these are command names, not files to build;
# without this, a same-named file would make them look up to date.
.PHONY: help setup lint test-fast test check

help:
	@echo "setup      Verify Python 3.11+ and the template structure"
	@echo "lint       Check harness links, adapters, Python and JSON syntax"
	@echo "test-fast  Run offline harness regression tests"
	@echo "test       Run the full current test suite"
	@echo "check      Run lint and tests (same entry point as CI)"

setup:
	$(PYTHON) agent/scripts/check_harness.py

lint:
	$(PYTHON) agent/scripts/check_harness.py

test-fast:
	$(PYTHON) -m unittest discover -s agent/tests -v

# Alias for now; add slower suites here when the project gains them.
test: test-fast

# CI runs exactly this, so a green `make check` locally means a green CI.
check: lint test
