# Visualizing Images

This guide covers how to view, navigate, and display images in BigDataViewer Playground.

## Overview

BigDataViewer Playground provides two main visualization modes:

| Viewer | Description | Best For |
|--------|-------------|----------|
| **BDV** (BigDataViewer) | 2D slice viewer with 3D navigation | Large datasets, multi-channel, time-lapse |
| **BVV** (BigVolumeViewer) | 3D volume rendering | Volumetric visualization, GPU-accelerated |

---

## Opening a Viewer

### Create a BDV Window

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Show Sources
```

Select sources to display and a new BDV window opens.

### Create a BVV Window (3D Volume)

```
Menu: Plugins > BigDataViewer-Playground > BVV > BVV - Show Sources
```

Opens a GPU-accelerated 3D volume rendering view.

---

## Basic Navigation (BDV)

### Mouse Controls

| Action | Effect |
|--------|--------|
| **Left-click + drag** | Pan the view |
| **Right-click + drag** | Rotate the view (3D) |
| **Scroll wheel** | Zoom in/out |
| **Middle-click + drag** | Translate in Z |
| **Shift + scroll** | Move through Z slices |

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `S` | Toggle source visibility |
| `F` | Toggle fused mode |
| `G` | Toggle grouping |
| `I` | Toggle interpolation |
| `1-9` | Select source/group |
| `Shift + 1-9` | Toggle source/group visibility |
| `[` / `]` | Previous/next timepoint |
| `Shift + Z` | Align view to XY plane |
| `Shift + X` | Align view to YZ plane |
| `Shift + C` or `Shift + Y` | Align view to XZ plane |

### View Alignment

Quickly align to standard orthogonal views:

| Shortcut | View |
|----------|------|
| `Shift + Z` | Top (XY plane) |
| `Shift + X` | Side (YZ plane) |
| `Shift + C` | Front (XZ plane) |

---

## Display Settings

### Adjusting Brightness and Contrast

1. Press `S` to open the brightness/contrast dialog
2. Or: `Settings > Brightness & Color` in the BDV menu

| Control | Effect |
|---------|--------|
| **Min slider** | Set black point |
| **Max slider** | Set white point |
| **Color button** | Change LUT/color |

### Setting Display Range

For quantitative display:
1. Right-click on the source in the tree
2. Select `Set Display Range`
3. Enter min and max values

### Color Lookup Tables (LUTs)

Change how intensity values are mapped to colors:

| LUT | Use Case |
|-----|----------|
| **Grays** | Single channel, quantitative |
| **Green** | GFP, FITC channels |
| **Magenta** | RFP, Cy5 channels |
| **Cyan** | CFP, DAPI channels |
| **Fire/Jet** | Heatmap visualization |

---

## Multi-Channel Visualization

### Fused vs Single Source Mode

| Mode | Shortcut | Description |
|------|----------|-------------|
| **Fused** | `F` | All visible sources overlaid |
| **Single** | `F` (toggle) | Only selected source shown |

### Channel Visibility

- Press `1-9` to select a source
- Press `Shift + 1-9` to toggle visibility
- Or use the source tree panel

### Recommended Multi-Channel Setup

```
1. Open all channels in BDV
2. Assign distinct colors to each channel
3. Adjust display range per channel
4. Toggle fused mode (F) to see overlay
```

### Grouping Sources

Group sources for synchronized operations:
- Press `G` to toggle grouping mode
- Grouped sources move together
- Useful for multi-channel datasets

---

## Source Tree Panel

The source tree (left panel) shows all loaded sources:

### Tree Operations

| Action | Effect |
|--------|--------|
| **Click source** | Select it |
| **Double-click** | Center view on source |
| **Right-click** | Context menu with options |
| **Drag** | Reorder sources |

### Context Menu Options

Right-clicking a source provides:
- Display settings
- Transform operations
- Export options
- Remove source

---

## 3D Visualization (BVV)

### Volume Rendering

BVV provides true 3D volume rendering:

```
Menu: Plugins > BigDataViewer-Playground > BVV > BVV - Show Sources
```

### BVV Navigation

| Action | Effect |
|--------|--------|
| **Left-click + drag** | Rotate volume |
| **Right-click + drag** | Pan |
| **Scroll** | Zoom |
| **Shift + drag** | Adjust clipping planes |

### Rendering Settings

Adjust volume rendering parameters:
- **Opacity**: How transparent the volume appears
- **Brightness**: Overall intensity
- **Clipping**: Show/hide parts of the volume

### GPU Requirements

BVV requires:
- OpenGL 3.3+ capable graphics card
- Updated graphics drivers
- Sufficient GPU memory for dataset size

---

## Interpolation

Toggle interpolation for smoother display:

| Mode | Shortcut | Description |
|------|----------|-------------|
| **Nearest neighbor** | `I` | Exact pixel values, blocky when zoomed |
| **Linear** | `I` | Smooth interpolation between pixels |

Use nearest neighbor for:
- Segmentation labels
- Quantitative analysis
- Seeing actual pixel values

Use linear for:
- Smooth visualization
- Publication figures
- General viewing

---

## Time-Lapse Navigation

For time-series data:

| Shortcut | Action |
|----------|--------|
| `[` | Previous timepoint |
| `]` | Next timepoint |
| Slider | Jump to specific timepoint |

### Playback

Use the timepoint slider or arrow keys to animate through time.

---

## View Synchronization

### Linking Multiple Windows

Synchronize navigation between BDV windows:

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Synchronize Windows
```

