# View Export

BigDataViewer Playground provides tools to export the current view as static images or ImagePlus objects for further processing in Fiji.

## Overview

View export allows you to:
- Capture the current BDV view as an image
- Export visible sources to ImagePlus
- Create screenshots at specific resolutions
- Bridge BDV visualization with Fiji processing

## Screenshot Export

### Command: Take Screenshot

**Menu**: `Plugins > BigDataViewer-Playground > BDV > Take Screenshot`
**Class**: `bdv.util.BdvViewToImagePlusExportCommand`

Captures the current BDV view as an ImagePlus.

| Parameter | Description |
|-----------|-------------|
| `bdv_h` | The BDV window to capture |
| `capture_width` | Width of the output image in pixels |
| `capture_height` | Height of the output image in pixels |
| `selected_timepoint` | Timepoint to capture |

| Output | Description |
|--------|-------------|
| `image` | The captured ImagePlus |

### How It Works

The screenshot captures exactly what you see in the BDV viewer:
- Current zoom level and position
- Visible sources and channels
- Applied display settings (contrast, color)
- Any overlays or annotations

---

## Source to ImagePlus Export

### Command: Export Sources to ImagePlus

Converts BDV sources directly to ImagePlus format.

| Parameter | Description |
|-----------|-------------|
| `sources` | Sources to export |
| `resolution_level` | Which pyramid level to use |
| `timepoint` | Timepoint to export |

### Resolution Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| 0 | Full resolution | Quantitative analysis |
| 1+ | Downsampled | Preview, navigation |

:::{note}
Higher resolution levels (lower numbers) provide more detail but require more memory. Choose based on your analysis needs.
:::

---

## Capture Modes

### Single View Capture

Captures the exact current view:
```
1. Navigate to desired view in BDV
2. Adjust display settings
3. Run screenshot command
4. Specify output dimensions
5. Get ImagePlus result
```

### Multi-Channel Capture

When multiple channels are visible:
- All visible channels are included
- Color mapping is preserved
- Result is RGB or composite ImagePlus

### Timepoint Series

For time-lapse data:
```
1. Set up desired view
2. Export each timepoint
3. Or export as stack with all timepoints
```

---

## Use Cases

### Documentation and Publication

**Creating figure panels:**
```
1. Set up optimal view
2. Adjust contrast and colors
3. Capture at publication resolution
4. Save or further process in Fiji
```

### Analysis Handoff

**Bridge to Fiji analysis:**
```
1. View registered/transformed data in BDV
2. Export to ImagePlus
3. Use Fiji analysis tools
4. Quantify results
```

### Quality Control

**Verify processing results:**
```
1. View processed data in BDV
2. Export representative views
3. Compare before/after
4. Document workflow
```

---

## Resolution and Quality

### Choosing Output Size

| Goal | Recommended Size |
|------|------------------|
| Screen preview | 512-1024 px |
| Presentation | 1920x1080 px |
| Publication | 300 dpi at final size |
| Print poster | 150+ dpi at final size |

### Interpolation

The export respects BDV interpolation settings:
- **Nearest neighbor**: Preserves exact values
- **Linear**: Smoother appearance
- **Cubic**: Smoothest, may overshoot

### Anti-aliasing

For publication quality:
- Use higher capture resolution
- Downsample in post-processing
- Provides smoother edges

---

## Multi-Source Export

### Visible Sources Only

By default, only visible sources are captured:
- Toggle visibility before capture
- Adjust per-source display settings
- Set appropriate group visibility

### Merging Channels

Multiple sources can be merged:
- Each source becomes a channel
- LUT (color) settings are preserved
- Result is composite or RGB

---

## Tips

### Best Practices

1. **Set up view first**: Navigate, zoom, adjust before capture
2. **Check display settings**: Contrast, colors, gamma
3. **Consider resolution**: Match output to intended use
4. **Verify result**: Check exported ImagePlus

### Memory Considerations

For large exports:
- Use appropriate resolution level
- Consider tiled export for very large regions
- Close unnecessary sources

### Batch Export

For multiple views:
```groovy
// Example: Export multiple timepoints
for (t in 0..numTimepoints-1) {
    // Navigate to timepoint
    // Capture screenshot
    // Save with appropriate name
}
```

---

## Comparison with Direct Export

### View Export vs Source Export

| Aspect | View Export | Source Export |
|--------|-------------|---------------|
| What's captured | Rendered view | Raw source data |
| Resolution | View-dependent | Source resolution |
| Transforms | Applied visually | Can be applied or not |
| Color/contrast | Included | Raw values |

### When to Use Each

**Use View Export when:**
- You want exactly what you see
- Display settings are important
- Creating figures or documentation

**Use Source Export when:**
- You need raw data values
- Quantitative analysis required
- Processing pipeline continues

---

## Integration with Fiji

### Post-Processing

Exported ImagePlus can be processed with:
- Image > Adjust > Brightness/Contrast
- Process > Filters
- Analyze > Measure
- Any Fiji plugin

### Saving Results

After export:
- File > Save As > Tiff
- File > Save As > PNG (for figures)
- File > Save As > AVI (for movies)

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Black/empty image | Sources not visible | Check source visibility |
| Wrong colors | Display settings | Adjust LUT before capture |
| Low resolution | Small capture size | Increase capture dimensions |
| Out of memory | Very large export | Use lower resolution or smaller region |
| Missing channels | Sources not visible | Toggle all desired sources on |

---

## Related Topics

- [Export Formats](../processing_images/export_formats.md) - File format options
- [Visualizing Images](../visualizing_images/visualizing_images.md) - Display settings
- [Region Selection](region_selection.md) - Selecting regions to export
