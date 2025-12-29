# BigStitcher Integration

BigDataViewer Playground provides tools for working with BigStitcher datasets, including CZI file preparation and dataset fusion.

## Overview

[BigStitcher](https://imagej.net/plugins/bigstitcher/) is a powerful tool for reconstructing large tiled datasets. BigDataViewer Playground complements BigStitcher with:

- CZI to BigStitcher format conversion
- Dataset compatibility conversion
- Fused export to OME-TIFF
- Entity and metadata management

## CZI to BigStitcher

### Command: Make CZI Dataset for BigStitcher

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Edit > Make CZI Dataset for BigStitcher`
**Class**: `ch.epfl.biop.scijava.command.spimdata.CreateCZIDatasetCommand`

Converts a Zeiss CZI file to a BigStitcher-compatible XML dataset.

| Parameter | Description |
|-----------|-------------|
| `czi_file` | The CZI file to convert |
| `erase_if_file_already_exists` | Overwrite existing output file |

| Output | Description |
|--------|-------------|
| `xml_out` | The BigStitcher-compatible XML file |

### When to Use

Use this command when:
- You have tiled CZI acquisitions
- You want to use BigStitcher for stitching
- Standard Bio-Formats import doesn't preserve tile positions

### Workflow

```
1. Run Make CZI Dataset for BigStitcher
2. Select your CZI file
3. An XML file is created alongside the CZI
4. Open the XML in BigStitcher for stitching
```

---

## Converting BDV to BigStitcher Format

### Command: Make BDVDataset BigStitcher Compatible

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Edit > Make BDVDataset BigStitcher Compatible`
**Class**: `ch.epfl.biop.scijava.command.spimdata.DatasetToBigStitcherDatasetCommand`

Converts a BDV dataset to BigStitcher format by removing incompatible attributes.

| Parameter | Description |
|-----------|-------------|
| `xmlin` | Input BDV XML dataset |
| `viewsetupreference` | View setup for rescaling reference |
| `xmlout` | Output BigStitcher-compatible XML |

### When to Use

Use when:
- Your BDV dataset has custom entities BigStitcher doesn't understand
- You need to process existing BDV data in BigStitcher
- Converting from BDV Playground format to BigStitcher

---

## Fusing BigStitcher Datasets

After stitching in BigStitcher, export the fused result using BDV Playground.

### Command: Fuse BigStitcher Dataset to OME-TIFF

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Fuse a BigStitcher dataset to OME-Tiff`
**Class**: `ch.epfl.biop.scijava.command.spimdata.FuseBigStitcherDatasetIntoOMETiffCommand`

| Parameter | Description |
|-----------|-------------|
| `xml_bigstitcher_file` | BigStitcher XML dataset |
| `output_path_directory` | Output folder |
| `range_channels` | Channels to export (e.g., "0,1" or empty for all) |
| `range_slices` | Z-slices to export |
| `range_frames` | Timepoints to export |
| `n_resolution_levels` | Pyramid levels |
| `fusion_method` | Blending method |
| `use_lzw_compression` | Enable compression |
| `split_slices/channels/frames` | Export as separate files |
| `x/y/z_downsample` | Downsampling factors |
| `use_interpolation` | Interpolate during fusion |

See [Fusion](../processing_images/fusion.md) for detailed parameter explanations.

---

## Managing Dataset Entities

### Remove Display Settings

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Edit > Remove Display Settings from BDVDataset`
**Class**: `ch.epfl.biop.scijava.command.spimdata.RemoveDisplaySettingsCommand`

Removes display settings for compatibility with other tools.

| Parameter | Description |
|-----------|-------------|
| `xmlin` | Input XML file |
| `xmlout` | Output XML file |

### Remove Entities

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Edit > Remove Entities from BDVDataset`
**Class**: `ch.epfl.biop.scijava.command.spimdata.RemoveEntitiesCommand`

Removes specific entity types for compatibility.

| Parameter | Description |
|-----------|-------------|
| `xmlin` | Input XML file |
| `xmlout` | Output XML file |
| `entitiestoremove` | Comma-separated entity types (e.g., "displaysettings, fileindex") |

---

## Complete Workflows

### CZI Stitching Pipeline

```
1. Acquire tiled CZI on Zeiss microscope
2. Convert CZI to BigStitcher format
   └── Make CZI Dataset for BigStitcher
3. Open in BigStitcher
4. Detect interest points
5. Calculate stitching
6. Fuse to OME-TIFF
   └── Fuse BigStitcher Dataset to OME-TIFF
7. Open fused result in QuPath or other tools
```

### Multi-View Fusion

```
1. Open multi-view dataset in BigStitcher
2. Register views
3. Configure fusion parameters
4. Export with BDV Playground fusion
5. Analyze fused result
```

### Format Conversion

```
1. Start with BDV dataset
2. Remove incompatible entities if needed
3. Convert to BigStitcher format
4. Process in BigStitcher
5. Export final result
```

---

## Fusion Methods

When exporting fused data, choose the appropriate blending method:

| Method | Description | Best For |
|--------|-------------|----------|
| **Blending** | Weighted by distance to edges | General use, smooth transitions |
| **Average** | Mean of overlapping pixels | Reduce noise |
| **Max** | Maximum intensity | Sparse fluorescence |
| **Min** | Minimum intensity | Inverted signals |

---

## Performance Tips

### Large Dataset Fusion

| Issue | Solution |
|-------|----------|
| Out of memory | Use split options, downsample |
| Slow export | Increase threads, reduce resolution levels |
| Disk space | Enable compression |

### Export Settings

| Dataset Size | Recommendations |
|--------------|-----------------|
| < 10 GB | Full resolution, 4 levels |
| 10-100 GB | Consider 2x downsample, 4-5 levels |
| > 100 GB | Downsample, split files, compression |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| BigStitcher won't open XML | Incompatible entities | Use Remove Entities command |
| Fusion has seams | Wrong blend method | Use "Blending" method |
| Missing tiles in fusion | Transformation not computed | Complete BigStitcher stitching first |
| Export incomplete | Disk full or interrupted | Check space, re-run |

---

## Related Topics

- [Fusion](../processing_images/fusion.md) - Fusion methods and parameters
- [Export Formats](../processing_images/export_formats.md) - Output format options
- [Opening Images](../opening_images/opening_images.md) - General import methods
