# Makefile for Sphinx overarching documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

STATICDIR     = source/_static
TEMPLATEDIR   = source/_templates

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean: Makefile
	rm -rf "$(BUILDDIR)"

setup: clean
	mkdir -p $(STATICDIR) $(TEMPLATEDIR)

.PHONY: help clean setup Makefile

# Catch-all target: route all unknown targets to Sphinx
%: setup
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
