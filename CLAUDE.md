# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This repository contains **end-user documentation** for the bigdataviewer-playground ecosystem —
a set of Fiji/ImageJ2 libraries enabling lazy, tiled, and streamed processing of very large
multi-dimensional image data on limited hardware. The target audience is **bio-image analysts**
working in Fiji, not Java developers.

Two major workflows built on this ecosystem are **ABBA** and **Warpy**, but the base
functionalities are themselves undocumented and the goal of this repo is to fill that gap.

## Documentation Format and Structure

- This is a **Sphinx** project hosted on **ReadTheDocs**
- The index and toctree structure uses **reStructuredText** (`.rst`)
- Content pages are written in **Markdown** (`.md`) via myst_parser
- Browse the existing repo structure to understand the backbone before creating new files
- New pages must be added to the appropriate toctree in `index.rst` or a section's own index file

## Build Commands
```bash
# Activate the conda environment first
conda activate bdvpg-documentation

# Build (from docs/ directory)
cd docs
sphinx-build -b html source build/html
# Output: docs/build/html/
```

## Current Version

The documentation currently tracks release: `ch.epfl.biop:bigdataviewer-biop-tools:0.20.4`

## CLI Introspection Tool

A tool for introspecting the ecosystem is in `fiji-tools/`. Read that directory to understand
available subcommands before calling it. Invoked via:
```bash
jgo -r scijava=https://maven.scijava.org/content/groups/public \
  "ch.epfl.biop:fiji-tools:0.1.0-SNAPSHOT:ch.epfl.biop.fiji.tools.CLI+ch.epfl.biop:bigdataviewer-biop-tools:0.20.4" \
  <subcommand> <args..>
```

## Versioned CLI Outputs

Save CLI outputs under `cli-outputs/<version>/` (e.g. `cli-outputs/0.20.4/`).
This enables diffing outputs across versions to guide incremental documentation updates.

## Existing Documentation Pages

Some pages have been carried over from a previous documentation effort. These are generally
still accurate in content, **but command names may have changed** and should be verified
against the current CLI tool output before being considered final.

## Demo Examples

`ijp-imglib2bdvdemo-ij2/` contains technical demos. The pixel classifier demo is the
current starting point for new documentation pages. `DemoHelper` includes screenshot
functionality that can be used to generate documentation images programmatically.

## Writing Guidelines

- Write for bio-image analysts: assume Fiji knowledge, not Java/programming knowledge
- Use simple workflows as the primary structure: goal → steps → snippets → screenshots
- Prefer concrete examples over abstract API descriptions