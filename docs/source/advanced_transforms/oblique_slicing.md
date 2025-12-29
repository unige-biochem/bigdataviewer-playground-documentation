# Oblique Slicing

BigDataViewer Playground allows extraction of arbitrarily oriented slices from 3D volumes, enabling views along any plane.

## Overview

Standard microscopy views show XY, XZ, or YZ planes. Oblique slicing allows:
- Slices at any angle through the volume
- Views along structures oriented arbitrarily
- Reslicing to match anatomical planes
- Creating projection planes aligned to features

## Slice Source Command

### Command: Slice Source

**Class**: `ch.epfl.biop.scijava.command.source.SliceSourceCommand`

Extracts a 2D slice from a 3D volume at arbitrary orientation.

This command resamples the source data onto a defined plane, creating a new 2D source.

---

## 3D Resampling with ROI Points

### Command: Rot3D Resample

**Class**: `ch.epfl.biop.scijava.command.transform.Rot3DReSampleCommand`

Uses interactively placed points to define a resampling plane.

### Workflow

```
1. Open 3D dataset in BDV
2. Navigate to region of interest
3. Use point selection to define plane
4. Apply resampling
5. View resampled slice
```

---

## Concepts

### Defining an Oblique Plane

A plane in 3D space can be defined by:
- **Three points**: Any three non-collinear points define a plane
- **Point and normal**: A point on the plane plus a perpendicular vector
- **Rotation from standard plane**: XY plane rotated by angles

### Slice Orientation

| Standard Plane | Orientation |
|----------------|-------------|
| **XY** | Looking down Z axis (top view) |
| **XZ** | Looking down Y axis (front view) |
| **YZ** | Looking down X axis (side view) |
| **Oblique** | Any other orientation |

---

## Use Cases

### Anatomical Plane Alignment

**Goal**: Extract a slice along an anatomical axis that doesn't match acquisition axes.

```
1. Identify the anatomical structure
2. Place points along the desired plane
3. Extract oblique slice
4. Analyze in the correct orientation
```

### Structure-Aligned Views

**Goal**: View a structure along its long axis.

```
1. Identify structure orientation
2. Define plane parallel to structure
3. Extract slice
4. View structure in optimal orientation
```

### Curved Section Following

**Goal**: Follow a curved structure through the volume.

For complex curves, consider:
1. Multiple oblique slices along the curve
2. Elliptical transforms for continuous unwrapping
3. Maximum intensity projection along the curve

---

## Comparison with BDV Navigation

### BDV Rotation vs Oblique Slice

| Approach | BDV Rotation | Oblique Slice |
|----------|--------------|---------------|
| What changes | View angle | Creates new source |
| Data extraction | No | Yes (2D result) |
| Export | Current view | Defined plane |
| Reproducibility | Manual | Parameterized |

### When to Use Each

**Use BDV rotation** for:
- Interactive exploration
- Quick visualization
- Finding the right orientation

**Use oblique slicing** for:
- Quantitative analysis
- Reproducible extraction
- Defined plane export

---

## Workflow Examples

### Extract Single Oblique Slice

```
1. Load 3D dataset
2. Navigate in BDV to desired plane
3. Define slice plane (points or angles)
4. Apply slice extraction
5. Export 2D result if needed
```

### Create Serial Oblique Sections

```
1. Define reference plane
2. Extract slice at that plane
3. Offset plane by step distance
4. Extract next slice
5. Repeat for series
```

### Reslice Along Structure

```
1. Identify structure axis
2. Define plane perpendicular to axis
3. Extract cross-section
4. Move along axis for serial sections
```

---

## Tips

### Choosing Slice Orientation

1. **Follow the structure**: Align with anatomical features
2. **Consider downstream analysis**: What orientation is needed?
3. **Match conventions**: Use standard anatomical planes when possible

### Quality Considerations

| Factor | Impact | Recommendation |
|--------|--------|----------------|
| Source resolution | Limits slice quality | Use highest resolution level |
| Interpolation | Affects smoothness | Enable for smooth slices |
| Slice thickness | Single plane vs projection | Match to analysis needs |

### Handling Thick Slices

For thick oblique sections:
1. Extract multiple parallel slices
2. Project (max, average, sum)
3. Or use slab projection in BDV

---

## Integration with Other Tools

### Export for Analysis

After extracting an oblique slice:
1. Export to ImagePlus for Fiji analysis
2. Save as TIFF for external tools
3. Use in further BDV Playground processing

### Combine with Registration

For registered datasets:
1. Register images first
2. Extract corresponding oblique slices
3. Compare aligned views

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Slice is black/empty | Plane outside data bounds | Verify plane intersects volume |
| Poor quality | Low resolution or no interpolation | Use higher resolution, enable interpolation |
| Wrong orientation | Plane definition incorrect | Re-check points or angles |
| Partial slice | Plane clips volume edges | Adjust plane position |

---

## Related Topics

- [3D Rotation](rotation_3d.md) - Rotate entire volumes
- [Elliptical Transforms](elliptical.md) - Curved surface unwrapping
- [Resampling](../processing_images/resampling.md) - General resampling
- [Export Formats](../processing_images/export_formats.md) - Save extracted slices
