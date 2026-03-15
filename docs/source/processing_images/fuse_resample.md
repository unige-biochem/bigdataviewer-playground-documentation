# Fuse & Resample

Fusing and resampling let you combine multiple sources into one and/or change the voxel grid of your data. This is essential when you need to:

- Merge overlapping tiles into a single seamless image
- Change the resolution or voxel size of your data
- Produce a single output from multi-channel or multi-tile acquisitions

The general workflow is: **define a target grid** (the output voxel size and extent), then **resample or fuse** your sources onto that grid.

All commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample`

---

## Source - Define Resampling Grid

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

---

## Source - Create Resampling Grid From Source

A simpler alternative: creates a model source that occupies the same volume as a single existing source but with a different voxel size. Useful when you want to resample one source to a different resolution without changing its spatial extent.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Create Resampling Grid From Source`

| Parameter | Description |
|-----------|-------------|
| Model Source | The source whose volume defines the extent of the new grid |
| Source name | Name for the new model source |
| Timepoint | Timepoint to use from the model source (0-based) |
| Voxel Size X/Y/Z | Voxel size in each dimension (in world coordinate units) |

---

## Source - Resample Source

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

---

## Source - Fuse And Resample Sources

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

---

## Source - Set Linear Blending Mask (L1 Alpha)

Sets a distance-based alpha blending mask on selected sources. The mask fades pixel intensity based on the distance from the source edge (L1 distance), so that overlapping regions blend smoothly when fused.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Fuse & Resample > Source - Set Linear Blending Mask (L1 Alpha)`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to apply L1 alpha blending to |

Apply this to all overlapping sources **before** calling **Source - Fuse And Resample Sources**.