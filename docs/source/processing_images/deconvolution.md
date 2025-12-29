# Deconvolution

BigDataViewer Playground provides GPU-accelerated deconvolution using the Richardson-Lucy algorithm. This feature is powered by CLIJ2-FFT and operates on sources in a lazy, tiled manner.

## Overview

Deconvolution improves image resolution and contrast by reversing the blurring caused by the optical system. It requires:
- The image to deconvolve
- A Point Spread Function (PSF) describing the optical blur
- Sufficient GPU resources

### Key Features

- **GPU-accelerated**: Uses OpenCL for fast computation
- **Tiled processing**: Handles large images that don't fit in GPU memory
- **Lazy evaluation**: Deconvolution computed on-demand
- **Multi-GPU support**: Can utilize multiple GPUs

---

## Requirements

### Hardware

- **GPU**: OpenCL-compatible GPU (NVIDIA, AMD, or Intel)
- **VRAM**: Sufficient for tile size (2-4 GB recommended minimum)
- **RAM**: For caching and data transfer

### Software

- **CLIJ2**: Must be installed via Fiji update site
- **CLIJ2-FFT**: FFT operations for deconvolution

:::{note}
Deconvolution performance depends heavily on GPU capabilities. A dedicated graphics card with ample VRAM will significantly outperform integrated graphics.
:::

---

## Command: Deconvolve Sources

**Class**: `ch.epfl.biop.scijava.command.source.deconvolve.SourcesDeconvolverCommand`

### Parameters

| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to deconvolve |
| `psf` | Point Spread Function source |
| `algorithm` | Deconvolution algorithm |
| `n_iterations` | Number of Richardson-Lucy iterations |

### Output

| Output | Description |
|--------|-------------|
| `deconvolved_sources` | The deconvolved source(s) |

---

## Preparing the PSF

The Point Spread Function (PSF) is critical for quality deconvolution.

### PSF Options

1. **Measured PSF**: Acquired from sub-resolution beads
2. **Theoretical PSF**: Generated based on optical parameters
3. **Extracted PSF**: Isolated from a bright point in the image

### PSF Requirements

- Should match the imaging conditions (wavelength, NA, medium)
- Must be properly centered
- Size should be appropriate (typically 3-5x FWHM in each dimension)

:::{tip}
A well-characterized PSF is more important than many iterations. Start with a measured or carefully calculated theoretical PSF.
:::

---

## Deconvolution Workflow

### Step 1: Load Image and PSF

```
1. Open your image in BDV Playground
2. Open or generate your PSF as a source
3. Both should be visible in the source tree
```

### Step 2: Configure Deconvolution

```
1. Select source(s) to deconvolve
2. Run deconvolution command
3. Select PSF source
4. Set number of iterations (start with 10-20)
```

### Step 3: Run and Evaluate

```
1. Execute deconvolution
2. Visualize deconvolved result alongside original
3. Adjust iterations if needed
4. Export when satisfied
```

---

## Parameters Guide

### Number of Iterations

| Iterations | Effect |
|------------|--------|
| 5-10 | Mild improvement, fast |
| 15-30 | Good balance of quality and speed |
| 50+ | Maximum resolution, risk of artifacts |

:::{warning}
Too many iterations can amplify noise and create ringing artifacts. Start with fewer iterations and increase only if needed.
:::

### Tile Size

The deconvolver processes images in tiles:
- Larger tiles: Better quality at boundaries, more VRAM needed
- Smaller tiles: Less VRAM, may show tile boundary artifacts

Tiles overlap to minimize boundary effects.

---

## Tiled Processing Details

The deconvolution implementation uses a sophisticated tiling approach:

1. **Tile division**: Image split into overlapping blocks
2. **GPU processing**: Each tile deconvolved on GPU
3. **Overlap blending**: Tiles merged with smooth transitions
4. **Caching**: Results cached via ImgLib2's CachedCellImg

This allows deconvolution of arbitrarily large images regardless of GPU memory.

---

## Performance Optimization

### GPU Selection

If multiple GPUs are available:
- CLIJ2 provides GPU selection options
- Dedicated GPU typically faster than integrated

### Memory Management

| Symptom | Solution |
|---------|----------|
| Out of GPU memory | Reduce tile size |
| Slow processing | Increase tile size (if VRAM allows) |
| System slowdown | Limit parallel operations |

### Processing Speed

Factors affecting speed:
1. GPU compute power
2. Tile size and overlap
3. Number of iterations
4. Image data type (8-bit faster than 16/32-bit)

---

## Quality Considerations

### When Deconvolution Helps

- Slight focus blur
- Known, stable PSF
- Sufficient signal-to-noise ratio

### When to Avoid Deconvolution

- Severe motion blur
- Very noisy images
- Unknown or varying PSF
- Saturated regions

### Avoiding Artifacts

| Artifact | Cause | Prevention |
|----------|-------|------------|
| Ringing | Too many iterations | Reduce iterations |
| Noise amplification | Low SNR | Pre-filter or fewer iterations |
| Edge effects | Tile boundaries | Increase overlap |
| Checkerboard pattern | GPU precision issues | Check CLIJ2 settings |

---

## Example Workflows

### Basic Deconvolution

```
1. Open 3D fluorescence stack
2. Load or generate PSF for objective/wavelength
3. Run deconvolution with 20 iterations
4. Compare with original
5. Export deconvolved result
```

### Multi-Channel Deconvolution

```
1. Open multi-channel image
2. Prepare PSF for each wavelength (different PSF per channel)
3. Deconvolve each channel with corresponding PSF
4. Combine deconvolved channels for visualization
```

### Lattice Light Sheet Deconvolution

```
1. Open LLS7 dataset (automatically deskewed)
2. Use LLS-specific PSF
3. Deconvolve to recover resolution
4. Export for analysis
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| No GPU found | CLIJ2 not configured | Install CLIJ2, check GPU drivers |
| Out of memory | Tile too large | Reduce tile size |
| No improvement | Wrong PSF | Verify PSF matches imaging conditions |
| Artifacts appear | Too many iterations | Reduce iterations |
| Very slow | Integrated GPU | Use dedicated GPU if available |
| Crashes | GPU driver issue | Update GPU drivers |

### Verifying GPU Setup

In Fiji:
1. Open `Plugins > CLIJ2 > CLIJ2 Macro Extensions`
2. Check that your GPU is detected
3. Run a simple CLIJ2 operation to verify functionality

---

## Related Topics

- [Export Formats](export_formats.md) - Save deconvolved results
- [Resampling](resampling.md) - Prepare data for deconvolution
- [Special Datasets: LLS7](../special_datasets/index.md) - Lattice light sheet processing
