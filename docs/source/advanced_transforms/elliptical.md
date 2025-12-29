# Elliptical 3D Transforms

Elliptical transforms map data between Cartesian and ellipsoidal coordinate systems, enabling visualization and analysis of curved biological structures.

## Overview

Many biological samples have curved or tubular geometry:
- Embryos (spherical/ellipsoidal)
- Blood vessels (cylindrical)
- Organoids (spherical)
- Gut tubes (cylindrical)
- Cochlea (spiral)

Elliptical transforms allow you to:
- "Unwrap" curved structures into flat views
- Create standardized projections
- Analyze data in natural coordinates

## Concepts

### Ellipsoidal Coordinate System

An ellipsoid is defined by:
- **Center**: Position in 3D space (cx, cy, cz)
- **Radii**: Size along each axis (rx, ry, rz)
- **Rotation**: Orientation angles (Euler angles)

The transform maps between:
- **Cartesian coordinates**: Standard X, Y, Z
- **Ellipsoidal coordinates**: Angular position on the surface

### Transform Direction

| Direction | Description | Use Case |
|-----------|-------------|----------|
| **Forward** | Cartesian → Ellipsoidal | Unwrap curved surface |
| **Inverse** | Ellipsoidal → Cartesian | Map flat data to surface |

---

## Creating Elliptical Transforms

### Command: New Elliptic 3D Transform

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Transform > New Elliptic 3D Transform`
**Class**: `ch.epfl.biop.scijava.command.transform.Elliptic3DTransformCreatorCommand`

| Parameter | Description |
|-----------|-------------|
| `radius_x` | Radius along first axis |
| `radius_y` | Radius along second axis |
| `radius_z` | Radius along third axis |
| `rotation_x` | Euler rotation around X (radians) |
| `rotation_y` | Euler rotation around Y (radians) |
| `rotation_z` | Euler rotation around Z (radians) |
| `center_x` | X coordinate of ellipse center |
| `center_y` | Y coordinate of ellipse center |
| `center_z` | Z coordinate of ellipse center |

| Output | Description |
|--------|-------------|
| `e3dt` | The created elliptical transform |

### Choosing Parameters

**For spherical samples** (embryos, organoids):
- Set all radii equal: `radius_x = radius_y = radius_z`
- Rotation usually zero

**For cylindrical samples** (tubes, vessels):
- One radius much larger: `radius_z >> radius_x, radius_y`
- Adjust rotation to align with tube axis

**For ellipsoidal samples**:
- Set radii to match sample dimensions
- Measure from your data or estimate

---

## Applying Transforms

### Command: Elliptic 3D Transform Sources

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Transform > Elliptic 3D Transform Sources`
**Class**: `ch.epfl.biop.scijava.command.transform.Elliptic3DTransformerCommand`

| Parameter | Description |
|-----------|-------------|
| `e3dt` | The elliptical transform to apply |
| `sacs_in` | Sources to transform |

### Workflow

```
1. Create elliptical transform with appropriate parameters
2. Select sources to transform
3. Apply transform
4. Visualize transformed (unwrapped) result
```

---

## Visualizing Transforms

### Command: Display Ellipse from Transform

**Class**: `ch.epfl.biop.scijava.command.transform.DisplayEllipseFromTransformCommand`

Creates a visualization source showing the ellipsoid defined by the transform. Useful for:
- Verifying transform parameters
- Aligning transform to sample
- Documentation

---

## Optimizing Transforms

### Command: Optimize 3D Elliptical Transform

**Class**: `ch.epfl.biop.scijava.command.transform.Optimize3DEllipticalTransformCommand`

Automatically adjusts transform parameters to better fit your data.

---

## Saving and Loading Transforms

### Export Transform

**Class**: `ch.epfl.biop.scijava.command.transform.Elliptic3DTransformExporterCommand`

Saves the transform to a JSON file for:
- Reproducibility
- Sharing with collaborators
- Applying to other datasets

### Import Transform

**Class**: `ch.epfl.biop.scijava.command.transform.Elliptic3DTransformImporterCommand`

Loads a previously saved transform from JSON.

---

## Use Cases

### Embryo Surface Projection

**Goal**: Create a flat map of an embryo surface.

```
1. Load 3D embryo dataset
2. Measure approximate center and radius
3. Create spherical transform (equal radii)
4. Apply transform to get unwrapped view
5. Adjust and optimize if needed
```

### Tube Unwrapping

**Goal**: Flatten a cylindrical structure (e.g., gut tube).

```
1. Load tube dataset
2. Identify tube axis orientation
3. Create cylindrical transform (one large radius)
4. Set rotation to align with tube axis
5. Apply transform
6. View as if tube were cut and unrolled
```

### Organoid Analysis

**Goal**: Standardized view of spherical organoids.

```
1. Load organoid dataset
2. Center transform on organoid
3. Set radius to match organoid size
4. Apply transform
5. Compare multiple organoids in standard view
```

---

## Parameter Guide

### Radius Selection

| Sample Type | Radius Strategy |
|-------------|-----------------|
| Perfect sphere | All radii equal |
| Oblate (flattened) | `rz < rx = ry` |
| Prolate (elongated) | `rz > rx = ry` |
| General ellipsoid | Measure each axis |

### Center Determination

Methods to find center:
1. **Manual**: Identify visually in BDV
2. **Centroid**: Calculate from segmentation
3. **Optimization**: Use automatic optimization

### Rotation

Euler angles specify orientation:
- Start with zero rotation
- Adjust if ellipsoid axes don't align with sample
- Use visualization to verify

---

## Tips and Best Practices

### Getting Good Results

1. **Start simple**: Try spherical (equal radii) first
2. **Visualize the ellipsoid**: Verify it fits your sample
3. **Iterate**: Adjust parameters, visualize, repeat
4. **Save transforms**: Export for reproducibility

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Wrong shape | Incorrect radii | Measure sample, adjust radii |
| Misaligned | Wrong rotation | Adjust Euler angles |
| Off-center | Wrong center coordinates | Re-measure center position |
| Distorted output | Sample doesn't fit ellipsoid | Try different radii ratios |

### When Not to Use

Elliptical transforms work best for:
- Samples that approximate ellipsoids
- Consistent geometry across the sample

Consider alternatives for:
- Highly irregular shapes
- Variable geometry
- Very thin structures

---

## Related Topics

- [3D Rotation](rotation_3d.md) - Simple rotation transforms
- [Oblique Slicing](oblique_slicing.md) - Extract arbitrary slices
- [Basic Transformations](../commands/transformations.md) - Affine transforms
- [Resampling](../processing_images/resampling.md) - Grid resampling
