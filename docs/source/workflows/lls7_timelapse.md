# Process LLS7 Timelapse

This workflow guides you through processing lattice light-sheet (LLS7) timelapse data: deskewing, cropping, deconvolution, and export.

## Goal

Transform raw LLS7 acquisitions into analysis-ready data:
- Correct the sheared geometry (deskewing)
- Crop to region of interest
- Deconvolve for improved resolution
- Export for downstream analysis

## Prerequisites

- [ ] BigDataViewer Playground installed ([Installation Guide](../installation/installation.md))
- [ ] CLIJ/CLIJ2 installed for GPU deconvolution (optional but recommended)
- [ ] LLS7 raw data (.czi or similar format)
- [ ] PSF image for deconvolution (optional)

## Overview

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│ Open LLS7   │ ──▶ │ Deskew       │ ──▶ │ Crop        │ ──▶ │ Deconvolve   │
│ Raw Data    │     │              │     │ (optional)  │     │ + Export     │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

---

## Step 1: Open LLS7 Data

### Load Raw Acquisition

```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Open with QuPath Bio-Formats Builder
```

Or for CZI files specifically:
```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Open CZI Dataset
```

The data will appear sheared due to the oblique illumination geometry.

### Verify Metadata

Check that voxel sizes are correctly read:
- Right-click source in tree > `Show Info`
- Verify XYZ voxel dimensions

:::{note}
LLS7 raw data has anisotropic voxels and appears sheared. This is normal and will be corrected by deskewing.
:::

---

## Step 2: Deskew

Correct the sheared geometry to isotropic coordinates.

### Apply Deskew Transform

```
Menu: Plugins > BigDataViewer-Playground > Sources > Transform > LLS7 > Deskew LLS7 Dataset
```

| Parameter | Description |
|-----------|-------------|
| Source | Your LLS7 raw data |
| Angle | LLS7 illumination angle (typically 30° or 58°) |
| Direction | Shear direction (check your system configuration) |

### Verify Deskew

1. Display the deskewed source in BDV
2. Navigate through Z - structures should appear straight
3. Check XZ and YZ views for proper geometry

---

## Step 3: Crop Region of Interest (Optional)

For large datasets, crop to save processing time.

### Interactive Crop

```
Menu: Plugins > BigDataViewer-Playground > Sources > Transform > Crop Source
```

1. Navigate to your region of interest
2. Define bounding box
3. Create cropped source

### Benefits of Cropping

- Faster deconvolution
- Smaller output files
- Focus on relevant structures

---

## Step 4: Deconvolve

Improve resolution and contrast using GPU-accelerated deconvolution.

### Prerequisites Check

Verify CLIJ is working:
```
Menu: Plugins > CLIJ2 > CLIJ2 Macro Extensions > CLIJ2_diagnostics()
```

### Run Deconvolution

```
Menu: Plugins > BigDataViewer-Playground > Sources > Process > CLIJ2 FFT Deconvolution
```

| Parameter | Recommended Value |
|-----------|-------------------|
| Source | Deskewed (and cropped) source |
| PSF | Your measured PSF, or synthetic |
| Iterations | 10-20 for Richardson-Lucy |
| Regularization | Start with 0.001 |

### PSF Options

| PSF Type | When to Use |
|----------|-------------|
| Measured PSF | Best quality, requires bead imaging |
| Synthetic PSF | Convenient, good results |
| No PSF | Skip deconvolution if not needed |

### Deconvolution Tips

- Start with fewer iterations, increase if needed
- Monitor GPU memory usage
- Process timepoints in batches for long timelapses

---

## Step 5: Export

Save processed data for downstream analysis.

### Export to OME-TIFF

```
Menu: Plugins > BigDataViewer-Playground > Sources > Export > Export to OME-TIFF
```

| Parameter | Recommendation |
|-----------|----------------|
| Compression | LZW for good balance |
| Timepoints | All or selected range |
| Resolution | Full resolution for analysis |

### Export to XML/HDF5

For continued use in BigDataViewer:

```
Menu: Plugins > BigDataViewer-Playground > Sources > Export > Export to XML/HDF5
```

Benefits: Fast random access, multi-resolution pyramids.

---

## Step 6: Quality Control

### Check Results

1. Open exported data
2. Compare with original (before/after)
3. Verify:
   - Geometry is correct (not sheared)
   - Resolution improved (if deconvolved)
   - All timepoints processed

### Visual Comparison

Use synchronized BDV windows to compare:
```
Menu: Plugins > BigDataViewer-Playground > Synchronize Views
```

---

## Expected Output

After completing this workflow:

- ✅ Isotropic, deskewed data
- ✅ Cropped to region of interest (optional)
- ✅ Deconvolved for improved resolution (optional)
- ✅ Exported in analysis-ready format

---

## Processing Strategies for Large Data

### Memory Management

| Strategy | When to Use |
|----------|-------------|
| Process all at once | Small datasets, enough GPU RAM |
| Process by timepoint | Large timelapses |
| Process by tile | Tiled acquisitions |

### Batch Processing

For very long timelapses, consider scripting:

```groovy
// Process each timepoint individually
for (t in 0..numTimepoints-1) {
    // Deskew
    // Deconvolve
    // Export
}
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Still sheared after deskew | Wrong angle parameter | Check microscope angle setting |
| GPU out of memory | Volume too large | Crop smaller region or tile |
| Deconvolution artifacts | Too many iterations | Reduce iterations, add regularization |
| Wrong orientation | Direction parameter wrong | Try opposite direction setting |
| Slow processing | CPU fallback | Verify GPU is being used |

---

## Related Topics

- [LLS7 Dataset Support](../special_datasets/lls7.md)
- [Deconvolution](../processing_images/deconvolution.md)
- [Export Formats](../processing_images/export_formats.md)
