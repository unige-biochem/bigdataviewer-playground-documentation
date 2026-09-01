# Warpy: Large 2D Image Registration

**Expected duration:** ~90 minutes
**Sample data:** [Zenodo dataset](https://doi.org/10.5281/zenodo.5675686)
**Publication:** [Warpy paper](https://doi.org/10.3389/fcomp.2021.780026)

## Goal

Register large 2D whole slide images (WSI) using QuPath and Fiji, then use the registration to:
- Transfer annotations between images
- Create combined multi-modal images
- Reconstruct 3D volumes from serial sections

![Workflow Overview](images/warpy_workflow_overview.jpeg)

## What You'll Learn

| Part | Topic | Duration |
|------|-------|----------|
| 1 | [Installation](installation.md) | 15 min |
| 2 | [Registration with GUI](registration-gui.md) | 30 min |
| 3 | [Automated Registration](registration-automated.md) | 15 min |
| 4 | [Using Registration in QuPath](qupath-usage.md) | 15 min |
| 5 | [Serial Sections Registration](serial-sections.md) | 15 min |

## Documentation

```{toctree}
:maxdepth: 1

installation
registration-gui
registration-automated
qupath-usage
serial-sections
```

## Overview

### Covered in this workshop

- Registration of large 2D images (WSI) in pairs
- Linear transformations (affine: translation, rotation, scaling)
- Non-linear transformations (spline deformations)
- Automated and semi-automated registration
- Transfer of annotations between registered images
- 3D reconstruction from serial sections

### Not covered (not possible in Warpy)

- 2D+t or 3D+t registration
- 3D volume registration

## Workflow Summary

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│ Images in   │ --> │ Register in  │ --> │ Export      │ --> │ Use in       │
│ QuPath      │     │ Fiji         │     │ Transform   │     │ QuPath       │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

1. **QuPath**: Organize images in a project
2. **Fiji**: Open project, perform registration (GUI or scripted)
3. **Export**: Save transformation to QuPath project
4. **QuPath**: Transfer annotations or create combined images

## Prerequisites

Before starting, you'll need:
- QuPath 0.6+ with Warpy extension
- The latest Fiji, with the UNIGE-Biochem update site enabled (this also brings in Elastix for automated registration)

See [Installation](installation.md) for detailed setup instructions.

## Related Tools

- [BigStitcher](https://imagej.net/plugins/bigstitcher/) - For tile stitching
- [WSIReg](https://github.com/NHPatterson/wsireg) - Alternative WSI registration
- [Valis](https://github.com/MathOnco/valis) - Another registration option
