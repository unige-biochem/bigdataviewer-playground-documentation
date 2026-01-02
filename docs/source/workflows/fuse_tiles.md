# Fuse Multi-Tile Acquisition

This workflow guides you through combining tiled microscopy acquisitions into a seamless fused volume.

## Goal

Combine multiple overlapping tiles into a single continuous dataset:
- Align tiles with sub-pixel precision
- Blend overlapping regions smoothly
- Export as a unified volume

## Prerequisites

- [ ] BigDataViewer Playground installed ([Installation Guide](../installation/installation.md))
- [ ] Multi-tile acquisition data (CZI, LIF, or similar)
- [ ] Sufficient disk space for output (fused data can be large)

## Overview

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│ Load Tiles  │ ──▶ │ Verify/Fix   │ ──▶ │ Calculate   │ ──▶ │ Fuse +       │
│             │     │ Positions    │     │ Stitching   │     │ Export       │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

---

## Step 1: Load Tiled Data

### Open Multi-Tile Dataset

For CZI files:
```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Open CZI Dataset
```

For other formats:
```
Menu: Plugins > BigDataViewer-Playground > BDVDataset > Open with QuPath Bio-Formats Builder
```

### Verify Tile Layout

1. Display all tiles in BDV
2. Check that tiles appear in approximately correct positions
3. Note any obvious misalignments

:::{note}
Stage positions from metadata provide initial placement. Fine alignment comes in later steps.
:::

---

## Step 2: Check Initial Positions

### Visualize Tile Arrangement

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Show Sources
```

Select all tiles to see their spatial arrangement.

### Identify Issues

| Issue | Appearance | Action |
|-------|------------|--------|
| Tiles overlap correctly | Structures align in overlap | Proceed to fusion |
| Small misalignment | Slight offset at boundaries | Run stitching refinement |
| Major misalignment | Tiles far from correct position | Check metadata, manual fix |
| Missing tiles | Gaps in coverage | Verify all tiles loaded |

---

## Step 3: Refine Tile Positions (if needed)

### Automatic Stitching Refinement

If tiles have small misalignments:

```
Menu: Plugins > BigDataViewer-Playground > Sources > Register > Calculate Pairwise Shifts
```

This computes optimal translations between adjacent tiles.

### Manual Position Adjustment

For problematic tiles:

```
Menu: Plugins > BigDataViewer-Playground > Sources > Transform > Manual Transform
```

Adjust position while viewing overlap regions.

---

## Step 4: Configure Fusion

### Blending Options

| Method | Description | Best For |
|--------|-------------|----------|
| Linear blending | Gradual transition in overlap | Most cases |
| Average | Mean of overlapping pixels | Uniform intensity |
| Max intensity | Maximum value wins | Sparse features |

### Resolution Settings

| Option | Result |
|--------|--------|
| Full resolution | Highest quality, largest file |
| Downsampled | Faster, smaller file |
| Multi-resolution | Pyramid for fast viewing |

---

## Step 5: Fuse and Export

### Export Fused Volume

```
Menu: Plugins > BigDataViewer-Playground > Sources > Export > Fuse and Export
```

| Parameter | Recommendation |
|-----------|----------------|
| Output format | XML/HDF5 for BDV, OME-TIFF for compatibility |
| Blending | Linear for smooth transitions |
| Compression | LZW or ZLIB |

### For Very Large Datasets

Export in blocks to manage memory:

```
Menu: Plugins > BigDataViewer-Playground > Sources > Export > Export to N5
```

N5 format supports chunked, parallel writing.

---

## Step 6: Verify Result

### Check Fusion Quality

1. Open fused dataset
2. Navigate to tile boundaries
3. Look for:
   - Smooth intensity transitions
   - No visible seams
   - Structures continuous across boundaries

### Compare Tile vs Fused

Use view synchronization to compare:
- Original tiles: boundaries visible
- Fused result: seamless volume

---

## Expected Output

After completing this workflow:

- ✅ Single continuous volume from multiple tiles
- ✅ Smooth blending at tile boundaries
- ✅ Preserved resolution and dynamic range
- ✅ Exported in chosen format

---

## Special Cases

### Time-Lapse Tiled Data

For tiled acquisitions with time dimension:
- Stitching parameters apply to all timepoints
- Export includes all timepoints
- Consider per-timepoint drift correction if needed

### Multi-Channel Tiled Data

For multi-channel acquisitions:
- All channels use same tile positions
- Each channel fused separately
- Export as multi-channel dataset

### 3D Tiled Data (Z-stacks)

For volumetric tiles:
- Tiles may overlap in Z as well as XY
- 3D stitching considers all three dimensions
- Export as full 3D volume

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Visible seams | Poor blending or misalignment | Refine positions, adjust blending |
| Intensity jumps | Uneven illumination | Apply flat-field correction first |
| Out of memory | Volume too large | Export in blocks, use N5 format |
| Missing regions | Tiles not included | Verify all tiles selected for fusion |
| Slow export | Large dataset | Use compression, export overnight |

---

## Performance Tips

### Memory Management

- Process subset of tiles if testing
- Use lazy loading (don't load all tiles to RAM)
- Export to chunked format (N5, HDF5)

### Disk Space

Estimate output size:
```
Size = X × Y × Z × bytes_per_pixel × num_channels × num_timepoints
```

Compression typically achieves 2-5x reduction.

---

## Related Topics

- [BigStitcher Integration](../special_datasets/bigstitcher.md)
- [Export Formats](../processing_images/export_formats.md)
- [Fusion Methods](../processing_images/fusion.md)
