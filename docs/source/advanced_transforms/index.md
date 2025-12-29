# Advanced Transforms

This section covers advanced spatial transformation tools beyond basic affine transforms.

## Overview

BigDataViewer Playground provides specialized transformations for complex spatial manipulations:

| Transform | Use Case | Key Feature |
|-----------|----------|-------------|
| [Elliptical](elliptical.md) | Curved samples (embryos, tubes) | Coordinate system mapping |
| [3D Rotation](rotation_3d.md) | Reorienting datasets | Rotate around any center |
| [Oblique Slicing](oblique_slicing.md) | Arbitrary plane extraction | Cut at any angle |

## Documentation

```{toctree}
:maxdepth: 2

elliptical
rotation_3d
oblique_slicing
```

## Quick Reference

### Elliptical 3D Transforms

**When to use:** Samples with spherical, ellipsoidal, or cylindrical geometry.

```
Create: Plugins > BigDataViewer-Playground > Sources > Transform > New Elliptic 3D Transform
Apply:  Plugins > BigDataViewer-Playground > Sources > Transform > Elliptic 3D Transform Sources
```

Features:
- Map curved surfaces to flat views
- Unwrap tubular structures
- Standardize spherical samples

### 3D Rotation

**When to use:** Reorienting samples to standard views or correcting acquisition angles.

```
Menu: Plugins > BigDataViewer-Playground > Sources > Transform > Rotation 3D Transform
```

Features:
- Rotate around X, Y, Z axes
- Specify rotation center
- Preserve or modify transforms

### Oblique Slicing

**When to use:** Extracting slices at arbitrary angles through 3D volumes.

Features:
- Define plane by points or angles
- Extract 2D slices from 3D data
- Reslice along structures

### Utility Transforms

```
Remove Z Offset: Plugins > BigDataViewer-Playground > Sources > Transform > Remove Z Offset
Recenter:        Plugins > BigDataViewer-Playground > Sources > Transform > Recenter sources
```

## Transform Selection Guide

| Your Goal | Recommended Transform |
|-----------|----------------------|
| Flatten a spherical sample | Elliptical |
| Unwrap a tube | Elliptical (cylindrical) |
| Correct sample tilt | 3D Rotation |
| View along a structure | Oblique Slicing |
| Center sample at origin | Recenter / Remove Z Offset |
| Standardize orientation | 3D Rotation |

## Combining Transforms

Transforms can be combined for complex manipulations:

```
Example: Analyze tilted tubular structure

1. Remove Z Offset → Center in Z
2. 3D Rotation → Align tube with Z axis
3. Elliptical Transform → Unwrap tube surface
4. Export → Analyze flat representation
```

## Tips

### Transform Order Matters

Apply transforms in logical order:
1. **Position first**: Center, remove offsets
2. **Orient second**: Rotation
3. **Map last**: Elliptical or specialized transforms

### Save and Reload

Export transforms to JSON for:
- Reproducibility
- Applying to similar datasets
- Documentation

### Verify Visually

Always check transforms in BDV before exporting:
- Use ellipsoid visualization
- Compare before/after
- Check edge cases

## See Also

- [Basic Transformations](../commands/transformations.md) - Affine transforms
- [BigWarp](../commands/bigwarp.md) - Landmark-based warping
- [Resampling](../processing_images/resampling.md) - Grid resampling
- [Registration](../registration/index.md) - Image alignment
