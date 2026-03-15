# Deconvolution

GPU-accelerated Richardson-Lucy deconvolution, computed lazily in tiles. The deconvolved result is a virtual source — tiles are deconvolved on-the-fly as you navigate or export.

:::{important}
GPU deconvolution requires CLIJ2 and an OpenCL-compatible graphics card. See the [Installation Guide](../installation/installation.md#gpu-deconvolution-clij) for setup instructions.
:::

---

## Source - Deconvolve (Richardson Lucy GPU - Tiled)

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