Linked windows:
- Pan together
- Zoom together
- Rotate together (optional)

Useful for comparing:
- Before/after processing
- Different channels
- Registered datasets

---

## Overlays and Annotations

### Grid Overlay

Display a reference grid:
```
Menu: Plugins > BigDataViewer-Playground > BDV > Add Grid Overlay
```

### Scale Bar

Add a scale bar showing physical dimensions.

### Source Boundaries

Visualize the extent of each source in the viewer.

---

## Screenshot and Export

### Capture Current View

```
Menu: Plugins > BigDataViewer-Playground > BDV > Take Screenshot
```

| Parameter | Description |
|-----------|-------------|
| Width/Height | Output image dimensions |
| Timepoint | Which timepoint to capture |

Result: ImagePlus with current view.

### Export to ImagePlus

Convert BDV sources to standard Fiji images:
```
Menu: Plugins > BigDataViewer-Playground > Sources > Export to ImagePlus
```

See [View Export](../interactive_tools/view_export.md) for details.

---

## Display Presets

### Save Display Settings

Store current display configuration:
- Colors and LUTs
- Display ranges
- Visibility states

### Apply to Other Datasets

Reuse settings for consistent visualization across experiments.

---

## Tips

### Optimal Viewing

1. **Adjust per channel**: Each channel may need different display range
2. **Use appropriate LUTs**: Colorblind-friendly options available
3. **Check multiple views**: XY, XZ, YZ reveal different features

### Performance

- For large datasets, BDV loads only visible regions
- Zoom out for overview, zoom in for detail
- Lower resolution levels display automatically when zoomed out

### Presentation Quality

1. Set up optimal display settings
2. Align to standard view (Shift+Z/X/C)
3. Use linear interpolation for smooth appearance
4. Export at appropriate resolution

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Black screen | Display range wrong | Adjust min/max values |
| Saturated (all white) | Max too low | Increase max display value |
| Laggy navigation | Dataset very large | Normal - data loads on demand |
| BVV won't open | GPU/OpenGL issue | Update graphics drivers |
| Colors look wrong | LUT mismatch | Check/change color settings |

---

## Related Topics

- [Opening Images](../opening_images/opening_images.md) - Load data into BDV
- [View Export](../interactive_tools/view_export.md) - Capture and export views
- [Processing Images](../processing_images/index.md) - Process visible data
