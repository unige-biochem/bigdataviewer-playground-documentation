# Workspace

The workspace is the central hub of BigDataViewer Playground. It keeps track of every source you have opened or created during your session and provides tools for organizing, inspecting, saving, and restoring your work.

All workspace commands are found under:

```
Menu: Plugins > BigDataViewer-Playground > Workspace
```

---

## The BDV Playground Window

The main workspace interface is a window with a **hierarchical tree view** showing all sources currently loaded in the session.

```
Menu: Plugins > BigDataViewer-Playground > Workspace > Show BDV Playground Window
```

This window is your primary way of interacting with sources outside of the viewers. Key interactions:

- **Right-click** on sources to open a contextual menu — from there you can visualize them in a BDV or BVV window, apply processing commands, export, and more
- **Double-click** on a source to center the current viewer (if one is open) on that source
- **Select multiple sources** to apply batch operations (e.g. show all selected sources in a viewer, export them together, apply the same transform)
- Organize sources into **groups** for easier management

The tree is organized hierarchically: datasets appear as top-level nodes, with individual channels, tiles, and timepoints nested below. As you process sources (fuse, classify, resample, etc.), the resulting virtual sources also appear in the tree.

:::{tip}
If you close the BDV Playground window by accident, re-open it with **Show BDV Playground Window**. Your sources are not lost — the window is just a view into the workspace, not the workspace itself.
:::

---

## Tree Organization

When working with many sources, the tree can become crowded. These commands help you organize it by creating filter and group nodes.

### Tree - Filter By Name

Adds a filter node to the tree that shows (or hides) sources matching a text pattern. Useful for quickly finding specific channels or tiles in a large dataset.

| Parameter | Description |
|-----------|-------------|
| Filter Name | Display name for this filter node in the tree |
| Name Contains | Text pattern that source names must contain to match |
| Match Case | When checked, matching is case-sensitive |
| Show Sources | When checked, shows matching sources; when unchecked, shows non-matching sources (inverted filter) |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> Tree --> Tree - Filter By Name`
::::

::::{tab-item} IJ Macro
```ijm
run("Tree - Filter By Name");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.command.workspace.FilterNodeNameAddCommand

