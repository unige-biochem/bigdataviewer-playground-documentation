# Registration

This section covers image registration workflows in BigDataViewer Playground, from manual landmark-based registration to fully automated methods.

:::{note}
This section is under development. Documentation for registration commands is being added.
:::

## Overview

BigDataViewer Playground provides multiple registration approaches:

- **Manual Registration**: Interactive landmark-based registration using BigWarp
- **Warpy Workflow**: Pair-based registration with GUI for combining manual and automated steps
- **Automated Registration**: SIFT feature matching and Elastix-based registration

## Registration Methods

### Manual Registration (BigWarp)

BigWarp provides interactive landmark-based registration for precise alignment of images. See [BigWarp commands](../commands/bigwarp.md) for the launcher command.

### Warpy Workflow

The Warpy workflow provides a structured approach to registration:

1. Create a registration pair (fixed + moving sources)
2. Apply centering to roughly align images
3. Use automated methods (SIFT, Elastix) for initial alignment
4. Refine with manual landmarks if needed
5. Export results to QuPath or OME-TIFF

**Available Commands:**
- `PairRegistrationCreateCommand` - Create registration pairs
- `PairRegistrationAddGUICommand` - Open interactive GUI
- `PairRegistrationCenterCommand` - Center moving over fixed
- `PairRegistrationSift2DAffineCommand` - SIFT-based 2D affine
- `PairRegistrationElastix2DAffineCommand` - Elastix 2D affine
- `PairRegistrationElastix2DSplineCommand` - Elastix B-spline deformable
- `PairRegistrationBigWarp2DSplineCommand` - Manual landmark spline
- `PairRegistrationExportToOMETIFFCommand` - Export registered images
- `PairRegistrationExportToQuPathCommand` - Export to QuPath

### Automated Registration

For batch processing and automated workflows:

- **SIFT Registration**: Feature-based 2D affine registration
- **Elastix Registration**: Intensity-based affine and deformable registration

## Planned Documentation

The following pages will be added:

- Warpy workflow tutorial
- Elastix registration guide
- SIFT registration guide
- Exporting registration results
- Registration best practices

## See Also

- [BigWarp Commands](../commands/bigwarp.md)
- [Transformations](../commands/transformations.md)
