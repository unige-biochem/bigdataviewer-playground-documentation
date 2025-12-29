# Zeiss LLS7 (Lattice Light Sheet)

BigDataViewer Playground provides dedicated support for Zeiss Lattice Light Sheet 7 (LLS7) datasets, including automatic deskewing during visualization.

## Overview

Lattice light sheet microscopy produces data with a characteristic shear due to the oblique illumination geometry. The LLS7 loader in BigDataViewer Playground:

- Automatically deskews data during visualization
- Maintains lazy loading (deskewing computed on-demand)
- Preserves original data (non-destructive)
- Supports 3D cropping of deskewed volumes

## Opening LLS7 Datasets

### Command: Create BDV Dataset [Zeiss LLS7]

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Zeiss LLS7]`
**Class**: `ch.epfl.biop.scijava.command.spimdata.LLS7OpenDatasetCommand`

| Parameter | Description |
|-----------|-------------|
| `czi_file` | The CZI file from a Zeiss LLS7 acquisition |
| `legacy_xy_mode` | Use legacy XY orientation (for older datasets) |

### Workflow

1. Acquire data on Zeiss LLS7
2. In Fiji, run `Create BDV Dataset [Zeiss LLS7]`
3. Select your CZI file
4. The dataset opens with live deskewing enabled

:::{note}
The deskewing is computed on-the-fly during visualization. The original skewed data is not modified.
:::

---

## Understanding Deskewing

### Why Deskewing is Needed

In lattice light sheet microscopy:
- The light sheet illuminates the sample at an oblique angle
- The camera captures images perpendicular to the detection objective
- This creates a parallelogram-shaped volume instead of a rectangular one

Deskewing transforms this parallelogram back to a rectangular volume for proper visualization and analysis.

### Live Deskewing

The LLS7 loader applies deskewing as a spatial transform:
- No intermediate files created
- Deskewing computed only for visible regions
- Efficient for large time-series

---

## Cropping LLS7 Data

After opening an LLS7 dataset, you can crop a 3D region from the deskewed volume.

### Command: LLS7 - Crop 3D

**Menu**: `Plugins > BigDataViewer-Playground > BDV > LLS7 - Crop 3D`
**Class**: `ch.epfl.biop.scijava.command.spimdata.LLS7CropCommand`

| Parameter | Description |
|-----------|-------------|
| `bdvh` | The BDV window containing LLS7 sources |
| `sources` | Source(s) to crop |
| `image_name` | Name for the cropped result |

| Output | Description |
|--------|-------------|
| `interval` | The selected 3D bounding box |
| `result` | True if user confirmed, false if cancelled |

### Cropping Workflow

1. Open LLS7 dataset in BDV
2. Navigate to the region of interest
3. Run `LLS7 - Crop 3D`
4. Interactively adjust the 3D bounding box
5. Confirm to create cropped source

:::{tip}
Use cropping to extract specific cells or structures for detailed analysis or export.
:::

---

## Complete LLS7 Workflow

### Basic Visualization

```
1. Open LLS7 CZI file
2. View deskewed data in BDV
3. Navigate through time and z
4. Adjust display settings (brightness, color)
```

### Analysis Workflow

```
1. Open LLS7 dataset
2. Crop region of interest
3. Export cropped region to ImagePlus
4. Analyze in Fiji (tracking, segmentation, etc.)
```

### Deconvolution Workflow

```
1. Open LLS7 dataset
2. Prepare LLS-specific PSF
3. Apply GPU deconvolution
4. Visualize or export deconvolved result
```

See [Deconvolution](../processing_images/deconvolution.md) for details.

---

## Parameters and Settings

### Legacy XY Mode

The `legacy_xy_mode` option is for compatibility with older LLS7 datasets:

| Setting | Use Case |
|---------|----------|
| Unchecked (default) | Current LLS7 data format |
| Checked | Older datasets with different XY convention |

If your data appears flipped or rotated incorrectly, try enabling legacy mode.

---

## Performance Considerations

### Memory

- Deskewing is lazy: only visible data is computed
- Large time-series work efficiently
- Cropping reduces data for export

### Visualization Speed

| Factor | Impact |
|--------|--------|
| Many timepoints | Minimal (lazy loading) |
| High resolution | May slow navigation |
| Multiple channels | Linear increase |

### Export Tips

- Crop to region of interest before export
- Consider downsampling for large volumes
- Use appropriate output format (see [Export Formats](../processing_images/export_formats.md))

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Data appears skewed | Deskewing not applied | Verify using LLS7 loader, not standard Bio-Formats |
| Wrong orientation | XY convention mismatch | Try `legacy_xy_mode` |
| Slow loading | Large file | Normal for first access; subsequent views faster |
| Cropping fails | Invalid selection | Ensure bounding box is within data bounds |

---

## Related Topics

- [Opening Images](../opening_images/opening_images.md) - General import methods
- [Deconvolution](../processing_images/deconvolution.md) - Improve LLS7 resolution
- [Export Formats](../processing_images/export_formats.md) - Save processed LLS7 data
