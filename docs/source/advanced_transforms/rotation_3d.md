# 3D Rotation

BigDataViewer Playground provides tools for rotating sources in 3D space around specified axes and center points.

## Overview

3D rotation is useful for:
- Reorienting samples to standard views
- Aligning structures for comparison
- Correcting acquisition orientation
- Creating specific viewing angles

## Rotation Transform

### Command: Rotation 3D Transform

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Transform > Rotation 3D Transform`
**Class**: `ch.epfl.biop.scijava.command.transform.Rotation3DTransformCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Sources to rotate (must be TransformedSource) |
| `rx` | Rotation around X axis (degrees) |
| `ry` | Rotation around Y axis (degrees) |
| `rz` | Rotation around Z axis (degrees) |
| `cx` | X coordinate of rotation center |
| `cy` | Y coordinate of rotation center |
| `cz` | Z coordinate of rotation center |

### Prerequisites

Sources must be wrapped as `TransformedSource` to allow rotation:
- Use `Wrap as TransformedSource` command first if needed
- Some import methods create TransformedSource automatically

---

## Understanding Rotation

### Rotation Axes

| Axis | Effect |
|------|--------|
| **X rotation** | Tilts forward/backward |
| **Y rotation** | Rotates left/right |
| **Z rotation** | Spins in the XY plane |

### Rotation Center

The center point stays fixed during rotation:
- **At origin (0,0,0)**: Rotates around world origin
- **At sample center**: Rotates sample in place
- **At custom point**: Rotates around that point

:::{tip}
To rotate a sample in place, set the rotation center to the sample's center coordinates.
:::

### Rotation Order

Rotations are applied in order: X, then Y, then Z. The final orientation depends on this sequence.

---

## Workflows

### Rotate to Standard Orientation

```
1. Load your 3D dataset
2. Identify current orientation in BDV
3. Determine needed rotation angles
4. Find sample center coordinates
5. Apply 3D rotation with center at sample
6. Verify result
```

### Align Sample with Axis

**Goal**: Make a structure align with Z axis.

```
1. View sample in BDV
2. Measure angle offset from Z axis
3. Apply rotation to correct offset
4. Verify alignment
```

### Create Multiple Views

```
1. Load dataset
2. Apply 0° rotation → front view
3. Apply 90° Y rotation → side view
4. Apply 90° X rotation → top view
5. Compare different perspectives
```

---

## Utility Transforms

### Remove Z Offset

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Transform > Remove Z Offset`
**Class**: `ch.epfl.biop.scijava.command.transform.RemoveZOffsetCommand`

Translates sources so their Z center is at Z=0.

| Parameter | Description |
|-----------|-------------|
| `sacs` | Sources to transform |
| `timepoint` | Timepoint for computing offset |
| `mode` | Mutate (modify) or Append (add layer) |

### Recenter Sources

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Transform > Recenter sources`
**Class**: `ch.epfl.biop.scijava.command.transform.SourcesRecenterCommand`

Moves sources so their center is at specified coordinates.

| Parameter | Description |
|-----------|-------------|
| `sacs` | Sources to recenter |
| `timepoint` | Timepoint for computing |
| `cx`, `cy`, `cz` | Target center coordinates |
| `mode` | Mutate or Append |

---

## Transform Modes

### Mutate vs Append

| Mode | Behavior | Use When |
|------|----------|----------|
| **Mutate** | Modifies existing transform | Correcting orientation permanently |
| **Append** | Adds new transform layer | Preserving original, testing options |

:::{note}
Append mode allows you to undo by removing the appended transform. Mutate permanently changes the transform.
:::

---

## Tips

### Finding Rotation Angles

1. **Visual estimation**: Look at sample in BDV, estimate degrees
2. **Measure in Fiji**: Use angle tool on a 2D slice
3. **Trial and error**: Apply small rotations, adjust

### Finding Sample Center

1. **BDV coordinates**: Place cursor at center, read coordinates
2. **Calculate**: Average of min and max coordinates
3. **Centroid**: From segmentation if available

### Common Rotations

| Goal | Rotation |
|------|----------|
| Flip upside down | 180° X |
| Mirror left-right | 180° Y |
| Rotate 90° clockwise (top view) | 90° Z |
| Tilt forward 45° | 45° X |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Rotation not applied | Sources not TransformedSource | Wrap sources first |
| Sample moves unexpectedly | Wrong rotation center | Set center to sample center |
| Wrong final orientation | Rotation order matters | Adjust angles iteratively |
| Transform accumulates | Multiple rotations applied | Reset or use Mutate mode |

---

## Related Topics

- [Elliptical Transforms](elliptical.md) - Curved coordinate systems
- [Oblique Slicing](oblique_slicing.md) - Arbitrary slice extraction
- [Basic Transformations](../commands/transformations.md) - Affine transforms
