# Special Datasets

This section covers specialized dataset formats and instruments supported by BigDataViewer Playground beyond standard Bio-Formats files.

## Overview

Some imaging systems produce data that requires custom handling. BigDataViewer Playground provides dedicated loaders for these formats:

| Format | Instrument | Key Feature |
|--------|------------|-------------|
| [LLS7](lls7.md) | Zeiss Lattice Light Sheet 7 | Live deskewing |
| [Operetta](operetta.md) | PerkinElmer Operetta | High-content plates |
| [Imaris](imaris.md) | Bitplane Imaris | Native .ims files |
| [BigStitcher](bigstitcher.md) | Zeiss CZI / Stitching | CZI conversion, fusion |

## Documentation

```{toctree}
:maxdepth: 2

lls7
operetta
imaris
bigstitcher
```

## Quick Reference

### Zeiss LLS7 (Lattice Light Sheet)

**When to use:** Opening Zeiss LLS7 CZI files that need deskewing.

```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Zeiss LLS7]
```

Features:
- Automatic live deskewing
- 3D cropping of deskewed data
- Non-destructive (original data unchanged)

### PerkinElmer Operetta

**When to use:** Opening high-content screening data from Operetta systems.

```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Operetta]
```

Features:
- Multi-well plate support
- Multi-field positioning
- Display settings control

### Imaris Files

**When to use:** Opening Bitplane Imaris `.ims` files without conversion.

```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Imaris]
```

Features:
- Native multi-resolution support
- Multi-channel handling
- Time-series support

### BigStitcher Integration

**When to use:** Preparing CZI files for stitching or exporting fused datasets.

```
CZI to BigStitcher: Plugins > BigDataViewer-Playground > BDVDataset > Edit > Make CZI Dataset for BigStitcher
Fuse to OME-TIFF:   Plugins > BigDataViewer-Playground > BDVDataset > Fuse a BigStitcher dataset to OME-Tiff
```

Features:
- CZI format conversion
- BigStitcher compatibility
- Pyramidal OME-TIFF export

## Choosing the Right Loader

| Your Data | Recommended Loader |
|-----------|-------------------|
| Zeiss LLS7 CZI with skewed data | LLS7 loader |
| Zeiss CZI for stitching | CZI to BigStitcher |
| Zeiss CZI (standard) | Bio-Formats bridge |
| PerkinElmer Operetta | Operetta loader |
| Bitplane .ims files | Imaris loader |
| Already stitched in BigStitcher | BigStitcher fusion |

## See Also

- [Opening Images](../opening_images/opening_images.md) - Standard import methods
- [Fusion](../processing_images/fusion.md) - Fusing stitched datasets
- [Export Formats](../processing_images/export_formats.md) - Output options
