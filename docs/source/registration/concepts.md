# Registration Concepts

This page explains the core concepts behind image registration in BigDataViewer Playground.

## What is Image Registration?

Image registration is the process of aligning two or more images so that corresponding features overlap. In the context of BigDataViewer Playground, registration typically involves:

- **Fixed image**: The reference image that stays stationary
- **Moving image**: The image that will be transformed to align with the fixed image
- **Transform**: The mathematical function that maps coordinates from the moving image to the fixed image

## Types of Transforms

### Rigid Transforms

Rigid transforms preserve distances and angles. They include:
- **Translation**: Shifting the image in X, Y, and/or Z
- **Rotation**: Rotating the image around one or more axes

Use rigid transforms when images differ only in position and orientation.

### Affine Transforms

Affine transforms extend rigid transforms with:
- **Scaling**: Changing the size (uniformly or per-axis)
- **Shearing**: Skewing the image

Use affine transforms when images have different magnifications or minor distortions.

### Non-rigid (Deformable) Transforms

Non-rigid transforms allow local deformations:
- **Thin-plate spline**: Smooth deformation based on control points
- **B-spline**: Deformation controlled by a grid of control points

Use non-rigid transforms for:
- Tissue sections with local distortions
- Histology alignment
- Atlas registration

## Registration Methods in BDV Playground

### Manual Landmark-Based (BigWarp)

**When to use**: When automatic methods fail or for maximum control.

Place corresponding points (landmarks) on both images. The transform is computed to minimize the distance between landmark pairs.

- **Pros**: Works for any image type, handles large deformations
- **Cons**: Time-consuming, requires expertise

See: [Registration with BigWarp](../commands/bigwarp.md)

### Automated Feature-Based (SIFT)

**When to use**: Images with clear, distinctive features.

SIFT (Scale-Invariant Feature Transform) automatically detects and matches features between images.

- **Pros**: Fast, automatic, good for images with texture
- **Cons**: May fail on smooth or repetitive images

### Automated Intensity-Based (Elastix)

**When to use**: Images with similar intensity patterns.

Elastix optimizes the transform by maximizing similarity between image intensities.

- **Pros**: Works well for similar modalities, can handle affine and deformable registration
- **Cons**: Requires parameter tuning, may get stuck in local minima

## Registration Workflows

### Pair Registration (Warpy)

The pair registration workflow provides a structured approach:

1. **Create pair**: Define fixed and moving sources
2. **Center**: Roughly align images
3. **Automated registration**: Apply SIFT or Elastix
4. **Manual refinement**: Fine-tune with BigWarp if needed
5. **Export**: Save results to QuPath or OME-TIFF

See: [Warpy Workflow](warpy_workflow.md)

### Direct Registration

For simple cases, you can directly launch BigWarp with fixed and moving sources:

1. Open fixed and moving images in BDV Playground
2. Launch BigWarp from the menu
3. Add landmarks and apply transform
4. Export registered result

See: [Registration with BigWarp](../commands/bigwarp.md)

## Choosing a Registration Strategy

| Scenario | Recommended Approach |
|----------|---------------------|
| Simple rotation/translation | Manual transform or few BigWarp landmarks |
| Different magnifications | SIFT or Elastix affine |
| Similar modalities | Elastix (intensity-based) |
| Different modalities (e.g., fluorescence + brightfield) | SIFT or manual BigWarp |
| Local tissue deformation | Elastix spline or BigWarp |
| Complex deformations | BigWarp with many landmarks |
| QuPath integration needed | Warpy workflow |

## Tips for Successful Registration

1. **Start with coarse alignment**: Use centering or rough manual alignment before automated methods
2. **Choose appropriate resolution**: Higher resolution isn't always better; 1-2 microns/pixel often works well
3. **Use multiple channels wisely**: Select channels with clear features for registration
4. **Iterate if needed**: Combine methods (e.g., SIFT affine followed by Elastix spline)
5. **Validate visually**: Always check the registration result before exporting

## Next Steps

- [Warpy Workflow](warpy_workflow.md) - Step-by-step pair registration tutorial
- [Automated Registration](automated_registration.md) - SIFT and Elastix guide
- [Registration with BigWarp](../commands/bigwarp.md) - Manual landmark registration
