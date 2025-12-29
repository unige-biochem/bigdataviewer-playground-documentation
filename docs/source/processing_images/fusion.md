# Image Fusion

Image fusion combines multiple overlapping sources into a single output. This is essential for stitched datasets, multi-view acquisitions, and combining registered images.

## Overview

Fusion in BigDataViewer Playground:
- Combines pixel values from overlapping regions
- Supports multiple blending methods
- Works with BigStitcher datasets
- Exports to OME-TIFF for downstream analysis

## Fusion Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **Average** | Mean of overlapping pixels | General purpose, reduces noise |
| **Max** | Maximum value | Fluorescence, sparse signals |
| **Min** | Minimum value | Inverted signals |
| **Sum** | Sum of values | Additive signals |
| **Blending** | Weighted by distance to edge | Smooth transitions |

---

## Fusing Sources

### Command: Fuse and Resample Sources

**Class**: `ch.epfl.biop.scijava.command.source.SourcesFuserAndResamplerCommand`

Fuses multiple sources and resamples them to a model grid.

| Parameter | Description |
|-----------|-------------|
| `sources_in` | Sources to fuse |
| `model` | Model source defining output geometry |
| `fusion_method` | Method for combining overlapping pixels |
| `interpolate` | Use interpolation when resampling |

### Workflow

1. Ensure sources are properly positioned (registered/stitched)
2. Select all sources to fuse
3. Select or create a model source for output geometry
4. Choose fusion method
5. Run fusion command

:::{note}
Fusion is computed lazily. The fused result is generated on-demand during visualization or export.
:::

---

## Fusing BigStitcher Datasets

For datasets created with BigStitcher, a dedicated command handles the complete fusion and export workflow.

### Command: Fuse BigStitcher Dataset to OME-TIFF

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Fuse a BigStitcher dataset to OME-Tiff`
**Class**: `ch.epfl.biop.scijava.command.spimdata.FuseBigStitcherDatasetIntoOMETiffCommand`

| Parameter | Description |
|-----------|-------------|
| `xml_bigstitcher_file` | BigStitcher XML dataset file |
| `output_path_directory` | Output folder for OME-TIFF |
| `range_channels` | Channels to export (e.g., "0,1" or "0:2") |
| `range_slices` | Z-slices to export (e.g., "0:100") |
| `range_frames` | Timepoints to export |
| `n_resolution_levels` | Number of pyramid levels |
| `fusion_method` | Blending method |
| `use_lzw_compression` | Apply LZW compression |
| `split_slices` | Export each Z-slice separately |
| `split_channels` | Export each channel separately |
| `split_frames` | Export each timepoint separately |
| `x_downsample`, `y_downsample`, `z_downsample` | Downsampling factors |
| `use_interpolation` | Interpolation during fusion |

### Example: Export Full Dataset

```
xml_bigstitcher_file: /path/to/dataset.xml
output_path_directory: /path/to/output/
range_channels: (empty for all)
range_slices: (empty for all)
n_resolution_levels: 4
fusion_method: Blending
use_lzw_compression: true
```

### Example: Export Subset

```
range_channels: 0,1
range_slices: 50:150
range_frames: 0
x_downsample: 2.0
y_downsample: 2.0
z_downsample: 1.0
```

---

## Alpha Blending

For advanced fusion with controlled transparency, BigDataViewer Playground supports alpha blending.

### Command: Set Alpha Source

**Class**: `ch.epfl.biop.scijava.command.source.SourceSetAlphaCommand`

Associates an alpha (transparency) source with image sources for blending operations.

| Parameter | Description |
|-----------|-------------|
| `sacs` | Sources to set alpha for |
| `alpha_source` | Source defining transparency values |

### Alpha Blending Modes

The alpha blending system supports:
- **Smooth average**: Weighted blending based on alpha
- **Distance-weighted**: Fade based on distance from source edges
- **Layer compositing**: Multi-layer blending with priorities

---

## Fusion Considerations

### Memory Management

Fusion of large datasets can be memory-intensive. The biop-tools fusion implementation includes:
- Block-based processing with bounded cache
- Automatic tile pre-filtering
- Cache cleanup at 50% RAM usage

### Performance Tips

| Factor | Recommendation |
|--------|----------------|
| Large dataset | Use downsampling factors |
| Many tiles | Block-based fusion handles this automatically |
| Limited RAM | Enable split options (slices, channels, frames) |
| Slow export | Increase n_threads, reduce compression |

### Quality Considerations

| Scenario | Recommendation |
|----------|----------------|
| Visible seams | Use "Blending" fusion method |
| Intensity variations | Consider flat-field correction before fusion |
| Registration errors | Re-run registration with finer parameters |

---

## Common Workflows

### Fuse Stitched Tiles

```
1. Stitch tiles in BigStitcher
2. Save BigStitcher XML
3. Run "Fuse BigStitcher Dataset to OME-TIFF"
4. Configure output options
5. Export fused result
```

### Fuse Registered Images

```
1. Register images (see Registration section)
2. Resample registered sources to common grid
3. Apply fusion with chosen blending method
4. Export result
```

### Create Composite View

```
1. Load multiple channels/views
2. Assign alpha sources for transparency
3. Visualize blended result in BDV
4. Export if needed
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Visible seams | Hard edges in tiles | Use "Blending" fusion method |
| Memory errors | Dataset too large | Enable split options, use downsampling |
| Slow export | Large data, high resolution | Reduce resolution levels, increase threads |
| Black regions | Missing data | Check that all tiles are properly positioned |
| Intensity jumps | Different exposure | Apply flat-field correction before fusion |

---

## Related Topics

- [Resampling](resampling.md) - Prepare sources for fusion
- [Export Formats](export_formats.md) - Save fused results
- [Registration](../registration/index.md) - Align images before fusion
