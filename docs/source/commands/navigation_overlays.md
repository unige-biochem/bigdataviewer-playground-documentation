# View Navigation and Overlays

This section covers commands for navigating within viewer windows and adding helpful UI overlays that enhance the viewing experience.

## View Navigation

### Adjust View to Sources

**Command**: `BDV - Adjust view on sources`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvViewAdjustOnSourcesCommand`

Automatically adjusts the BDV view (zoom and position) to fit the selected sources in the window. Useful after loading new data or when sources are out of view.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | BDV window to adjust |
| `sacs` | Source(s) to fit in view |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Before/after showing view adjustment -->

:::{tip}
Use this command after adding sources to quickly center the view on your data.
:::

---

### Apply View Transform

**Command**: `BDV - Apply view transformation`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvViewTransformatorCommand`

Applies a specified transformation to the current view. This changes what you see in the window, not the underlying source data.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | BDV window to transform |
| `translatex`, `translatey`, `translatez` | Translation amounts |
| `rotatearoundx`, `rotatearoundy`, `rotatearoundz` | Rotation angles (degrees) |

### Use Cases

- **Programmatic navigation**: Move to specific locations in scripts
- **Standardized views**: Apply consistent view angles for comparison
- **Animation**: Create sequences with incremental transformations

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script demonstrating programmatic view navigation -->

:::{note}
View transformations affect only the viewing angle and position - they do not modify source data. For data transformations, see [Transformations](transformations.md).
:::

---

## Overlays

Overlays are visual elements drawn on top of the viewer to provide additional information or controls.

### Add Centering Cross

**Command**: `BDV - Add centering cross overlay`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvCrossAdderCommand`

Adds a crosshair overlay at the center of the BDV window. Useful for:
- Identifying the exact center of the view
- Aligning features during manual registration
- Marking a reference point when navigating

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to add the cross to |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV window with centering cross overlay -->

:::{tip}
The centering cross is particularly useful with [orthogonal views](viewers.md#create-orthogonal-bdv-views) to see where the view planes intersect.
:::

---

### Add Source Name Overlay

**Command**: `BDV - Add source name overlay`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourceNameOverlayAdderCommand`

Displays the names of visible sources as text overlaid on the viewer. Helpful when working with multiple sources to identify what you're looking at.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to add the overlay to |
| `fontSize` | Font size for the text |
| `fontString` | Font specification |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV window showing source name overlay -->

---

### Add Z Slider

**Command**: `BDV - Add Z slider overlay`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvZSliderAdderCommand`

Adds a slider control for navigating through Z slices. Provides a more intuitive way to browse through 3D data compared to mouse scrolling.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to add the slider to |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV window with Z slider -->

### Features

- Drag the slider to move through Z
- Shows current Z position
- Snaps to slice positions

---

### Add Source Navigator Slider

**Command**: `BDV - Add source navigator slider`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourceNavigatorSliderAdderCommand`

Adds a slider for navigating between different sources. Useful when you have many sources and want to quickly switch between them.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to add the slider to |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV window with source navigator slider -->

---

## Combining Overlays

You can add multiple overlays to the same viewer:

1. **Navigation setup**: Add Z slider + centering cross for precise positioning
2. **Multi-source comparison**: Add source navigator + source name overlay
3. **Orthogonal views**: Add centering cross to all three windows to visualize intersection

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BDV window with multiple overlays combined -->

---

## Standard BDV Navigation

In addition to these commands, BDV provides built-in navigation controls:

### Mouse Controls

| Action | Effect |
|--------|--------|
| Left-drag | Rotate view |
| Right-drag | Pan (translate) view |
| Scroll | Zoom in/out |
| Middle-drag | Move through Z |

### Keyboard Controls

| Key | Effect |
|-----|--------|
| `Shift + X` | Align view to X axis |
| `Shift + Y` | Align view to Y axis |
| `Shift + Z` | Align view to Z axis |
| `I` | Toggle interpolation |
| `S` | Toggle source visibility |
| `F` | Toggle fused mode |

<!-- TODO:MISSING_CONTENT: [type: example] - Complete list of BDV keyboard shortcuts -->

:::{tip}
Use `Shift + Z` to quickly snap to the standard XY view orientation.
:::

---

## Summary

| Command | Purpose |
|---------|---------|
| `BdvViewAdjustOnSourcesCommand` | Fit view to sources |
| `BdvViewTransformatorCommand` | Apply view transformation |
| `MultiBdvCrossAdderCommand` | Add centering cross |
| `MultiBdvSourceNameOverlayAdderCommand` | Show source names |
| `MultiBdvZSliderAdderCommand` | Add Z navigation slider |
| `MultiBdvSourceNavigatorSliderAdderCommand` | Add source switcher slider |
