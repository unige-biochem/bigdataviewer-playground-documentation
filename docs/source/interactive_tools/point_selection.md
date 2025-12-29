# Point Selection

BigDataViewer Playground provides interactive tools for selecting points in 3D space within the viewer.

## Overview

Point selection allows you to:
- Mark specific locations in your data
- Define landmarks for registration
- Specify coordinates for processing commands
- Annotate positions of interest

## Get User Points Command

### Command: Get User Points

**Class**: `ch.epfl.biop.scijava.command.bdv.userdefinedregion.GetUserPointsCommand`

Allows interactive selection of multiple points in the BDV viewer.

| Parameter | Description |
|-----------|-------------|
| `message_for_user` | Instructions displayed to the user |
| `time_out_in_ms` | Timeout in milliseconds (-1 for no timeout) |

| Output | Description |
|--------|-------------|
| `pts` | List of selected RealPoint coordinates |

---

## How to Select Points

### Basic Workflow

1. A command triggers point selection mode
2. Message appears guiding the user
3. Click in the BDV window to place points
4. Points are recorded in 3D world coordinates
5. Confirm selection when done

### Controls

| Action | Effect |
|--------|--------|
| **Left click** | Place a point at cursor location |
| **Navigate** | Standard BDV navigation still works |
| **Confirm** | Accept current points |
| **Cancel** | Discard selection |

---

## Use Cases

### Defining Landmarks

Point selection is commonly used for:

**Registration landmarks:**
```
1. Open fixed and moving images
2. Start registration command
3. Select corresponding points on both
4. Points define the transform
```

**ROI centers:**
```
1. Navigate to region of interest
2. Select center point
3. Use coordinates for cropping/export
```

### Specifying Coordinates

Commands that need spatial input can use point selection:
- Rotation centers
- Crop boundaries
- Transform origins
- Measurement locations

---

## Integration with Commands

### Commands Using Point Selection

Point selection is integrated into various workflows:

| Workflow | How Points Are Used |
|----------|---------------------|
| Registration | Landmark correspondences |
| Cropping | Define boundaries |
| Transforms | Specify centers |
| Analysis | Mark locations |

### Scripting

Point selection can be triggered from scripts:
```groovy
// Example: Get points from user
points = commandService.run(GetUserPointsCommand.class, true,
    "message_for_user", "Click to place landmarks",
    "time_out_in_ms", -1
).get().getOutput("pts")
```

---

## Tips

### Accurate Point Placement

1. **Zoom in**: Higher zoom = more precision
2. **Use orthogonal views**: XY, XZ, YZ for different perspectives
3. **Navigate in Z**: Ensure correct Z position before clicking
4. **Check coordinates**: Verify points are where expected

### Working with 3D Data

Points are placed in 3D world coordinates:
- X, Y from the view plane
- Z from the current slice position
- Coordinates respect image calibration

### Multiple Points

When selecting multiple points:
- Take your time for accuracy
- Use consistent ordering if order matters
- Verify all points before confirming

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Points in wrong Z | Didn't navigate to correct slice | Check Z position before clicking |
| Inaccurate placement | Zoomed out too far | Zoom in for precision |
| Selection cancelled | Timeout or accidental cancel | Increase timeout, try again |
| Wrong coordinates | Calibration issue | Verify image calibration |

---

## Related Topics

- [Region Selection](region_selection.md) - Rectangle and box selection
- [Registration](../registration/index.md) - Uses points for landmarks
- [Advanced Transforms](../advanced_transforms/index.md) - Point-based operations
