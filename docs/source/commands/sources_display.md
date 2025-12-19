# Sources: Display and Management

In BigDataViewer Playground, image data is represented as **Sources**. A source wraps the actual image data and provides metadata about its spatial calibration, time points, and display settings.

This section covers how to display sources in viewers and manage their lifecycle.

## Understanding Sources

A **SourceAndConverter** is the fundamental unit in BDV Playground. It combines:
- **Source**: The actual image data (pixels, voxels)
- **Converter**: Display settings (color, brightness range)

Sources are managed by the **SourceAndConverter Service**, which keeps track of all loaded sources and their properties.

<!-- TODO:MISSING_CONTENT: [type: screenshot] - The SourceAndConverter service window showing a list of sources -->

---

## Displaying Sources in BDV

### Show Sources in a New BDV Window

**Command**: `BDV - Show sources in new BDV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesShowCommand`

Creates a new BDV window and displays the selected sources in it. This is often the quickest way to visualize sources.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to display |
| `adjustviewonsource` | Automatically adjust the view to fit the sources |
| `autocontrast` | Automatically set brightness/contrast |
| `interpolate` | Enable interpolation for smoother rendering |

**Output**:
- `bdvh`: Handle to the newly created BDV window

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Sources displayed in a new BDV window -->

:::{tip}
Enable `autocontrast` when first viewing a new dataset to automatically set appropriate display ranges.
:::

---

### Add Sources to an Existing BDV Window

**Command**: `BDV - Add sources to BDV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesAdderCommand`

Adds one or more sources to an already open BDV window. Useful for comparing datasets or adding channels.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | Target BDV window |
| `sacs` | Source(s) to add |
| `adjustviewonsource` | Adjust view to fit the newly added sources |
| `autocontrast` | Auto-adjust brightness/contrast |

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script adding multiple sources to a BDV window -->

---

### Add Sources to Multiple BDV Windows

**Command**: `BDV - Add sources to multiple BDV windows`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourcesAdderCommand`

Adds sources to several BDV windows at once. Useful when working with synchronized orthogonal views.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | Target BDV window(s) |
| `sacs` | Source(s) to add |

---

### Remove Sources from a BDV Window

**Command**: `BDV - Remove sources from BDV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesRemoverCommand`

Removes sources from display in a BDV window. The sources remain in the service and can be re-added later.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | Target BDV window |
| `sacs` | Source(s) to remove |

:::{note}
This only removes sources from the display. To permanently delete sources, use `SourcesRemoverCommand`.
:::

---

### Remove Sources from Multiple BDV Windows

**Command**: `BDV - Remove sources from multiple BDV windows`
**Class**: `sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourcesRemoverCommand`

Removes sources from several BDV windows at once.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | Target BDV window(s) |
| `sacs` | Source(s) to remove |

---

## Displaying Sources in BVV

### Add Sources to a BVV Window

**Command**: `BVV - Add sources to BVV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bvv.BvvSourcesAdderCommand`

Displays sources in a BigVolumeViewer window for 3D volume rendering.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bvvh` | Target BVV window |
| `sacs` | Source(s) to display |
| `adjustviewonsource` | Adjust view to fit the sources |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Source displayed in BVV with volume rendering -->

:::{warning}
BVV is limited to **16-bit images**. Sources with higher bit depths will not display correctly.
:::

---

### Remove Sources from a BVV Window

**Command**: `BVV - Remove sources from BVV window`
**Class**: `sc.fiji.bdvpg.scijava.command.bvv.BvvSourcesRemoverCommand`

Removes sources from a BVV window display.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bvvh` | Target BVV window |
| `sacs` | Source(s) to remove |

---

## Source Visibility

### Make Sources Visible

**Command**: `Sources - Make sources visible`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesVisibleMakerCommand`

Makes selected sources visible in all BDV windows where they are present.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to make visible |

---

### Make Sources Invisible

**Command**: `Sources - Make sources invisible`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesInvisibleMakerCommand`

Hides selected sources in all BDV windows without removing them. The sources remain available and can be made visible again.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to hide |

:::{tip}
Use visibility toggling to quickly compare datasets by showing/hiding specific sources, rather than removing and re-adding them.
:::

---

## Managing Source Lifecycle

### Duplicate Sources

**Command**: `Sources - Duplicate sources`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesDuplicatorCommand`

Creates copies of selected sources. The duplicates share the underlying image data but have independent display settings.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to duplicate |

:::{note}
Duplicated sources share the same underlying data - no additional memory is used for pixel data. Only the display settings (color, brightness) are independent.
:::

<!-- TODO:MISSING_CONTENT: [type: example] - Use case: duplicating a source to show it with two different LUTs -->

---

### Remove Sources Permanently

**Command**: `Sources - Remove sources from service`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesRemoverCommand`

Permanently removes sources from the SourceAndConverter service. This also removes them from all viewer windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to remove |

:::{warning}
This action cannot be undone. The sources will need to be re-imported if you want to use them again.
:::

---

## Workflow Example

A typical workflow for displaying sources:

1. **Import data** using [Import commands](import_export.md) - sources appear in the service
2. **Show sources** in a new BDV window using `BdvSourcesShowCommand`
3. **Adjust visibility** to compare different channels
4. **Duplicate sources** if you need the same data with different display settings
5. **Remove from view** when done, or **remove permanently** to free up resources

<!-- TODO:MISSING_CONTENT: [type: script] - Complete Groovy workflow script demonstrating source management -->

---

## Summary

| Command | Purpose |
|---------|---------|
| `BdvSourcesShowCommand` | Display sources in new BDV window |
| `BdvSourcesAdderCommand` | Add sources to existing BDV window |
| `BdvSourcesRemoverCommand` | Remove sources from BDV window |
| `MultiBdvSourcesAdderCommand` | Add sources to multiple BDV windows |
| `MultiBdvSourcesRemoverCommand` | Remove sources from multiple BDV windows |
| `BvvSourcesAdderCommand` | Add sources to BVV window |
| `BvvSourcesRemoverCommand` | Remove sources from BVV window |
| `SourcesVisibleMakerCommand` | Make sources visible |
| `SourcesInvisibleMakerCommand` | Hide sources |
| `SourcesDuplicatorCommand` | Create source copies |
| `SourcesRemoverCommand` | Permanently remove sources |
