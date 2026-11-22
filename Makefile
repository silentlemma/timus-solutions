.PHONY: lint format lint-comments

PYTHON ?= python
PROBLEMS ?=
LANGUAGES ?= cpp go java python rust
JOBS ?= 2

lint:
	$(PYTHON) code_quality.py lint $(PROBLEMS) --languages $(LANGUAGES) --jobs $(JOBS)

format:
	$(PYTHON) code_quality.py format $(PROBLEMS) --languages $(LANGUAGES) --jobs $(JOBS)

lint-comments:
	$(PYTHON) code_quality.py comments $(PROBLEMS) --languages $(LANGUAGES)
