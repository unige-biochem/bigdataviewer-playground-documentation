# Interactive Tools

This section covers interactive selection and manipulation tools in BigDataViewer Playground.

## Overview

BigDataViewer Playground provides interactive tools for:
- Selecting points and regions directly in the viewer
- Defining spatial parameters for processing commands
- Exporting views to standard image formats
- Creating visualizations and overlays

| Tool | Purpose | Key Feature |
|------|---------|-------------|
| [Point Selection](point_selection.md) | Mark locations in 3D | Landmark placement |
| [Region Selection](region_selection.md) | Define 2D/3D bounds | Rectangles and boxes |
| [View Export](view_export.md) | Capture BDV views | Screenshot to ImagePlus |

## Documentation

```{toctree}
:maxdepth: 2

point_selection
region_selection
view_export
```

## Quick Reference

### Selection Commands

| Command | Class | Output |
|---------|-------|--------|
| Get User Points | `GetUserPointsCommand` | List of RealPoint |
| Get User Rectangle | `GetUserRectangleCommand` | Position + size (2D) |
| Get User 3D Box | `GetUserBox3DCommand` | Position + size (3D) |

### Export Commands

| Command | Class | Description |
|---------|-------|-------------|
| Take Screenshot | `BdvViewToImagePlusExportCommand` | Full-featured view capture |
| Basic Export | `BasicBdvViewToImagePlusExportCommand` | Simple view export |

### Visualization Commands

| Command | Description |
|---------|-------------|
| `OverviewerCommand` | Create overview visualization |
| `ShowGridBdvCommand` | Display sources in grid layout |

## Common Workflows

### Interactive Selection → Processing

```
1. Start command that requires spatial input
2. Use selection tool (points, rectangle, or box)
3. Command receives coordinates
4. Processing proceeds with defined region
```

### Landmark-Based Registration

```
1. Open fixed and moving images in BDV
2. Select corresponding points on both
3. Registration computes transform from point pairs
4. Transform aligns moving to fixed
```

### Region-Based Export

```
1. Navigate to region of interest
2. Select region (rectangle for 2D, box for 3D)
3. Export with defined boundaries
4. Result cropped to selection
```

## Tips

### Effective Selection

1. **Zoom appropriately**: Higher zoom = more precision
2. **Use standard views**: XY, XZ, YZ for axis-aligned selections
3. **Check all dimensions**: Verify X, Y, and Z are correct
4. **Take your time**: Accurate selection saves reprocessing

### Working with Large Data

- Selection works at any zoom level
- Coordinates are in world units (physical space)
- Actual processing uses appropriate resolution level

## See Also

- [Navigation & Overlays](../commands/navigation_overlays.md) - BDV navigation controls
- [Visualizing Images](../visualizing_images/visualizing_images.md) - Display settings
- [Registration](../registration/index.md) - Uses point selection for landmarks
