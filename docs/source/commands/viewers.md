# Viewers: Creating and Configuring

BigDataViewer Playground supports two types of viewers:
- **BDV (BigDataViewer)**: The standard 2D slice viewer for navigating 3D data
- **BVV (BigVolumeViewer)**: A GPU-accelerated 3D volume renderer

This section covers how to create, configure, and manage these viewer windows.

## Creating Viewers

### Create an Empty BDV Window

**Command**: `BDV - Create empty BDV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvCreatorCommand`

Creates a new, empty BigDataViewer window. Sources can be added afterwards using the [source display commands](sources_display.md).

**Output**:
- `bdvh`: A handle to the newly created BDV window

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Empty BDV window after creation -->

:::{tip}
Use this command when you want to set up a viewer first and add sources programmatically or through subsequent commands.
:::

---

### Create Orthogonal BDV Views

**Command**: `BDV - Create Orthogonal Views`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvOrthoCreatorCommand`

Creates three synchronized BDV windows showing orthogonal views (XY, XZ, YZ planes). This is particularly useful for examining 3D structures from multiple angles simultaneously.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `drawcrosses` | Add cross overlay to show view plane locations |
| `interpolate` | Enable interpolation for smoother rendering |
| `locationx`, `locationy` | Screen position for the front window |
| `ntimepoints` | Number of timepoints (1 for single timepoint data) |
| `screen` | Display index (0 for single monitor setups) |
| `sizex`, `sizey` | Window dimensions in pixels |
| `synchronize_sources` | Keep sources synchronized across all three views |

**Output**:
- `bdvhx`, `bdvhy`, `bdvhz`: Handles to the three orthogonal BDV windows

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Three orthogonal BDV windows showing the same dataset -->

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script demonstrating orthogonal view creation -->

---

### Create an Empty BVV Window

**Command**: `BVV - Create empty BVV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bvv.BvvWindowCreatorCommand`

Creates a new BigVolumeViewer window for GPU-accelerated 3D volume rendering.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `windowtitle` | Title for the new BVV window |

**Output**:
- `bvvh`: A handle to the newly created BVV window

:::{note}
BVV requires a compatible GPU and is limited to 16-bit images. For very large datasets, consider using BDV instead.
:::

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Empty BVV window -->

---

### Create Orthogonal BVV Views

**Command**: `BVV - Create Orthogonal Views`
**Class**: `sc.fiji.bdvpg.scijava.command.bvv.BvvOrthoWindowCreatorCommand`

Creates three synchronized BVV windows with orthogonal views, similar to the BDV orthogonal view command but with volume rendering.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `interpolate` | Enable interpolation |
| `locationx`, `locationy` | Screen position for the front window |
| `ntimepoints` | Number of timepoints |
| `screen` | Display index |
| `sizex`, `sizey` | Window dimensions |
| `synchronize_sources` | Keep sources synchronized |

**Output**:
- `bvvhx`, `bvvhy`, `bvvhz`: Handles to the three orthogonal BVV windows

---

## Configuring Viewers

### Set BDV Window Preferences

**Command**: `BDV - Set BDV window preferences`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvDefaultViewerSetterCommand`

Configures default settings for new BDV windows. These settings affect all subsequently created BDV windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `frametitle` | Default window title |
| `width`, `height` | Default window dimensions |
| `interpolate` | Enable interpolation by default |
| `is2d` | Create 2D viewers (lock Z navigation) |
| `numrenderingthreads` | Number of threads for rendering |
| `numsourcegroups` | Number of source groups |
| `numtimepoints` | Default number of timepoints |
| `screenscales` | Screen scales for multi-resolution rendering |
| `targetrenderms` | Target render time in milliseconds |
| `resetToDefault` | Check to reset all settings to defaults |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV preferences dialog -->

:::{tip}
Adjusting `numrenderingthreads` can improve performance on multi-core systems. Start with a value equal to half your CPU cores.
:::

---

### Set BDV Window Title

**Command**: `BDV - Set BDV window title`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvTitleSetterCommand`

Changes the title of an existing BDV window.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | The BDV window to rename |
| `title` | New title for the window |

:::{note}
There is also `RenameBdv` which does the same thing. Both commands are interchangeable.
:::

---

### Configure Key and Mouse Bindings

**Command**: `BDV - Set BDV keyboard/mouse settings`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvSettingsCommand`

Opens a dialog to configure keyboard shortcuts and mouse actions in BDV windows.

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV settings dialog showing key bindings -->

<!-- TODO:MISSING_CONTENT: [type: example] - List of common keyboard shortcuts -->

---

## Managing Timepoints

### Set Number of Timepoints (BDV)

**Command**: `BDV - Set number of timepoints`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvTimepointsSetterCommand`

Manually sets the number of timepoints in one or more BDV windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to modify |
| `numberoftimepoints` | Number of timepoints (minimum 1) |

---

### Adapt Timepoints to Sources (BDV)

**Command**: `BDV - Adapt timepoints to sources`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvTimepointAdapterCommand`

Automatically adjusts the number of timepoints in BDV windows to match the timepoints present in their sources. Useful when loading time-series data.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to adapt |

---

### Set Number of Timepoints (BVV)

**Command**: `BVV - Set number of timepoints`
**Class**: `sc.fiji.bdvpg.scijava.command.bvv.BvvSetTimepointsNumberCommand`

Sets the number of timepoints in one or more BVV windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bvvhs` | BVV window(s) to modify |
| `numberoftimepoints` | Number of timepoints (minimum 1) |

---

## Closing Viewers

### Close BDV Windows

**Command**: `BDV - Close BDV windows`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvCloseCommand`

Closes one or more BDV windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to close |

:::{warning}
Closing a BDV window does not remove the sources from the SourceAndConverter service. They remain available for display in other windows.
:::

---

## Summary

| Command | Purpose |
|---------|---------|
| `BdvCreatorCommand` | Create empty BDV window |
| `BdvOrthoCreatorCommand` | Create 3 orthogonal BDV views |
| `BvvWindowCreatorCommand` | Create empty BVV window |
| `BvvOrthoWindowCreatorCommand` | Create 3 orthogonal BVV views |
| `BdvDefaultViewerSetterCommand` | Configure BDV defaults |
| `BdvTitleSetterCommand` | Rename BDV window |
| `BdvSettingsCommand` | Configure key/mouse bindings |
| `MultiBdvTimepointsSetterCommand` | Set BDV timepoints |
| `MultiBdvTimepointAdapterCommand` | Auto-adapt BDV timepoints |
| `BvvSetTimepointsNumberCommand` | Set BVV timepoints |
| `MultiBdvCloseCommand` | Close BDV windows |
