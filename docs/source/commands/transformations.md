# Transformations

BigDataViewer Playground provides several ways to transform sources spatially. Transformations are applied non-destructively - the original data is preserved and transformations are computed on-the-fly during display.

## Types of Transformations

| Type | Use Case |
|------|----------|
| **Basic** | Simple rotations (90°) and flips |
| **Affine** | General linear transforms (rotation, scaling, shearing, translation) |
| **Manual** | Interactive alignment using mouse/keyboard |
| **Resampling** | Change voxel size or resolution |

---

## Basic Transformations

### Rotate and Flip

**Command**: `Sources - Basic transformation (rotate/flip)`
**Class**: `sc.fiji.bdvpg.scijava.command.source.BasicTransformerCommand`

Performs simple geometric transformations: 90° rotations or mirror flips along the X, Y, or Z axis.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to transform |
| `axis` | Axis for the transformation (X, Y, or Z) |
| `type` | Type of transformation (Rotate or Flip) |
| `globalchange` | If true, transform relative to world origin (0,0,0). If false, transform around each source's center |
| `initimepoint` | Starting timepoint (0-based) |
| `ntimepoints` | Number of timepoints to transform |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Before/after showing a flip transformation -->

### Understanding Global vs Local Transforms

- **Global transform** (`globalchange = true`): The transformation is applied relative to the world coordinate origin. Useful when aligning multiple sources to a common reference frame.

- **Local transform** (`globalchange = false`): The transformation is applied around each source's center. The source rotates/flips in place without changing its overall position.

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Diagram showing difference between global and local transformations -->

:::{tip}
Use local transforms when you want to flip or rotate an individual source without moving it. Use global transforms when aligning sources to each other.
:::

---

## Affine Transformations

### Apply Affine Transform

**Command**: `Sources - Apply affine transformation`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourceTransformerCommand`

Applies a full 3D affine transformation to sources. An affine transformation can express any combination of rotation, scaling, shearing, and translation.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to transform |
| `m00`, `m01`, `m02` | First row of rotation/scale matrix |
| `m10`, `m11`, `m12` | Second row of rotation/scale matrix |
| `m20`, `m21`, `m22` | Third row of rotation/scale matrix |
| `tx`, `ty`, `tz` | Translation vector |
| `matrixCsv` | Alternative: matrix as comma-separated values |
| `initimepoint` | Starting timepoint |
| `ntimepoints` | Number of timepoints |

### Affine Matrix Format

The transformation is specified as a 3x4 matrix:

```
| m00  m01  m02  tx |
| m10  m11  m12  ty |
| m20  m21  m22  tz |
```

**Common transformations**:

| Transformation | Matrix |
|---------------|--------|
| Identity (no change) | `1,0,0,0,1,0,0,0,1,0,0,0` |
| Scale by 2x | `2,0,0,0,2,0,0,0,2,0,0,0` |
| Translate by (10,20,30) | `1,0,0,0,1,0,0,0,1,10,20,30` |
| Rotate 90° around Z | `0,-1,0,1,0,0,0,0,1,0,0,0` |

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script demonstrating common affine transformations -->

:::{note}
The `matrixCsv` parameter allows you to paste transformation matrices from other software. The format is: `m00,m01,m02,m10,m11,m12,m20,m21,m22,tx,ty,tz`
:::

---

## Manual Registration

### Interactive Manual Transform

**Command**: `Sources - Manual transform`
**Class**: `sc.fiji.bdvpg.scijava.command.source.ManualTransformCommand`

Enables interactive manual transformation of sources using mouse and keyboard controls. This is useful for rough alignment before applying more precise registration methods.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvh` | BDV window to use for transformation |
| `sacs` | Source(s) to transform |
| `mode` | Transformation mode |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Manual transform mode active in BDV -->

### How Manual Transform Works

1. The selected sources are put into "moving" mode
2. The viewer perspective shifts to the reference frame of the moving sources
3. Use mouse drag to translate and rotate the sources
4. Press **Enter** to confirm or **Escape** to cancel

:::{note}
During manual transformation, the moving sources appear stationary while the "fixed" reference appears to move. This is because you are placed in the coordinate system of the moving sources.
:::

<!-- TODO:MISSING_CONTENT: [type: example] - Step-by-step guide for manual alignment -->

:::{tip}
For precise registration, use manual transform for initial rough alignment, then use [BigWarp](bigwarp.md) for fine-tuning.
:::

---

## Resampling

### Resample Sources

**Command**: `Sources - Resample`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourcesResamplerCommand`

Creates new sources resampled to match the voxel grid of a model source. This is a powerful tool for:
- Changing voxel size
- Aligning sources to a common grid
- Creating isotropic versions of anisotropic data
- Downsampling for faster processing

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to resample |
| `model` | Model source defining the target voxel grid |
| `name` | Name for the resampled source(s) |
| `interpolate` | Use interpolation (smoother) or nearest-neighbor |
| `reusemipmaps` | Re-use existing multi-resolution pyramid |
| `defaultmipmaplevel` | MipMap level if not reusing (0 = full resolution) |
| `cache` | Cache resampled data for faster repeat access |

**Output**:
- `sacs_out`: Resampled source(s)

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Comparison of original and resampled source -->

### Use Cases

#### Converting Anisotropic to Isotropic Data

If your source has anisotropic voxels (e.g., 0.5 x 0.5 x 2.0 µm), you can resample to isotropic voxels by using a model source with the desired voxel size.

<!-- TODO:MISSING_CONTENT: [type: script] - Script demonstrating anisotropic to isotropic conversion -->

#### Aligning Multiple Sources to a Common Grid

When sources have different voxel sizes or orientations, resampling them to a common model ensures they share the same coordinate grid for further processing.

#### Downsampling for Processing

For computationally intensive operations, resample to a coarser grid first, then apply the result to the full-resolution data.

:::{tip}
Enable `cache` when you will access the resampled data multiple times. Disable it for one-time operations to save memory.
:::

:::{note}
Resampling creates a virtual source - the actual resampling is computed on-demand. For permanent resampling, export the result using the [export commands](import_export.md).
:::

---

## Transformation Pipeline

A typical transformation workflow:

1. **Assess orientation**: Determine if basic flips/rotations are needed
2. **Apply basic transforms**: Use `BasicTransformerCommand` for 90° corrections
3. **Rough alignment**: Use `ManualTransformCommand` to approximately align sources
4. **Fine registration**: Use [BigWarp](bigwarp.md) for precise alignment
5. **Resample**: Use `SourcesResamplerCommand` to create aligned outputs

<!-- TODO:MISSING_CONTENT: [type: script] - Complete transformation pipeline example -->

---

## Summary

| Command | Purpose |
|---------|---------|
| `BasicTransformerCommand` | 90° rotations and flips |
| `SourceTransformerCommand` | General affine transformations |
| `ManualTransformCommand` | Interactive manual alignment |
| `SourcesResamplerCommand` | Resample to new voxel grid |
