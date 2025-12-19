# State Management and Settings

BigDataViewer Playground allows you to save and restore your working session, including all loaded sources, their display settings, transformations, and organization. This section covers state management and global settings.

## The SourceAndConverter Service

The SourceAndConverter Service is the central manager for all sources in BDV Playground. It tracks:
- All loaded sources
- Display settings (colors, brightness)
- Transformations
- Metadata and groups
- Relationships between sources

### Show the Service Window

**Command**: `Service - Show SourceAndConverter window`
**Class**: `sc.fiji.bdvpg.scijava.command.ShowSourceAndConverterServiceWindow`

Opens the SourceAndConverter Service window, which provides a tree view of all sources and tools for managing them.

<!-- TODO:MISSING_CONTENT: [type: screenshot] - The SourceAndConverter Service window -->

### Service Window Features

- **Tree view**: Hierarchical display of sources and groups
- **Right-click menu**: Access commands for selected sources
- **Drag and drop**: Reorganize sources
- **Multi-select**: Select multiple sources for batch operations

---

## Saving and Loading State

### Save Session State

**Command**: `State - Save state`
**Class**: `sc.fiji.bdvpg.scijava.command.SaveSourceAndConverterServiceState`

Saves the entire current state to a JSON file, including:
- All source references
- Display settings (colors, brightness ranges)
- Applied transformations
- Groups and metadata
- Tree organization

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `file` | Output file path (.json) |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Save state dialog -->

### What Gets Saved

| Saved | Not Saved |
|-------|-----------|
| Source references (paths to data) | Actual pixel data |
| Display settings | Open viewer windows |
| Transformations | View positions |
| Metadata | Unsaved image modifications |
| Groups and tree structure | |

:::{note}
The state file contains **references** to data files, not the data itself. The original files must remain accessible at the same paths.
:::

---

### Load Session State

**Command**: `State - Load state`
**Class**: `sc.fiji.bdvpg.scijava.command.LoadSourceAndConverterServiceState`

Restores a previously saved session state from a JSON file.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `file` | State file to load (.json) |
| `erasepreviousstate` | If true, clear current sources before loading. If false, merge with existing. |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Load state dialog -->

### Erase vs Merge Mode

**Erase mode** (`erasepreviousstate = true`):
- Clears all current sources
- Loads the saved state fresh
- Use when: Starting a new session from saved state

**Merge mode** (`erasepreviousstate = false`):
- Keeps existing sources
- Adds sources from the saved state
- Use when: Combining multiple saved sessions

:::{warning}
In merge mode, duplicate sources may appear if the same data is in both the current state and the saved file.
:::

---

## Practical State Management

### Workflow: Daily Save/Restore

1. **At end of session**: Save state with descriptive filename
   ```
   Project_Analysis_2024-01-15.json
   ```

2. **Next session**: Load the saved state
   - All sources, settings, and organization restored
   - Continue where you left off

### Workflow: Sharing Analysis

1. **Complete your analysis setup**
2. **Save state to shared location**
3. **Colleague loads state on their machine**
4. **They see exactly your setup** (if data paths are accessible)

<!-- TODO:MISSING_CONTENT: [type: script] - Automated state save script -->

:::{tip}
Include dates or version numbers in state filenames to track your analysis history.
:::

### State File Best Practices

1. **Use relative data paths** when possible (for portability)
2. **Save states before major changes** (as checkpoints)
3. **Keep state files with your project** (not in temp locations)
4. **Document what each state file represents**

---

## Cache Settings

### Configure Cache Options

**Command**: `Settings - Cache options`
**Class**: `sc.fiji.bdvpg.scijava.command.CacheOptionsCommand`

Configures the caching system used by BDV Playground. Proper cache settings can significantly impact performance when viewing large datasets.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `cache_type` | Type of cache to use |
| `mem_for_cache_mb` | Fixed cache size in megabytes |
| `mem_for_everything_else_mb` | Memory to reserve for other operations |
| `mem_ratio_pc` | Use a percentage of available memory |
| `log_ms` | Logging interval (negative to disable) |
| `button` | Reset to defaults |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Cache options dialog -->

:::{warning}
Changes to cache settings require a **restart of Fiji** to take effect.
:::

### Cache Sizing Strategies

#### Fixed Size (`mem_for_cache_mb`)

Set an exact cache size:
- **Pros**: Predictable memory usage
- **Cons**: May not adapt to system resources
- **Use when**: Memory is limited or shared with other applications

#### Leave Room for Application (`mem_for_everything_else_mb`)

Specify how much memory to leave free:
- Cache gets everything else
- **Use when**: BDV Playground is the main application

#### Ratio (`mem_ratio_pc`)

Use a percentage of total memory:
- **Pros**: Scales with system resources
- **Cons**: Less predictable
- **Use when**: Running on different machines

### Recommended Settings

| System RAM | Suggested Cache |
|------------|-----------------|
| 8 GB | 2-4 GB |
| 16 GB | 6-10 GB |
| 32 GB | 16-24 GB |
| 64+ GB | 32-48 GB |

:::{tip}
If you experience slow navigation or frequent "loading" indicators, increase the cache size.
:::

---

## Troubleshooting

### State Loading Issues

| Problem | Solution |
|---------|----------|
| "File not found" errors | Check that data files haven't moved |
| Missing sources | Verify paths in the JSON file |
| Wrong settings | Check for merge vs erase mode |

### Cache Issues

| Problem | Solution |
|---------|----------|
| Out of memory | Reduce cache size |
| Slow navigation | Increase cache size |
| Settings not applied | Restart Fiji |

### Recovering from Problems

If the service gets into a bad state:
1. Save any important state files
2. Close all BDV windows
3. Restart Fiji
4. Load your saved state

---

## Summary

| Command | Purpose |
|---------|---------|
| `ShowSourceAndConverterServiceWindow` | Open the service management window |
| `SaveSourceAndConverterServiceState` | Save session to JSON |
| `LoadSourceAndConverterServiceState` | Restore session from JSON |
| `CacheOptionsCommand` | Configure memory cache |
