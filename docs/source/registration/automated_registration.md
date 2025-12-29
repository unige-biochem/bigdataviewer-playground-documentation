# Automated Registration

This guide covers automated registration methods available in BigDataViewer Playground: SIFT feature-based registration and Elastix intensity-based registration.

## Overview

Automated registration methods can align images without manual landmark placement. They work best when:
- Images have some overlap
- Images have similar or complementary features
- A reasonable initial alignment exists

## Prerequisites

### Elastix Requirements

Elastix registration requires the Elastix software to be installed and configured:

1. Download Elastix from [elastix.lumc.nl](https://elastix.lumc.nl/)
2. Install and configure the path in Fiji
3. The PTBIOP update site includes Elastix wrappers

:::{note}
Elastix is an external tool. Registration speed depends on your system configuration.
:::

### SIFT Requirements

SIFT registration is built into Fiji via the MPICBG library. No additional installation is required.

---

## SIFT Registration

### How SIFT Works

SIFT (Scale-Invariant Feature Transform):
1. Detects distinctive keypoints in both images
2. Computes descriptors for each keypoint
3. Matches keypoints between images
4. Estimates transform from matched pairs
5. Uses RANSAC to reject outliers

### When to Use SIFT

**Good for:**
- Images with texture and distinctive features
- Different staining methods (H&E vs. immunofluorescence)
- Large initial misalignment
- Quick rough alignment

**Not ideal for:**
- Smooth, featureless images
- Very repetitive structures
- When sub-pixel precision is needed

### SIFT Parameters

#### Within Pair Registration

**Command**: `Register Pair 2D - Sift Affine`

| Parameter | Description | Recommendations |
|-----------|-------------|-----------------|
| `pixel_size_micrometer` | Resolution for feature detection | 1-4 microns for whole-slide images |
| `channels_fixed_csv` | Fixed image channels | Use channel with most features |
| `channels_moving_csv` | Moving image channels | Match modality if possible |
| `invert_moving` | Invert moving image | Enable for opposite contrast |
| `invert_fixed` | Invert fixed image | Enable for opposite contrast |
| `bounds` | Region of interest | Use "intersection" for overlapping regions |

### SIFT Tips

1. **Choose informative channels**: Select channels with clear tissue structure
2. **Adjust pixel size**:
   - Too fine: slow, may find too many features
   - Too coarse: may miss important features
   - 2-4 microns is often a good starting point
3. **Use intensity inversion**: When comparing brightfield (dark features) to fluorescence (bright features)
4. **Check the result**: SIFT can fail silently - always verify visually

---

## Elastix Registration

### How Elastix Works

Elastix optimizes a transform to maximize image similarity:
1. Resamples both images to a common grid
2. Computes a similarity metric (e.g., mutual information)
3. Iteratively adjusts transform parameters
4. Uses multi-resolution pyramid for robustness

### When to Use Elastix

**Good for:**
- Images with similar intensity patterns
- Same or similar staining
- When affine alignment is insufficient
- Deformable (non-rigid) registration

**Not ideal for:**
- Very different modalities
- Large initial misalignment (run SIFT first)
- Images with very different intensity ranges

### Elastix Transform Types

#### Affine Registration

**Command**: `Register Pair 2D - Elastix Affine`

Estimates a global affine transform (translation, rotation, scaling, shearing).

| Parameter | Description | Recommendations |
|-----------|-------------|-----------------|
| `pixel_size_micrometer` | Resolution for registration | 2-10 microns depending on image size |
| `channels_fixed_csv` | Fixed image channels | Use similar stains if available |
| `channels_moving_csv` | Moving image channels | Match with fixed channels |
| `show_imageplus_registration_result` | Show result | Enable for verification |

#### B-Spline Deformable Registration

**Command**: `Register Pair 2D - Elastix Spline`

Adds local deformations using a B-spline grid.

| Parameter | Description | Recommendations |
|-----------|-------------|-----------------|
| `nb_control_points_x` | B-spline grid density | Start with 4-8, increase if needed |
| `pixel_size_micrometer` | Resolution | 2-5 microns for local corrections |

:::{warning}
Always run affine registration before spline registration. Starting with deformable registration on unaligned images often fails.
:::

### Elastix Tips

1. **Start coarse, refine fine**: Begin with low resolution, then increase
2. **Affine before spline**: Global alignment first, then local corrections
3. **Reasonable control points**:
   - Too few: won't capture local deformation
   - Too many: may overfit, slow computation
4. **Check for divergence**: If registration looks worse, the optimization may have diverged

---

## Combining Methods

A robust registration workflow often combines multiple methods:

### Recommended Workflow

```
1. Center (rough alignment)
      ↓
2. SIFT Affine (handles large misalignment)
      ↓
3. Elastix Affine (refines alignment)
      ↓
4. Elastix Spline (local corrections)
      ↓
5. BigWarp (manual refinement if needed)
```

### When to Add Each Step

| Situation | Action |
|-----------|--------|
| Large misalignment | Add SIFT after centering |
| Sub-pixel precision needed | Add Elastix affine after SIFT |
| Local tissue distortion | Add Elastix spline |
| Remaining errors | Add BigWarp for manual correction |

---

## Standalone Registration Commands

In addition to the Pair Registration workflow, there are standalone commands for direct registration:

### Wizard 2D Whole Scan Register

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Wizard Align Slides (2D)`

An interactive wizard that guides through registration steps:

| Parameter | Description |
|-----------|-------------|
| `fixed` | Fixed reference source |
| `moving` | Moving source |
| `sources_to_transform` | All sources to transform |
| `center_moving_image` | Apply initial centering |
| `manual_rigid_registration` | Include manual rigid step |
| `automated_affine_registration` | Include automated affine |
| `automated_spline_registration` | Include automated spline |
| `manual_spline_registration` | Include BigWarp step |
| `coarse_pixel_size_um` | Pixel size for coarse registration |
| `precise_pixel_size_um` | Pixel size for fine registration |

### QuPath-Specific Commands

For QuPath projects, additional Warpy commands are available:

- `QuPath - Create Warpy Registration`: Interactive registration wizard
- `QuPath - Create Warpy Multiscale Registration`: Automated multiscale registration
- `QuPath - Edit Warpy Registration`: Edit existing registration
- `QuPath - Export Warpy Registered Image`: Export to OME-TIFF

---

## Troubleshooting

### SIFT Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| No matches found | Features too different | Try intensity inversion, different channels |
| Wrong matches | Repetitive structures | Reduce pixel size, add constraints |
| Registration offset | Calibration mismatch | Verify pixel sizes are correct |

### Elastix Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Optimization diverges | Bad initial alignment | Run SIFT or manual alignment first |
| Registration too smooth | Not enough control points | Increase `nb_control_points_x` |
| Registration too noisy | Too many control points | Decrease control points |
| Very slow | High resolution | Increase `pixel_size_micrometer` |

### General Tips

1. **Check calibration**: Both images must have correct pixel size metadata
2. **Verify initial alignment**: Centering or rough manual alignment helps
3. **Use appropriate resolution**: Don't register at full resolution if not needed
4. **Validate results**: Always check visually before exporting

---

## Performance Considerations

| Factor | Impact | Recommendation |
|--------|--------|----------------|
| Image size | Larger = slower | Use appropriate pixel size |
| Resolution levels | More = slower | 3-4 levels usually sufficient |
| Control points | More = slower (spline) | Start with 4-8 |
| Threads | More = faster | Use available CPU cores |

---

## Related Resources

- [Registration Concepts](concepts.md)
- [Warpy Workflow](warpy_workflow.md)
- [Registration with BigWarp](../commands/bigwarp.md)
