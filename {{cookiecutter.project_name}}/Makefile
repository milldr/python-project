PIPENV_PATH := $(shell command -v pipenv 2> /dev/null)
PIPENV_RUN=$(PIPENV_PATH) run
PREPEND_CMD=

PROJECT_PATH={{cookiecutter.project_name}}
TESTS_PATH=tests/unit

# Format output
GREEN=\033[0;32m
START_LINE_FMT=\n\n$(GREEN)
END_LINE_FMT=\n\n\003[0m

.PHONY: check-env test lint unittest python_format build clean

# Check for pipenv
check-env:
ifndef PIPENV_PATH
	$(error Pipenv is required.)
endif
ifndef PIPENV_ACTIVE
	PREPEND_CMD=$(PIPENV_RUN)
endif

# Run tests
test: start_message dependencies code_lint sec_lint build unit_test install

# Build package
build: check-env clean
	@printf "$(START_LINE_FMT)** Packaging dist **$(END_LINE_FMT)"
	$(PREPEND_CMD) python setup.py sdist
	$(PREPEND_CMD) python setup.py bdist_wheel

# Upload the release
install: check-env
	@printf "$(START_LINE_FMT)** Installing local package **$(END_LINE_FMT)"
	pipenv install dist/{{cookiecutter.project_name}}-*.tar.gz

# Upload to nexus
release:
	@printf "$(START_LINE_FMT)** Uploading release to Nexus **$(END_LINE_FMT)"
	@pipenv install twine
	$(PREEND_CMD) twine upload --verbose --repository-url {{cookiecutter.repository_url}} -u ${NEXUS_USER} -p ${NEXUS_PASSWORD} dist*/*

dependencies: check-env
	@printf "$(START_LINE_FMT)** Installing dev packages **$(END_LINE_FMT)"
	@pipenv install --dev

start_message: check-env
	@printf "$(GREEN)*****************************************\n"
	@printf "**            RUNNING TESTS            **\n"
	@printf "**                 GL HF               **\n"
	@printf "*****************************************$(END_LINE_FMT)"

python_format: check-env
	@printf "$(START_LINE_FMT)** Formatting with black **$(END_LINE_FMT)"
	$(PREPREND_CMD) black setup.py
	$(PREPREND_CMD) black $(PROJECT_PATH)/*.py
	$(PREPREND_CMD) black $(TESTS_PATH)/*.py

code_lint: check-env
	@printf "$(START_LINE_FMT)** Static code analysis **$(END_LINE_FMT)"
	$(PREPREND_CMD) prospector setup.py $(PROJECT_PATH)/*.py $(TESTS_PATH)/*.py

sec_lint: check-env
	@printf "$(START_LINE_FMT)** Static code analysis for security **$(END_LINE_FMT)"
	$(PREPREND_CMD) bandit -r . 

unit_test: check-env
	@printf "$(START_LINE_FMT)** Unit testing  **$(END_LINE_FMT)"
	$(PREPREND_CMD) bandit -r . 

smoke_message: 
	@printf "$(START_LINE_FMT)*************\n"
	@printf "** SMOKE TESTS **\n"
	@printf "*************$(END_LINE_FMT)"

help_test: check-env
	@printf "$(START_LINT_FMT)** Smoke test entry point **$(END_LINE_FMT)"
	$(PREPREND_CMD) {{cookiecutter.project_name}} --help

clean: check-env
	@printf "$(START_LINT_FMT)** Clean up build artifacts **$(END_LINE_FMT)"
	pipenv uninstall {{cookiecutter.project_name}}
	rm -rf build .pytest_cache .coverage dist *.egg-info .eggs

