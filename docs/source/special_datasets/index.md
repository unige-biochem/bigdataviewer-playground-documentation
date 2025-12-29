# Special Datasets

This section covers specialized dataset formats and instruments supported by BigDataViewer Playground beyond standard Bio-Formats files.

:::{note}
This section is under development. Documentation for special dataset commands is being added.
:::

## Overview

BigDataViewer Playground includes dedicated support for several specialized imaging systems and formats that require custom handling beyond standard Bio-Formats import.

## Supported Special Formats

### Zeiss LLS7 (Lattice Light Sheet)

The Zeiss LLS7 lattice light sheet microscope produces data that requires deskewing for proper visualization.

**Features:**
- Live deskewing during visualization
- 3D cropping of deskewed data
- Proper handling of LLS7 metadata

**Commands:**
- `LLS7OpenDatasetCommand` - Open LLS7 dataset with live deskewing
- `LLS7CropCommand` - Crop 3D region from LLS7 sources

### PerkinElmer Operetta

High-content screening data from Operetta systems.

**Commands:**
- `OpenOperettaDatasetCommand` - Open Operetta datasets

### Imaris Files

Direct import of Bitplane Imaris `.ims` files.

**Commands:**
- `OpenImarisCommand` - Open Imaris files

### Zeiss CZI to BigStitcher

Convert Zeiss CZI files to BigStitcher-compatible format for stitching workflows.

**Commands:**
- `CreateCZIDatasetCommand` - Create BigStitcher XML from CZI

### BigStitcher Integration

Tools for working with BigStitcher datasets.

**Commands:**
- `DatasetToBigStitcherDatasetCommand` - Convert BDV to BigStitcher format
- `FuseBigStitcherDatasetIntoOMETiffCommand` - Fuse and export to OME-TIFF

## Planned Documentation

The following pages will be added:

- LLS7 workflow guide (opening, deskewing, cropping)
- Operetta dataset handling
- Imaris file import
- BigStitcher integration workflow

## See Also

- [Opening Images](../opening_images/opening_images.md)
- [Import & Export Commands](../commands/import_export.md)
