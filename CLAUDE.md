# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Sphinx documentation project for BigDataViewer Playground, a tool for handling large-scale multi-dimensional image data. The documentation is hosted on ReadTheDocs.

## Build Commands

```bash
# Install dependencies
pip install -r docs/requirements.txt

# Build HTML documentation (from docs/ directory)
cd docs
make html          # Linux/macOS
make.bat html      # Windows

# Build output goes to docs/build/html/
```

## Documentation Structure

- `docs/source/` - Documentation source files
  - `conf.py` - Sphinx configuration
  - `contents.rst` - Main table of contents (master_doc)
  - `index.rst` - Homepage content
  - Subdirectories contain topic-specific documentation (installation, opening_images, visualizing_images, processing_images)
- `docs/requirements.txt` - Python dependencies for building docs
- `.readthedocs.yaml` - ReadTheDocs build configuration

## Writing Documentation

- Both reStructuredText (`.rst`) and Markdown (`.md`) files are supported via myst_parser
- MyST extensions enabled: colon_fence, tasklist, dollarmath, html_admonition, and others (see conf.py)
- New pages must be added to the appropriate toctree in `contents.rst`
- Theme: sphinx_rtd_theme with logo-only mode