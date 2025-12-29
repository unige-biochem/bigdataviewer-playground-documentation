# Warpy Workflow

The Warpy workflow provides a structured approach to image registration using registration pairs. This tutorial walks through the complete workflow from creating a pair to exporting results.

## Overview

The Warpy workflow consists of these steps:

1. **Create** a registration pair (fixed + moving sources)
2. **Open GUI** for interactive control
3. **Center** moving sources on fixed sources
4. **Register** using automated or manual methods
5. **Refine** if needed
6. **Export** results to QuPath or OME-TIFF

## Prerequisites

- Images loaded in BDV Playground
- For QuPath export: images from a QuPath project

## Step-by-Step Guide

### Step 1: Create a Registration Pair

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Create registration pair`

| Parameter | Description |
|-----------|-------------|
| `fixed_sources` | Reference source(s) that stay stationary |
| `moving_sources` | Source(s) to be aligned to the fixed reference |
| `registration_name` | Unique name for this pair (e.g., "slide1_HE_to_IF") |

:::{tip}
Select sources from the BDV Playground window before running the command. The selection widget will use your selection.
:::

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Create registration pair dialog -->

---

### Step 2: Open the Registration GUI

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Registration pair - Add GUI`

This opens a BigDataViewer window showing both fixed and moving sources with registration controls.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair created in Step 1 |

The GUI provides:
- Visualization of both sources overlaid
- Access to registration commands via buttons or menu
- Real-time preview of registration results

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Registration GUI with overlay view -->

---

### Step 3: Center the Images

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair - Center moving sources on fixed sources`

This applies a translation to roughly align the moving sources with the fixed sources. It uses the bounding boxes of both sources to compute the centering transform.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to center |

:::{note}
Centering is recommended as the first step for most registrations. It helps automated methods work better by starting from a reasonable alignment.
:::

---

### Step 4: Apply Registration

You can apply one or more registration steps. Common approaches:

#### Option A: Automated SIFT Affine

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair 2D - Sift Affine`

Best for images with distinctive features (texture, landmarks).

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to register |
| `bounds` | Region of interest: intersection, union, or custom |
| `channels_fixed_csv` | Channels to use from fixed image (e.g., "0" or "0,1") |
| `channels_moving_csv` | Channels to use from moving image |
| `pixel_size_micrometer` | Resolution for registration (e.g., 2.0) |
| `invert_moving` | Invert moving image intensities |
| `invert_fixed` | Invert fixed image intensities |

:::{tip}
If images have inverted contrast (e.g., brightfield vs. fluorescence), try enabling intensity inversion.
:::

#### Option B: Automated Elastix Affine

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair 2D - Elastix Affine`

Best for images with similar intensity patterns.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to register |
| `bounds` | Region of interest |
| `channels_fixed_csv` | Channels to use from fixed image |
| `channels_moving_csv` | Channels to use from moving image |
| `pixel_size_micrometer` | Resolution for registration |
| `show_imageplus_registration_result` | Display result for verification |

#### Option C: Deformable Elastix Spline

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair 2D - Elastix Spline`

Adds local deformations on top of affine alignment.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to register |
| `nb_control_points_x` | Number of B-spline control points (more = finer deformation) |
| `bounds` | Region of interest |
| `channels_fixed_csv` | Channels to use |
| `channels_moving_csv` | Channels to use |
| `pixel_size_micrometer` | Resolution for registration |

:::{note}
Run affine registration first, then apply spline registration for local corrections.
:::

#### Option D: Manual BigWarp

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair 2D - BigWarp Spline`

Opens BigWarp for interactive landmark placement.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to register |

See [Registration with BigWarp](../commands/bigwarp.md) for detailed BigWarp usage.

---

### Step 5: Refine if Needed

#### Edit Last Registration

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair - Edit last registration`

Re-opens the last registration step for adjustment (e.g., add more BigWarp landmarks).

#### Remove Last Registration

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Register Pair - Remove last registration`

Removes the last registration step if it didn't work well.

:::{tip}
You can chain multiple registration steps. For example:
1. Center
2. SIFT affine
3. Elastix spline
4. BigWarp for final refinement
:::

---

### Step 6: Export Results

#### Export to QuPath

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Register Pair - Export registration to QuPath project`

Saves the registration transforms to the QuPath project for use with the Warpy QuPath extension.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to export |
| `allow_overwrite` | Overwrite existing registration files |

#### Export to OME-TIFF

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Register Pair - Export registration to OME-TIFF`

Exports the registered images as a pyramidal OME-TIFF file.

| Parameter | Description |
|-----------|-------------|
| `registration_pair` | The pair to export |
| `interpolate` | Use interpolation when resampling |
| `channels_fixed_csv` | Fixed channels to include ("*" for all, empty for none) |
| `channels_moving_csv` | Moving channels to include |
| `file_path` | Output file path |
| `n_resolution_levels` | Number of pyramid levels |
| `downscaling` | Scale factor between levels (e.g., 2) |
| `tile_size_x`, `tile_size_y` | Tile dimensions |
| `n_threads` | Parallel threads for export |
| `compression` | Compression algorithm |

---

### Step 7: Clean Up

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Register > Delete registration pair`

Removes the registration pair from memory and closes associated windows.

---

## Complete Workflow Example

```
1. Open QuPath project images in BDV Playground
2. Create registration pair: HE slide (fixed) + IF slide (moving)
3. Open GUI to visualize
4. Center moving on fixed
5. Apply SIFT affine (pixel size: 4 microns)
6. Apply Elastix spline (control points: 8)
7. Verify alignment in GUI
8. Export to QuPath project
9. Delete registration pair
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| SIFT finds no matches | Adjust pixel size, try different channels, enable intensity inversion |
| Elastix diverges | Start with affine before spline, use coarser resolution |
| Registration is offset | Ensure both images have correct calibration (pixel size) |
| Export fails | Check disk space, reduce resolution levels if needed |
| BigWarp is slow | Use fewer landmarks initially, add more in critical areas |

## Related Resources

- [Registration Concepts](concepts.md)
- [Automated Registration](automated_registration.md)
- [Registration with BigWarp](../commands/bigwarp.md)
