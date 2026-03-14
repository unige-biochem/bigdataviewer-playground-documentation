# Processing Images

This guide covers the commands for transforming, fusing, classifying, and deconvolving your datasets.

A key principle: most processing in BigDataViewer Playground is **lazy**. When you fuse, resample, classify, or deconvolve sources, the result is a new virtual source — pixels are only computed when you look at them or export them. This means you can set up complex processing pipelines on terabyte-scale data without waiting for the whole volume to be computed.

All processing commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Process`

---

## Fuse & Resample

Fusing and resampling let you combine multiple sources into one and/or change the voxel grid of your data. This is essential when you need to:

- Merge overlapping tiles into a single seamless image
- Change the resolution or voxel size of your data
- Produce a single output from multi-channel or multi-tile acquisitions

The general workflow is: **define a target grid** (the output voxel size and extent), then **resample or fuse** your sources onto that grid.

### Source - Define Resampling Grid

Creates an empty model source that spans the bounding box of multiple sources with a custom voxel size. Use this to define the output grid before fusing.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Define Resampling Grid`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources whose combined bounding box defines the model extent |
| Model Name | Name for the model source |
| Voxel Size X/Y/Z | Output voxel size in each dimension (in world coordinate units) |
| Resolution Levels | Number of pyramid resolution levels to create |
| X/Y/Z Downscale Factor | Downscaling factor between resolution levels in each dimension |
| Number of Timepoints | Number of timepoints in the model source |
| Model Timepoint | Reference timepoint used to compute the bounding box |

:::{tip}
Choose the voxel size based on your desired output resolution. For example, if your sources have 0.3 um pixels but you want a 1 um isotropic output, set all three voxel sizes to 1.0.
:::

### Source - Create Resampling Grid From Source

A simpler alternative: creates a model source that occupies the same volume as a single existing source but with a different voxel size. Useful when you want to resample one source to a different resolution without changing its spatial extent.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Create Resampling Grid From Source`

| Parameter | Description |
|-----------|-------------|
| Model Source | The source whose volume defines the extent of the new grid |
| Source name | Name for the new model source |
| Timepoint | Timepoint to use from the model source (0-based) |
| Voxel Size X/Y/Z | Voxel size in each dimension (in world coordinate units) |

### Source - Resample Source

Resamples one or more sources to match the voxel grid of a model source. The model source defines the output resolution and dimensions — the resampled source will have exactly the same grid.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Resample Source`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to resample |
| Model Source | The source whose voxel grid defines the output |
| Name(s) | Name(s) for the resampled source(s), comma-separated for multiple |
| Interpolate | Use interpolation when resampling (recommended for intensity data) |
| Re-use MipMaps | Reuse existing pyramid levels for efficiency |
| MipMap level if not re-used | Resolution level to use when not reusing MipMaps (0 = highest resolution) |
| Cache | Cache the resampled data in memory |

### Source - Fuse And Resample Sources

Fuses multiple sources into a single source, resampled to match a model source's grid. This is the main command for merging overlapping tiles or combining channels with blending.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Fuse And Resample Sources`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to fuse together |
| Model Source | The source whose grid defines the output resolution and dimensions |
| Output Name | Name for the fused source |
| Blending Mode | Method used to combine overlapping sources |
| Interpolate | Use interpolation when resampling |
| Re-use MipMaps | Use existing pyramid levels for efficiency |
| Default MipMap Level | Pyramid level to use if not reusing mipmaps (0 = highest resolution) |
| Cache | Cache computed blocks in memory |
| Cache Block X/Y/Z | Cache block size in each dimension |
| Cache Size Limit | Maximum number of blocks in cache (-1 = unlimited) |
| Number of Threads | Number of parallel threads for computation |

:::{tip}
For smooth transitions where tiles overlap, apply **L1 alpha blending masks** to your sources before fusing (see below). Without blending masks, hard edges will be visible at tile boundaries.
:::

### Source - Set Linear Blending Mask (L1 Alpha)

