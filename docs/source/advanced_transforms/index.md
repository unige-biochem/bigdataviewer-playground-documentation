# Advanced Transforms

This section covers advanced spatial transformation tools beyond basic affine transforms.

:::{note}
This section is under development. Documentation for advanced transform commands is being added.
:::

## Overview

BigDataViewer Playground provides specialized transformation tools for complex spatial manipulations, particularly useful for samples with non-standard geometries.

## Transform Types

### Elliptical 3D Transforms

Elliptical transforms are designed for samples with cylindrical or ellipsoidal geometry (e.g., embryos, organoids, tubular structures). They allow mapping data to/from an elliptical coordinate system.

**Use Cases:**
- Unwrapping tubular structures
- Projecting spherical/ellipsoidal samples
- Creating standardized views of curved specimens

**Commands:**
- `Elliptic3DTransformCreatorCommand` - Create new elliptical transform
- `Elliptic3DTransformerCommand` - Apply elliptical transform to sources
- `Elliptic3DTransformExporterCommand` - Export transform to JSON
- `Elliptic3DTransformImporterCommand` - Import transform from JSON
- `Optimize3DEllipticalTransformCommand` - Optimize transform parameters
- `DisplayEllipseFromTransformCommand` - Visualize ellipsoid

### 3D Rotation

Interactive 3D rotation tools for reorienting datasets.

**Commands:**
- `Rotation3DTransformCommand` - Interactive 3D rotation

### Oblique Slicing

Extract arbitrarily oriented slices from 3D volumes.

**Commands:**
- `SliceSourceCommand` - Resample sources to oblique slice
- `Rot3DReSampleCommand` - 3D resampling using ROI points

### Utility Transforms

**Commands:**
- `RemoveZOffsetCommand` - Remove Z offset from sources
- `SourcesRecenterCommand` - Recenter sources to specified coordinates
- `EditSourcesWarpingCommand` - Edit warping transform with BigWarp

## Planned Documentation

The following pages will be added:

- Elliptical transform tutorial with use cases
- 3D rotation guide
- Oblique slicing workflow
- Transform export/import for reproducibility

## See Also

- [Basic Transformations](../commands/transformations.md)
- [BigWarp](../commands/bigwarp.md)
