# Region Selection

BigDataViewer Playground provides interactive tools for selecting rectangular regions and 3D boxes within the viewer.

## Overview

Region selection allows you to:
- Define areas for cropping or export
- Specify regions of interest (ROIs)
- Set boundaries for processing operations
- Create 3D bounding boxes

## Rectangle Selection

### Command: Get User Rectangle

**Class**: `ch.epfl.biop.scijava.command.bdv.userdefinedregion.GetUserRectangleCommand`

Allows interactive selection of a 2D rectangular region in the current BDV view plane.

| Parameter | Description |
|-----------|-------------|
| `message_for_user` | Instructions displayed to the user |
| `time_out_in_ms` | Timeout in milliseconds (-1 for no timeout) |

| Output | Description |
|--------|-------------|
| `px`, `py` | Top-left corner coordinates |
| `sx`, `sy` | Rectangle width and height |

---

## 3D Box Selection

### Command: Get User 3D Box

**Class**: `ch.epfl.biop.scijava.command.bdv.userdefinedregion.GetUserBox3DCommand`

Allows interactive selection of a 3D bounding box in the viewer.

| Parameter | Description |
|-----------|-------------|
| `message_for_user` | Instructions displayed to the user |
| `time_out_in_ms` | Timeout in milliseconds (-1 for no timeout) |

| Output | Description |
|--------|-------------|
| `px`, `py`, `pz` | Box origin coordinates (corner) |
| `sx`, `sy`, `sz` | Box dimensions (width, height, depth) |

---

## How to Select Regions

### Rectangle Selection Workflow

1. A command triggers rectangle selection mode
2. Message appears guiding the user
3. Click and drag to define rectangle corners
4. Rectangle is drawn in the current view plane
5. Release to confirm the selection

### 3D Box Selection Workflow

1. A command triggers 3D box selection mode
2. Message appears guiding the user
3. Define the XY extent in the current view
4. Navigate in Z to set depth
5. Confirm the 3D region

### Controls

| Action | Effect |
|--------|--------|
| **Click + drag** | Define rectangle extent |
| **Navigate** | Standard BDV navigation still works |
| **Scroll Z** | Adjust Z extent for 3D boxes |
| **Confirm** | Accept current region |
| **Cancel** | Discard selection |

---

## Use Cases

### Cropping Operations

Region selection is commonly used for:

**2D cropping:**
```
1. Open image in BDV
2. Navigate to area of interest
3. Start crop command
4. Draw rectangle around region
5. Export cropped region
```

**3D subvolume extraction:**
```
1. Open 3D dataset in BDV
2. Navigate to region of interest
3. Select 3D box boundaries
4. Extract subvolume
5. Process or export
```

### Defining Processing Regions

Commands that need spatial boundaries can use region selection:
- Deconvolution regions
- Fusion boundaries
- Analysis ROIs
- Export extents

---

## Coordinate Systems

### View vs World Coordinates

| Coordinate System | Description |
|-------------------|-------------|
| **View coordinates** | Pixels in the current display |
| **World coordinates** | Physical units (µm, mm) |

Region selection typically returns world coordinates that:
- Respect image calibration
- Are independent of zoom level
- Can be applied to registered sources

### Axis Alignment

Rectangles are aligned to the current view:
- XY plane when viewing from top
- XZ plane when viewing from front
- Arbitrary plane when view is rotated

:::{tip}
For axis-aligned regions, ensure your view is oriented along a standard axis (XY, XZ, or YZ) before selecting.
:::

---

## Integration with Commands

### Commands Using Region Selection

Region selection integrates with various workflows:

| Workflow | How Regions Are Used |
|----------|---------------------|
| Cropping | Define crop boundaries |
| Export | Specify export extent |
| Processing | Limit computation area |
| Resampling | Define output bounds |

### Scripting

Region selection can be triggered from scripts:
```groovy
// Example: Get rectangle from user
result = commandService.run(GetUserRectangleCommand.class, true,
    "message_for_user", "Draw a rectangle around the region",
    "time_out_in_ms", -1
).get()

px = result.getOutput("px")
py = result.getOutput("py")
sx = result.getOutput("sx")
sy = result.getOutput("sy")
```

```groovy
// Example: Get 3D box from user
result = commandService.run(GetUserBox3DCommand.class, true,
    "message_for_user", "Define the 3D region",
    "time_out_in_ms", -1
).get()

// Access all 6 parameters
px = result.getOutput("px")
py = result.getOutput("py")
pz = result.getOutput("pz")
sx = result.getOutput("sx")
sy = result.getOutput("sy")
sz = result.getOutput("sz")
```

---

## Rectangle vs Box Selection

### When to Use Each

| Use Rectangle (2D) | Use Box (3D) |
|--------------------|--------------|
| Single slice operations | Volume extraction |
| 2D projections | 3D cropping |
| Current plane only | Full Z range needed |
| Quick region marking | Subvolume processing |

### Converting Between Them

A rectangle can be extended to a 3D box:
- Add current Z position for single slice
- Add full Z range for all slices
- Add custom Z bounds for partial stack

---

## Tips

### Accurate Region Definition

1. **Zoom appropriately**: Match zoom to the precision needed
2. **Use grid overlays**: If available, for alignment
3. **Check all dimensions**: Especially Z for 3D boxes
4. **Verify before confirming**: Review selection visually

### Working with Large Datasets

For large datasets:
- Regions can be defined at any resolution level
- Coordinates are stored in world units
- Actual extraction happens at chosen resolution

### Multiple Regions

When defining multiple regions:
- Select one region per command call
- Use scripts to collect multiple regions
- Store coordinates for batch processing

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Wrong region size | Defined at wrong zoom | Check coordinates in world units |
| Region in wrong Z | Z not set correctly | Navigate to correct Z before/during selection |
| Selection cancelled | Timeout or accidental cancel | Increase timeout, try again |
| Misaligned region | View was rotated | Align view to standard axis first |

---

## Related Topics

- [Point Selection](point_selection.md) - Individual point selection
- [Export Formats](../processing_images/export_formats.md) - Exporting selected regions
- [Resampling](../processing_images/resampling.md) - Processing selected regions
