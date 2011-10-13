all: html
	sed -i -e 's/_static/static/g' _build/html/*.html
	cp -r _build/html/* ../../repo_index
	rm -rf ../../repo_index/static
	mv ../../repo_index/_static ../../repo_index/static

SPHINX_PROJECT_NAME=XCore Open Source Repository Index
VERSION=0
XDOC_DIR ?= ../../../xdoc
include $(XDOC_DIR)/Makefile.inc
