all: html
	sed -i -e 's/_static/static/g' _build/html/*.html
	cp -r _build/html/* ../community_doc
	rm -rf ../community_doc/static
	mv ../community_doc/_static ../community_doc/static

SPHINX_PROJECT_NAME=XCore Community Documentation
VERSION=0.1
DOXYGEN_DIRS=
SOURCE_INCLUDE_DIRS=
XDOC_DIR ?= ../../xdoc
include $(XDOC_DIR)/Makefile.inc
