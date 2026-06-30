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

## Deployment (ReadTheDocs)

- **Repo home**: `unige-biochem/bigdataviewer-playground-documentation` (public). `origin` points here.
- **Hosting**: ReadTheDocs **Community** (free tier — correct for public OSS docs). Integration is via the
  RTD **GitHub App** installed on the `unige-biochem` org, *not* a classic per-repo webhook — so
  `gh api repos/.../hooks` returns `[]` even though auto-builds work. Pushes to `main` trigger rebuilds.
- **Published URLs**:
  - `https://bigdataviewer-playground-documentation.readthedocs.io/en/latest/` — tracks `main` (living docs)
  - `https://bigdataviewer-playground-documentation.readthedocs.io/en/stable/` — tracks the highest version tag
- **Build env**: `ubuntu-22.04` / Python 3.10 (see `.readthedocs.yaml`). RTD installs **only**
  `docs/requirements.txt` — it does *not* see your local conda env.

### Critical: keep `docs/requirements.txt` in sync with `conf.py` extensions

Every extension listed in `conf.py`'s `extensions` (and anything `myst_enable_extensions` needs) must have
its pip package in `docs/requirements.txt`, or the RTD build fails with `Could not import extension ...`.
This bit us once: `sphinx_design` was enabled in `conf.py` but missing from `requirements.txt`.
When adding an extension, add the package in the same commit.

### Versioning / tagging scheme

- Tag format is **PEP 440 4-segment**: `MAJOR.MINOR.PATCH.DOC` (e.g. `0.20.4.0`, `0.20.4.1`).
  The first three digits mirror the documented `bigdataviewer-biop-tools` release; the 4th is the
  doc-only revision. (Avoid `0.20.4-doc.N` — sorts as a *pre-release*, before `0.20.4`; avoid
  `0.20.4+doc.N` — build metadata has undefined ordering. Both break RTD `stable` detection.)
- `latest` auto-tracks `main`, so doc fixes publish on every push — a tag is only for a frozen snapshot.
- New tags must be **activated once** in the RTD admin (Versions tab) before they build/appear.
- **When upstream bumps** (e.g. to 0.20.5): update `version`/`release` and the `extlinks` version strings
  in `conf.py`, then tag `0.20.5.0`.

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

## Looking Up Command Signatures for Scripting Tabs

When adding multi-language tabs to a documentation page, you need the **full Java class name**
and **parameter names** for every command. Both are stored in the pre-computed JSON snapshots:

- `cli-outputs/0.20.4/snapshot-sc.fiji.bdvpg.json` — core BDV Playground commands (`sc.fiji.bdvpg.*`)
- `cli-outputs/0.20.4/snapshot-ch.epfl.biop.json` — BIOP-specific commands (`ch.epfl.biop.*`)

### JSON structure

Each entry in those files is a command descriptor with at minimum:
- `"className"` — the full Java class name to use in `import` / `cs.run(...)`
- `"inputs"` — list of parameter objects, each with a `"name"` field (the string key for `cs.run`)

### Efficient lookup procedure

**Do this in a single batch, not command by command:**

1. Read the `.md` file and compile the complete list of all command labels on the page.
2. Launch **one** Explore agent with the full list, instructing it to search both JSON files and
   return the class name + list of input `name` fields for every command. Example prompt shape:

   > Search `cli-outputs/0.20.4/snapshot-sc.fiji.bdvpg.json` and
   > `cli-outputs/0.20.4/snapshot-ch.epfl.biop.json`. For each of the following commands,
   > return the full `className` and all input `name` fields:
   > 1. BDV - Show Sources
   > 2. Source - Set Color
   > …

3. Use the agent's single response to write all four-tab blocks in one pass over the file.

This one-agent-one-pass approach avoids repeated individual searches and keeps the main
context clean.

## Existing Documentation Pages

Some pages have been carried over from a previous documentation effort. These are generally
still accurate in content, **but command names may have changed** and should be verified
against the current CLI tool output before being considered final.

## Demo Examples

`ijp-imglib2bdvdemo-ij2/` contains technical demos. The pixel classifier demo is the
current starting point for new documentation pages. `DemoHelper` includes screenshot
functionality that can be used to generate documentation images programmatically.

## Generating Screenshots for Documentation Pages

Screenshots are generated by Java `main()` classes in `ijp-imglib2bdvdemo-ij2/src/test/java/ch/epfl/biop/docs/`.
One class per documentation page, named `Generate<PageName>Screenshots.java`.
The completed example is `GenerateVisualizingImagesScreenshots.java` for `visualizing_images.md`.

### How it works

1. The class starts a full Fiji/ImageJ2 context (`DemoHelper.startFiji`), loads the LLS7 HeLa dataset
   (`DemoDatasetHelper.DemoDataset.LATTICE_HELA_SKEWED`), and runs through a sequence of scenarios —
   one per screenshot needed.
2. Each scenario: open the relevant BDV/BVV window via `CommandService`, set an explicit window title
   via `BdvHandleHelper.getJFrame(handle).setTitle(...)` on the EDT, then call `DemoHelper.shot()`.
