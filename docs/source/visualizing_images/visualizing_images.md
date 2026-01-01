# Visualizing Images

This guide covers how to view, navigate, and display images in BigDataViewer Playground.

## Overview

BigDataViewer Playground provides two main visualization modes:

| Viewer                    | Description                        | Best For                                  |
|---------------------------|------------------------------------|-------------------------------------------|
| **BDV** (BigDataViewer)   | 2D slice viewer with 3D navigation | Large datasets, multi-channel, time-lapse |
| **BVV** (BigVolumeViewer) | 3D volume rendering                | Volumetric visualization, GPU-accelerated |

---

## Opening a Viewer

It is possible to create empty viewers.

### Create an empty BDV window

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Create empty BDV window
```

This command has no parameter. Note that it is possible to customize the default viewer that is used.

### Create a BDV Window with sources

Generally, you want to display sources which are already opened inside viewers. 

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Show Sources
```

This command will create a viewer if none exists. Otherwise, sources will be added to the current BDV viewer.

```
Menu: Plugins > BigDataViewer-Playground > BDV > BDV - Show Sources (new Bdv window)
```

This command will always create a new viewer to display sources.

### Create an empty BVV Window (3D Volume)

```
Menu: Plugins > BigDataViewer-Playground > BVV > BVV - Create Empty BVV Frame
```

Opens a GPU-accelerated 3D volume rendering view. A BVV window always has to be created empty before sources are added to it.

---

## Basic Navigation (BDV)

### Mouse Controls

| Action                  | Effect                |
|-------------------------|-----------------------|
| **Left-click + drag**   | Pan the view          |
| **Right-click + drag**  | Rotate the view (3D)  |
| **Scroll wheel**        | Zoom in/out           |
| **Middle-click + drag** | Translate in Z        |
| **Shift + scroll**      | Move through Z slices |

### Keyboard Shortcuts

| Key           | Action                         |
|---------------|--------------------------------|
| `S`           | Toggle source visibility       |
| `F`           | Toggle fused mode              |
| `G`           | Toggle grouping                |
| `I`           | Toggle interpolation           |
| `1-9`         | Select source/group            |
| `Shift + 1-9` | Toggle source/group visibility |
| `[` / `]`     | Previous/next timepoint        |

### View Alignment

Quickly align to standard orthogonal views:

| Shortcut    | View             |
|-------------|------------------|
| `Shift + Z` | Top (XY plane)   |
| `Shift + X` | Side (YZ plane)  |
| `Shift + Y` | Front (XZ plane) |

---

## Display Settings

### Adjusting Brightness and Contrast

Viewers have a convenient side panel to change these display settings.
To open the side panel, hover with the mouse on the middle at the right of the viewer. A blue arrow will appear. Click on it. From there, you can change these parameters for one or several of the sources (multi-line selection possible):

| Control          | Effect              |
|------------------|---------------------|
| **Min slider**   | Set black point     |
| **Max slider**   | Set white point     |
| **Color button** | Change source color |

### Setting Display Range

One can tune the color and min max of each sources with scijava commands.

1. Right-click on the source in the tree
2. Select `Set Display Range`
3. Enter min and max values

---

## Multi-Channel Visualization

### Fused vs Single Source Mode

| Mode       | Shortcut     | Description                  |
|------------|--------------|------------------------------|
| **Fused**  | `F`          | All visible sources overlaid |
| **Single** | `F` (toggle) | Only selected source shown   |

---

## Source Tree Panel

The source tree view of BigDataViewer-Playground (left panel) shows all loaded sources:

### Tree Operations

| Action           | Effect                    |
|------------------|---------------------------|
| **Click source** | Select it                 |
| **Double-click** | Center view on source     |
| **Right-click**  | Context menu with options |

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

This is similar to BDV navigation.

| Action                 | Effect                 |
|------------------------|------------------------|
| **Left-click + drag**  | Rotate volume          |
| **Right-click + drag** | Pan                    |
| **Scroll**             | Zoom                   |
| **Shift + drag**       | Adjust clipping planes |

---

## Time-Lapse Navigation

For time-series data:

| Shortcut | Action                     |
|----------|----------------------------|
| `[`      | Previous timepoint         |
| `]`      | Next timepoint             |
| Slider   | Jump to specific timepoint |

---

## View Synchronization

### Linking Multiple Windows

Synchronize navigation between BDV and BVV windows:

```
Menu: Plugins > BigDataViewer-Playground > Synchronize Views
```

Linked windows:
- Pan together
- Zoom together

Useful for comparing:
- Before/after processing
- Different channels
- Registered datasets
- 2D and 3D

---

## Screenshot and Export

See [View Export](../interactive_tools/view_export.md) for details.

---

## Tips

### Optimal Viewing

1. **Adjust per channel**: Each channel may need different display range
2. **Use appropriate LUTs**: Colorblind-friendly ideally
3. **Check multiple views**: XY, XZ, YZ reveal different features

### Performance

- For large datasets, BDV loads only visible regions
- Zoom out for overview, zoom in for detail
- Lower resolution levels display automatically when zoomed out

---

## Troubleshooting

| Problem               | Cause               | Solution                      |
|-----------------------|---------------------|-------------------------------|
| Black screen          | Display range wrong | Adjust min/max values         |
| Saturated (all white) | Max too low         | Increase max display value    |

---

## Related Topics

- [Opening Images](../opening_images/opening_images.md) - Load data into BDV
- [View Export](../interactive_tools/view_export.md) - Capture and export views
- [Processing Images](../processing_images/index.md) - Process visible data