Sets a distance-based alpha blending mask on selected sources. The mask fades pixel intensity based on the distance from the source edge (L1 distance), so that overlapping regions blend smoothly when fused.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Set Linear Blending Mask (L1 Alpha)`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to apply L1 alpha blending to |

Apply this to all overlapping sources **before** calling **Source - Fuse And Resample Sources**.

---

## Pixel Classification (Labkit)

Labkit integration lets you train a pixel classifier interactively and then apply it lazily to your full dataset. This is the recommended way to segment large images — you train on a small region, then the classifier is applied on-the-fly as you navigate or export.

### Source - Open Labkit

Opens the Labkit pixel classification GUI for the selected sources. Each source is treated as a separate channel input to the classifier.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Classify (Labkit) > Source - Open Labkit`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to open in Labkit (each treated as a channel) |
| Resolution Level | Resolution level to use (0 = full resolution, higher = lower resolution) |

:::{tip}
For large datasets, start with a higher resolution level (e.g. 2 or 3) to train your classifier quickly. Once you're satisfied, apply it at full resolution using **Source - Apply Labkit Classifier**.
:::

### Source - Apply Labkit Classifier

Creates a lazy segmentation source by applying a previously saved Labkit classifier. The classification is computed on-the-fly — only the pixels you view or export are actually classified.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Classify (Labkit) > Source - Apply Labkit Classifier`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to classify (each treated as a channel) |
| Classifier File | Path to the Labkit `.classifier` file |
| Resolution Level | Resolution level to use from input sources (0 = full resolution) |
| Output Name Suffix | Suffix appended to the source name for the classified output |
| Use GPU | Use GPU acceleration for classification (requires compatible GPU and OpenCL) |

---

## Deconvolution

GPU-accelerated Richardson-Lucy deconvolution, computed lazily in tiles. The deconvolved result is a virtual source — tiles are deconvolved on-the-fly as you navigate or export.

:::{important}
GPU deconvolution requires CLIJ2 and an OpenCL-compatible graphics card. See the [Installation Guide](../installation/installation.md#gpu-deconvolution-clij) for setup instructions.
:::

### Source - Deconvolve (Richardson Lucy GPU - Tiled)

{menuselection}`Plugins > BigDataViewer-Playground > Process > Deconvolve > Source - Deconvolve (Richardson Lucy GPU - Tiled)`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to deconvolve |
| PSF Source | Point spread function source (applied to all sources) |
| Iterations | Number of Richardson-Lucy iterations |
| Block Size X/Y/Z | Tile size in each dimension for GPU processing (pixels) |
| Overlap Size | Overlap between adjacent tiles to avoid edge artifacts (pixels) |
| Non-Circulant | Use non-circulant boundary conditions (reduces edge artifacts) |
| Regularization Factor | Regularization strength to prevent noise amplification (0 = none) |
| Output Pixel Type | Pixel type for the deconvolved output |
| Name Suffix | Suffix appended to source names for the deconvolved outputs |
| Number of Threads | Number of parallel threads for tile processing |

:::{tip}
The PSF must be loaded as a source in BigDataViewer Playground before running deconvolution. You can import a PSF image using any of the import commands (e.g. **Dataset - Create [Bio-Formats]** or **Dataset - Create [Current ImagePlus]**).
:::

---

## Multi-Resolution

These commands manage the pyramid (multi-resolution) levels of your sources. Pyramid levels are crucial for interactive navigation — they let the viewer load lower-resolution tiles when zoomed out, keeping browsing responsive even on very large datasets.

### Source - Pyramidize

Generates multi-resolution pyramid levels for sources that don't already have them (e.g. sources derived from processing operations).

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Pyramidize`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to add pyramid levels to |

### Source - Crop Resolution Levels

Creates a new source with only a subset of the original resolution levels. Useful when you want to restrict which pyramid levels are available — for example, to skip the lowest-resolution levels or to start from a specific level.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Crop Resolution Levels`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to crop resolution levels from |
| Min Level | Minimum resolution level to keep (0 = highest resolution) |
| Max Level | Maximum resolution level to keep (inclusive) |
| Name Suffix | Suffix to append to the source name |

---

## Timepoint Operations

Commands for manipulating the time dimension of your sources.

### Source - Freeze Timepoint

Creates a new source that shows a single fixed timepoint across a range of timepoints. Useful for creating a static reference from a time-series — for example, freezing a pre-treatment timepoint so it can be compared side-by-side with later timepoints.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Freeze Timepoint`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to freeze |
| Timepoint to copy | The timepoint to replicate |
| Timepoint start | Start of the output time range |
| Timepoint end (excluded) | End of the output time range (exclusive) |
| Output Name | Suffix for the resulting source |

