BUILDDIR = build

.PHONY: help

help:
	@echo "Available commands:"
	@echo "  clean     deletes build dir"
	@echo "  build     rebuilds html docs"
	@echo "  publish   pushes html docs to github pages"
	@echo "  serve     starts local HTTP server"

clean:
	/bin/rm -rf $(BUILDDIR)

build:
	mkdocs build

publish: build
	ghp-import -n -p $(BUILDDIR)

serve:
	mkdocs serve