cs.run(FilterNodeNameAddCommand, true,
    "filter_name", "My Filter",
    "string_filter", "channel",
    "match_case", false,
    "show_sources", true
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.command.workspace import FilterNodeNameAddCommand

cs.run(FilterNodeNameAddCommand, True,
    ["filter_name", "My Filter",
     "string_filter", "channel",
     "match_case", False,
     "show_sources", True]
).get()
```
::::

:::::

### Tree - Filter By Metadata

Adds a filter node that selects sources based on a metadata key-value pair. This is useful for filtering by properties you have attached with **Source - Add Metadata** (see [Source Utilities](../processing_images/source_utilities.md)).

| Parameter | Description |
|-----------|-------------|
| Name of the node | Display name for the filter node |
| Metadata Key | The metadata key to filter by |
| Value regex | Regular expression to match metadata values (`.*` matches everything) |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> Tree --> Tree - Filter By Metadata`
::::

::::{tab-item} IJ Macro
```ijm
run("Tree - Filter By Metadata");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.tree.FilterNodeMetadataAddCommand

cs.run(FilterNodeMetadataAddCommand, true,
    "group_name", "My Metadata Filter",
    "key", "class",
    "value_regex", ".*"
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.workspace.tree import FilterNodeMetadataAddCommand

cs.run(FilterNodeMetadataAddCommand, True,
    ["group_name", "My Metadata Filter",
     "key", "class",
     "value_regex", ".*"]
).get()
```
::::

:::::

### Tree - Make Global Source Group

Creates a named group node containing specific sources. Use this to manually curate a subset of sources — for example, grouping all channels of a particular region of interest.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to include in the group |
| Name of the group | Display name for the group node |
| Display Sources | When checked, shows individual sources under the group node |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> Tree --> Tree - Make Global Source Group`
::::

::::{tab-item} IJ Macro
```ijm
run("Tree - Make Global Source Group");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.tree.SourceGroupMakeCommand

cs.run(SourceGroupMakeCommand, true,
    "sources", sources,
    "group_name", "My Group",
    "display_sources", true
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.workspace.tree import SourceGroupMakeCommand

cs.run(SourceGroupMakeCommand, True,
    ["sources", sources,
     "group_name", "My Group",
     "display_sources", True]
).get()
```
::::

:::::

### Tree - Inspect Sources

Adds an inspection node for each selected source, showing details about its properties and type hierarchy. Useful for debugging or understanding what kind of source you are working with.

| Parameter | Description |
|-----------|-------------|
| Source(s) to inspect | The sources to inspect |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> Tree --> Tree - Inspect Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("Tree - Inspect Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.tree.SourceInspectCommand

cs.run(SourceInspectCommand, true,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.workspace.tree import SourceInspectCommand

cs.run(SourceInspectCommand, True,
    ["sources", sources]
).get()
```
::::

:::::

---

## State Save and Load

You can save the entire workspace state — all sources, their display settings, and their transforms — to a JSON file, and restore it later. This is different from saving a dataset XML: the state captures *everything* in the workspace, including virtual sources created by processing commands.

### State - Save

| Parameter | Description |
|-----------|-------------|
| State file (JSON) | Path to save the state file |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> State --> State - Save`
::::

::::{tab-item} IJ Macro
```ijm
run("State - Save");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.state.StateSaveCommand

cs.run(StateSaveCommand, true,
    "file", new File("/path/to/state.json")
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs
#@File file

from sc.fiji.bdvpg.command.workspace.state import StateSaveCommand

cs.run(StateSaveCommand, True,
    ["file", file]
).get()
```
::::

:::::

### State - Load

| Parameter | Description |
|-----------|-------------|
| State file (JSON) | The JSON file containing the saved state |
| Erase current state | When checked, removes all current sources before loading. When unchecked, the loaded sources are added to the existing workspace |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> State --> State - Load`
::::

::::{tab-item} IJ Macro
```ijm
run("State - Load");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.state.StateLoadCommand

cs.run(StateLoadCommand, true,
    "file", new File("/path/to/state.json"),
    "erase_previous_state", true
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs
#@File file

from sc.fiji.bdvpg.command.workspace.state import StateLoadCommand

cs.run(StateLoadCommand, True,
    ["file", file,
     "erase_previous_state", True]
).get()
```
::::

:::::

### State - Clear

Removes all sources from the workspace. Use this to start fresh.

:::{important}
**State - Clear** cannot be undone. If you have unsaved work, save the state first.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> State --> State - Clear`
::::

::::{tab-item} IJ Macro
```ijm
run("State - Clear");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.state.StateClearCommand

cs.run(StateClearCommand, true).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.workspace.state import StateClearCommand

cs.run(StateClearCommand, True, []).get()
```
::::

:::::

:::{tip}
**State vs. Dataset XML** — what's the difference?

- A **Dataset XML** file stores the recipe for reading raw data plus spatial transforms. It is format-specific and can be shared with collaborators.
- A **State JSON** file captures the full workspace snapshot: all sources (including virtual/processed ones), display settings, and viewer configurations. It is session-specific and primarily useful for resuming your own work.

Use Dataset XML for archiving and sharing. Use State for checkpointing complex analysis sessions.
:::

---

## Cache Options

BigDataViewer Playground uses a cache to store recently accessed image tiles in memory, so that scrolling back to a region you've already visited is instantaneous. The cache settings control how much memory is allocated to this cache.

| Parameter | Description |
|-----------|-------------|
| Cache type | Cache implementation to use |
| Cache size (MB) | Fixed cache size in megabytes |
| Reserved memory (MB) | Memory reserved for the rest of the application (Fiji, plugins, etc.) |
| Memory ratio (%) | Percentage of available memory to allocate to the cache |
| Log interval (ms) | Interval between cache log messages (negative to disable) |

:::{important}
Cache options take effect only after restarting Fiji.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Workspace --> Set Cache Options (Needs Restart)`
::::

::::{tab-item} IJ Macro
```ijm
run("Set Cache Options (Needs Restart)");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.workspace.CacheOptionsSetCommand

cs.run(CacheOptionsSetCommand, true,
    "cache_type", "BOUNDED",
    "mem_for_cache_mb", 512,
    "mem_for_everything_else_mb", 256,
    "mem_ratio_pc", 50,
    "log_ms", -1
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.workspace import CacheOptionsSetCommand

cs.run(CacheOptionsSetCommand, True,
    ["cache_type", "BOUNDED",
     "mem_for_cache_mb", 512,
     "mem_for_everything_else_mb", 256,
     "mem_ratio_pc", 50,
     "log_ms", -1]
).get()
```
::::

:::::

:::{tip}
If BigDataViewer feels sluggish when navigating large datasets, increasing the cache size can help — it allows more tiles to stay in memory. Conversely, if Fiji runs out of memory during processing, reduce the cache size to leave more room for other operations.
:::