### Source - Shift Timepoints

Creates a new source with timepoints offset by a fixed amount. Useful for aligning time-series data that was acquired with different starting times.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Shift Timepoints`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to time-shift |
| Time Shift | Number of timepoints to shift (positive = forward, negative = backward) |
| Output Name | Suffix for the resulting source |

---

## Transforms

Commands for spatially transforming sources. These add affine transforms to the source's transform chain — no pixels are rewritten.

Remember: each source in a dataset carries a **chain of affine transforms** that maps pixel coordinates to world coordinates. The transform commands here modify that chain, which means they are instant and non-destructive.

### Source - Basic Transformation

Performs 90/180/270-degree rotations or mirror flips along X, Y, or Z axes.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform > Source - Basic Transformation`

| Parameter | Description |
|-----------|-------------|
| Select source(s) | The source(s) to transform |
| Transformation type | Flip (mirror) or Rot (rotate by 90/180/270 degrees) |
| Axis | Axis along which to perform the transformation |
| Global transform | If checked, transforms relative to world origin (0,0,0). Otherwise, keeps each source center unchanged |
| Initial timepoint | First timepoint to apply the transformation (0-based) |
| Number of timepoints | Number of timepoints to apply the transformation to |

### Source - Interactive Transformation

Lets you manually drag sources in a BDV window to position them. The sources you select are the ones that move — all other sources in the window stay fixed as reference.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform > Source - Interactive Transformation`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to manually transform |
| Select BDV Window | The BigDataViewer window used for manual positioning |
| Mode | How to apply the transformation: **Mutate** modifies the existing transform, **Append** adds a new transform layer |

:::{note}
During interactive transformation, you are placed in the coordinate frame of the moving sources — so the moving sources appear stationary while the reference sources move. This is normal. When you confirm the transform, the result is applied to the moving sources.
:::

### New Affine Transform

Creates an affine transform from a 4x3 matrix (12 comma-separated values in row-major order). Use this when you need to apply a known numeric transform to sources via the Dataset transform stack commands.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform > New Affine Transform`

| Parameter | Description |
|-----------|-------------|
| Transform Matrix | 12 comma-separated values defining a 4x3 affine matrix in row-major order |

### Source - Recenter Sources

Moves sources so their center is at the specified world coordinates. Useful for aligning sources to a common reference point.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform > Source - Recenter Sources`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to recenter |
| Center X/Y/Z | Target world coordinates for the source center |
| Timepoint | Timepoint used for computing the recentering transform |
| Mode | **Mutate** modifies the existing transform; **Append** adds a new transform layer |

### Source - Remove Z Offset

Removes the Z position offset from sources, shifting them to Z=0. Useful when imported data has a large Z offset that makes navigation awkward.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform > Source - Remove Z Offset`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to remove Z offset from |
| Timepoint | Timepoint used to compute the Z offset |
| Apply to all timepoints | If checked, removes Z offset for each timepoint independently |
| Mode | **Mutate** modifies the existing transform; **Append** adds a new transform layer |

:::{note}
**About "Make Transformable"**: Sources created from a dataset already carry a mutable affine transform chain and can be transformed directly. The command **Source - Make Transformable** (`Process > Source - Make Transformable`) is only needed for sources that were not created from a dataset (e.g. procedurally generated sources). It wraps the source in a TransformedSource so that interactive and programmatic transforms can be applied.
:::

---

## Source Management

Utility commands for managing sources in the workspace.

| Command | Menu path | Description |
|---------|-----------|-------------|
| Source - Delete | `Process > Source - Delete` | Removes selected sources from the workspace |
| Source - Duplicate | `Process > Source - Duplicate` | Creates a copy of the selected sources |
| Source - Add Metadata | `Process > Source - Add Metadata` | Attaches a key-value metadata string to selected sources (useful for filtering in the tree view) |