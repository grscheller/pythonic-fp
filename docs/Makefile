# Makefile for Sphinx overarching documentation

# Source of truth - what is in pyproject.toml should agree
# with with this. Also floors need to be added to pyproject.toml
# after a top level release starting the next rolling release.

SPHINXOPTS ?= -W
SPHINXBUILD ?= sphinx-build

# Give build info if "make" without arguments is given
help:
	@echo To build homepage: uv run make homepage

homepage:
	@rm -rf build
	@command -v $(SPHINXBUILD) >/dev/null 2>&1 || { \
	    echo 'Error: $(SPHINXBUILD) not found.'; echo; \
	    $(MAKE) --no-print-directory help; exit 1; }
	@$(SPHINXBUILD) -b html source build $(SPHINXOPTS)

clean:
	@rm -rf build
	@echo Removed all doc build artifacts.

.PHONY: help clean homepage
