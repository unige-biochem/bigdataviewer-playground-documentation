# Processing Images

This section covers image processing capabilities in BigDataViewer Playground, including resampling, fusion, deconvolution, and export.

## Overview

BigDataViewer Playground provides powerful processing tools that operate on sources while maintaining lazy evaluation - computations happen on-demand during visualization or export, not immediately when the command is run.

### Key Concepts

- **Lazy processing**: Transforms are applied on-the-fly, no intermediate files created
- **Source-based**: Processing creates new sources that can be visualized and exported
- **Multi-resolution aware**: Operations respect pyramid levels for efficient processing

## Processing Capabilities

| Capability | Description | Source |
|------------|-------------|--------|
| **Resampling** | Change resolution, match grids | bdv-playground |
| **Fusion** | Combine multiple sources | biop-tools |
| **Deconvolution** | GPU-accelerated Richardson-Lucy | biop-tools |
| **Pyramidization** | Generate multi-resolution levels | biop-tools |
| **Export** | Save to OME-TIFF, ImagePlus, XML/HDF5 | both |

## Documentation

```{toctree}
:maxdepth: 2

resampling
fusion
deconvolution
export_formats
```

## Quick Reference

### Resampling

Match a source to a different voxel grid:
1. Select source(s) to resample
2. Select a model source (defines target grid)
3. Run `Sources > Resample`

### Fusion

Combine overlapping sources into one:
1. Select sources to fuse
2. Choose fusion method (average, max, etc.)
3. Run fusion command

### Deconvolution

Apply GPU-accelerated deconvolution:
1. Select source(s) to deconvolve
2. Provide PSF source
3. Configure iterations and tile size
4. Run deconvolution (requires OpenCL GPU)

### Export

Save processed results:
- **OME-TIFF**: Pyramidal, compatible with QuPath
- **ImagePlus**: For ImageJ/Fiji analysis
- **XML/HDF5**: Native BDV format

## See Also

- [Opening Images](../opening_images/opening_images.md) - Import data
- [Visualizing Images](../visualizing_images/visualizing_images.md) - Display options
- [Import & Export Commands](../commands/import_export.md) - Command reference
