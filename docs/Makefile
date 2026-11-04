# Makefile for Sphinx overarching documentation

# Next two are the source of truth - what is in pyproject.toml
# should agree with first two and one of the last two.
PREV_ROLLING_RELEASE = 5.1.0
CURR_ROLLING_RELEASE = 6.0.0

# Put it first so that "make" without argument is like "make help".
help:
	@echo To build homepage: uv run make homepage

clean:
	rm -rf build/ source/conf.py

setup:
	@echo Setting up for homepage build

source/conf.py: gen_conf.py Makefile
	@./gen_conf.py $(CURR_ROLLING_RELEASE) > source/conf.py
	@echo Generated source/conf.py for current rolling release

# Build homepage
homepage: source/conf.py
	@sphinx-build -b html source build
	@echo Generated homepage for current rolling release

.PHONY: help clean setup 
