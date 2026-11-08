# Makefile for Sphinx overarching documentation

# Source of truth - what is in pyproject.toml should agree
# with with this. Also floors need to be added to pyproject.toml
# after a top level release starting the next rolling release.
CURR_ROLLING_RELEASE = 6.0.0

SPHINXBUILD = sphinx-build

# Give build info if "make" without arguments is given
help:
	@echo To build homepage: uv run make homepage

clean:
	rm -rf build/ source/conf.py

source/conf.py: gen_conf.py Makefile
	@./gen_conf.py $(CURR_ROLLING_RELEASE) > source/conf.py
@echo Generated sour:qce/conf.py for current rolling release.

homepage: source/conf.py
	@command -v $(SPHINXBUILD) >/dev/null 2>&1 || { \
	    echo 'Error: $(SPHINXBUILD) not found.'; echo; \
	    $(MAKE) --no-print-directory help; exit 1; }
	@$(SPHINXBUILD) -b html source build
	@echo Generated homepage for current rolling release.

.PHONY: help clean homepage
