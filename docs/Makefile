# Makefile for Sphinx overarching documentation

# Source of truth - what is in pyproject.toml should agree
# with with this. Also floors need to be added to pyproject.toml
# after a top level release starting the next rolling release.
CURR_ROLLING_RELEASE = 6.0.0

# Put it first so that "make" without argument is like "make help".
help:
	@echo To build homepage: uv run make homepage

clean:
	rm -rf build/ source/conf.py

source/conf.py: gen_conf.py Makefile
	@./gen_conf.py $(CURR_ROLLING_RELEASE) > source/conf.py
	@echo Generated source/conf.py for current rolling release

# Build homepage
homepage: source/conf.py
	@sphinx-build -b html source build
	@echo Generated homepage for current rolling release

.PHONY: help clean homepage
