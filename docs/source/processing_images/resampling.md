# Resampling

Resampling allows you to change the voxel grid of sources, matching them to a different resolution or aligning them to a common coordinate system.

## Overview

Resampling is essential when:
- Combining images with different resolutions
- Preparing data for analysis that requires uniform voxel sizes
- Reducing data size for faster processing
- Creating multi-resolution pyramids

## Resampling to a Model Source

The most common resampling operation matches source(s) to a "model" source that defines the target voxel grid.

### Command: Resample Sources

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Resample`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesResamplerCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to resample |
| `model` | Model source defining the target voxel grid |
| `name` | Name for the resampled source(s) |
| `reusemipmaps` | Re-use MipMaps from original source |
| `defaultmipmaplevel` | MipMap level if not re-using (0 = max resolution) |
| `interpolate` | Use interpolation when resampling |
| `cache` | Cache resampled data for faster access |

### Example Workflow

1. Open two images with different resolutions
2. Select the source(s) to resample
3. Run the Resample command
4. Select the model source (target resolution)
5. Configure options:
   - Enable interpolation for smoother results
   - Enable caching if you'll access the data multiple times

:::{tip}
Choose a model source that represents your target resolution. All resampled sources will match this voxel grid exactly.
:::

---

## Creating Empty Model Sources

Sometimes you need a custom target grid that doesn't match any existing source.

### Command: New Empty Source

**Menu**: `Plugins > BigDataViewer-Playground > Sources > New Empty Source`
**Class**: `sc.fiji.bdvpg.scijava.command.source.NewSourceCommand`

| Parameter | Description |
|-----------|-------------|
| `model` | Source defining the spatial extent |
| `name` | Name for the new source |
| `voxsizex`, `voxsizey`, `voxsizez` | Voxel sizes for the new source |
| `timepoint` | Timepoint (0-based) |

This creates an empty source with the specified voxel size that covers the same spatial region as the model source.

---

## Pyramidization

For large images, multi-resolution pyramids enable efficient visualization at different zoom levels.

### Command: Pyramidize Sources

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Pyramidize`
**Class**: `ch.epfl.biop.scijava.command.source.SourcesPyramidizerCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to pyramidize |
| `n_resolution_levels` | Number of pyramid levels to create |
| `downscaling` | Downscaling factor between levels (e.g., 2) |

### Example

For an image at 0.5 microns/pixel with 4 levels and factor 2:
- Level 0: 0.5 microns/pixel (original)
- Level 1: 1.0 microns/pixel
- Level 2: 2.0 microns/pixel
- Level 3: 4.0 microns/pixel

:::{note}
Pyramidization is computed lazily. The levels are generated on-demand during visualization, not immediately when the command runs.
:::

---

## Creating Model Sources from Multiple Sources

When working with multiple sources that need to be combined, you may want a model source that spans all of them.

### Command: Make Model Source

**Class**: `ch.epfl.biop.scijava.command.source.SourcesMakeModelCommand`

Creates a model source that covers the bounding box of multiple input sources.

---

## Interpolation Options

When resampling, interpolation affects how pixel values are computed:

| Mode | Description | Use Case |
|------|-------------|----------|
| **Nearest neighbor** | Uses closest pixel value | Discrete data (labels, masks) |
| **Linear** | Weighted average of neighbors | Continuous intensity data |

:::{warning}
Use nearest neighbor interpolation for label images or segmentation masks to avoid creating artificial intermediate values.
:::

---

## Performance Considerations

### Caching

Enable caching when:
- You'll access the resampled data multiple times
- Visualization performance is important
- You have sufficient RAM

Disable caching when:
- Processing very large datasets
- RAM is limited
- Data is accessed only once (e.g., during export)

### MipMap Reuse

When `reusemipmaps` is enabled:
- Resampling uses existing pyramid levels when possible
- Faster for downsampling operations
- May be less precise for upsampling

When `reusemipmaps` is disabled:
- Always computes from the specified `defaultmipmaplevel`
- More consistent results
- May be slower

---

## Common Workflows

### Match Resolution for Analysis

```
1. Identify the target resolution (e.g., from reference image)
2. Select sources to resample
3. Resample to match the reference
4. Proceed with analysis on uniform data
```

### Prepare for Fusion

```
1. Open overlapping images
2. Create a model source spanning all images
3. Resample all sources to the model
4. Apply fusion operation
```

### Downsample for Quick Preview

```
1. Select source(s)
2. Create empty source with larger voxel size
3. Resample to the empty source
4. Visualize the downsampled result
```

---

## Related Commands

- [Fusion](fusion.md) - Combine resampled sources
- [Export Formats](export_formats.md) - Save resampled results
- [Transformations](../commands/transformations.md) - Spatial transforms
