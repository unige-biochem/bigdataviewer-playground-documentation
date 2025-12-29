# Registration

This section covers image registration workflows in BigDataViewer Playground, from manual landmark-based registration to fully automated methods.

## Overview

Image registration aligns two or more images so that corresponding features overlap. BigDataViewer Playground provides multiple approaches:

| Method | Best For | Speed |
|--------|----------|-------|
| **BigWarp** | Maximum control, complex deformations | Manual |
| **SIFT** | Different modalities, large misalignment | Fast |
| **Elastix** | Similar modalities, local deformations | Medium |
| **Warpy Workflow** | Combining methods, QuPath integration | Flexible |

## Documentation

```{toctree}
:maxdepth: 2

concepts
warpy_workflow
automated_registration
```

## Quick Start

### For Simple Alignment

Use [BigWarp](../commands/bigwarp.md) directly:
1. Select fixed and moving sources
2. Run `BigWarp - Launch BigWarp`
3. Add landmarks and apply transform

### For Complex Registration

Use the [Warpy Workflow](warpy_workflow.md):
1. Create a registration pair
2. Center the images
3. Apply automated registration (SIFT/Elastix)
4. Refine with BigWarp if needed
5. Export to QuPath or OME-TIFF

## Choosing a Method

### By Use Case

| Use Case | Recommended Approach |
|----------|---------------------|
| Quick manual alignment | BigWarp with few landmarks |
| H&E to immunofluorescence | SIFT affine (with intensity inversion) |
| Serial sections (same stain) | Elastix affine + spline |
| Whole-slide to QuPath | Warpy workflow with QuPath export |
| Atlas registration | BigWarp with many landmarks |

### By Image Characteristics

| Characteristic | Method |
|---------------|--------|
| Clear features, texture | SIFT |
| Smooth, similar intensities | Elastix |
| Different modalities | SIFT or manual BigWarp |
| Local tissue distortion | Elastix spline or BigWarp |

## Section Contents

### [Registration Concepts](concepts.md)
Learn about transform types, registration methods, and when to use each approach.

### [Warpy Workflow](warpy_workflow.md)
Step-by-step tutorial for the pair registration workflow, from creating pairs to exporting results.

### [Automated Registration](automated_registration.md)
Detailed guide to SIFT and Elastix registration methods, parameters, and troubleshooting.

### [BigWarp Commands](../commands/bigwarp.md)
Reference for manual landmark-based registration using BigWarp.

## Command Quick Reference

### Pair Registration (Warpy)

| Command | Purpose |
|---------|---------|
| `Create registration pair` | Create fixed/moving pair |
| `Registration pair - Add GUI` | Open interactive viewer |
| `Register Pair - Center` | Rough alignment |
| `Register Pair 2D - Sift Affine` | Automated SIFT |
| `Register Pair 2D - Elastix Affine` | Automated Elastix affine |
| `Register Pair 2D - Elastix Spline` | Automated Elastix deformable |
| `Register Pair 2D - BigWarp Spline` | Manual BigWarp |
| `Register Pair - Export to QuPath` | Export to QuPath project |
| `Register Pair - Export to OME-TIFF` | Export as OME-TIFF |

### Direct Registration

| Command | Purpose |
|---------|---------|
| `BigWarp - Launch BigWarp` | Direct BigWarp launch |
| `Wizard Align Slides (2D)` | Interactive registration wizard |

## See Also

- [Transformations](../commands/transformations.md) - Basic affine transforms
- [Import & Export](../commands/import_export.md) - Saving registered results