3. Screenshots are saved as `{prefix}_{WindowTitle}.png` in `docs/source/<section>/images/`.
4. After each shot, dispose the window and call `DemoHelper.waitFor(500)` to let Swing fully clean up
   before the next scenario.

### Key conventions

- **Pause before each shot** — call `DemoHelper.pause("Scenario N – description\nAdjust if needed, then click Continue.")` immediately before every `DemoHelper.shot()`. This lets you tweak the view interactively before the screenshot is taken, without changing any code.
- **Always set the window title explicitly** (`SwingUtilities.invokeAndWait` + `setTitle`) before
  `DemoHelper.shot()`. BDV internally appends numbers like `[00]` to window titles, which produces
  unpredictable filenames. Setting the title yourself gives stable, predictable output filenames.
- **Adjust view on `sources[0]` only** — `new ViewerTransformAdjuster(handle, sources[0]).run()` —
  not on all sources. This gives a better framing for the LLS7 dataset.
- **Filter by title in `DemoHelper.shot()`** to avoid capturing unrelated windows (Fiji toolbar, etc.).
  Use a shared prefix like `"BigDataViewer-"` to capture a group, or an exact title to capture one.
- **One image per screenshot in the md**, placed immediately after the relevant parameter table.
  Reference images as `![alt text](images/filename.png)` (relative path).
- **Images directory**: `docs/source/<section>/images/` — create it before running if it doesn't exist.

### Output directory

The class reads the output path from the system property `doc.output.dir`, defaulting to
`../bigdataviewer-playground-documentation/docs/source/<section>/images` (works when both repos
are siblings on disk). Override with `-Ddoc.output.dir=/absolute/path` in VM options if needed.

### Running the class

Run directly from the IDE: right-click the class → *Run 'Generate...Screenshots.main()'*.
No Maven test harness needed — these are plain `main()` methods, following the same convention
as `SimpleIJLaunch.java` and other test utilities in the project.

### Adding a new page — checklist

1. Create `docs/source/<section>/images/` in this repo.
2. Create `Generate<PageName>Screenshots.java` in `ijp-imglib2bdvdemo-ij2/src/test/java/ch/epfl/biop/docs/`,
   modelled on `GenerateVisualizingImagesScreenshots.java`.
3. Look up the exact class names of the commands to invoke from
   `cli-outputs/0.20.4/snapshot-sc.fiji.bdvpg.json` and `snapshot-ch.epfl.biop.json`.
4. For each scenario: run the command via `ij.command().run(...)`, set window title, call
   `DemoHelper.shot(OUTPUT_DIR, "prefix", waitMs, "TitleFilter")`, then dispose + wait.
5. Run the class from the IDE to generate the images.
6. Add `![alt text](images/filename.png)` references in the `.md` file at the appropriate locations.

## Sphinx Extensions in Use

- **sphinx-design** is installed and enabled. Use it for layout features.
- **sphinx_copybutton** adds copy buttons to all code blocks automatically.

### Image grids (sphinx-design)

Use `{grid}` for multi-image layouts (e.g. orthogonal views). Always use one extra colon
level on the outer directive compared to its children:

```
::::{grid} 2
:::{grid-item}
![label](images/file.png)
:::
:::{grid-item}
![label](images/file.png)
:::
::::
```

### Multi-language code tabs (sphinx-design)

Every command section should expose four tabs: **GUI**, **IJ Macro**, **Groovy**, **Python**.

**Structure rules:**
- The parameter table and any admonitions (tip, note, warning) go **above** the tab-set —
  they describe the command regardless of how it is called.
- The tab-set contains only the invocation itself (menu path + screenshot for GUI; script for others).
- Use `:::::`/`::::` nesting so `:::` remains free for admonitions inside tabs.
- **Multi-image grids** (e.g. orthogonal views) go **below** the tab-set, not inside the GUI tab.
  Placing `::::{grid}` inside `::::{tab-item}` causes a colon-fence conflict. Keep grids outside
  so they are always visible regardless of which tab is selected — same as the parameter table.

**Template:**

```
| Parameter | Description |
|-----------|-------------|
| ...       | ...         |

:::{tip}
...
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> ... --> Command Name`

![alt text](images/screenshot.png)
::::

::::{tab-item} IJ Macro
```ijm
run("Command Name");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import full.class.Name.Command

cs.run(Command, true,
    "sources", sources,
    "param", value
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from full.class.Name import Command

cs.run(Command, True,
    ["sources", sources,
     "param", value]
).get()
```
::::

:::::
```

**Language notes:**
- **IJ Macro**: complex object parameters (e.g. `SourceAndConverter[]`) cannot be passed
  from macro — `run("Command Name")` opens the dialog for selection.
- **Groovy**: use `imagej-groovy` as the code fence language (not `groovy`) so the custom
  `ImageJGroovyLexer` in `conf.py` handles `#@` preprocessor lines correctly.
- **Python**: standard `python` fence is fine; `#` is already a valid comment character.
- Use `#@SourceAndConverter[] sources` (and other `#@` parameters) so the Script Editor
  shows a picker when the script is run interactively.

## Writing Guidelines

- Write for bio-image analysts: assume Fiji knowledge, not Java/programming knowledge
- Use simple workflows as the primary structure: goal → steps → snippets → screenshots
- Prefer concrete examples over abstract API descriptions