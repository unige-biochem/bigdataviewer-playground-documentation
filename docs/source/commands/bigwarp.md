# Registration with BigWarp

[BigWarp](https://imagej.net/plugins/bigwarp) is a powerful tool for landmark-based image registration. BigDataViewer Playground integrates seamlessly with BigWarp, allowing you to perform both rigid and non-rigid (deformable) registration of sources.

## What is BigWarp?

BigWarp enables:
- **Landmark-based registration**: Place corresponding points on fixed and moving images
- **Rigid transformations**: Translation, rotation, scaling
- **Non-rigid transformations**: Thin-plate spline deformations for complex alignments
- **Real-time preview**: See the warped result as you add landmarks

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BigWarp interface showing two panels and landmarks -->

---

## Launching BigWarp

### Start BigWarp from Sources

**Command**: `BigWarp - Launch BigWarp`
**Class**: `sc.fiji.bdvpg.scijava.command.source.BigWarpLauncherCommand`

Launches BigWarp with specified fixed and moving sources.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `fixedsources` | Source(s) that define the target space (will not move) |
| `movingsources` | Source(s) to be warped to match the fixed sources |
| `bigwarpname` | Window title for the BigWarp session |

**Output**:
| Output | Description |
|--------|-------------|
| `bdvhp` | BDV handle for the "moving" panel |
| `bdvhq` | BDV handle for the "fixed" panel |
| `warpedsources` | The warped version of the moving sources |
| `gridsource` | A grid visualization showing the deformation field |
| `warpmagnitudesource` | A source showing the magnitude of deformation |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BigWarp launcher dialog -->

---

## Using BigWarp

### Basic Workflow

1. **Launch BigWarp** using the command above
2. **Navigate** to a recognizable feature in both panels
3. **Add landmarks**:
   - Click on a point in the moving image (left panel)
   - Click on the corresponding point in the fixed image (right panel)
4. **Repeat** for multiple landmarks (more = better for non-rigid)
5. **Toggle preview** to see the warped result
6. **Apply** the transformation when satisfied

### Keyboard Shortcuts in BigWarp

| Key | Action |
|-----|--------|
| `Space` | Add landmark at current cursor position |
| `T` | Toggle transformation preview |
| `Q` | Toggle between moving and fixed panel |
| `U` | Undo last landmark |
| `Ctrl+S` | Save landmarks |
| `Ctrl+E` | Export transformed image |

<!-- TODO:MISSING_CONTENT: [type: example] - Step-by-step BigWarp tutorial with screenshots -->

---

## Understanding the Outputs

When BigWarp is launched, several output sources are automatically created:

### Warped Sources

The `warpedsources` output contains the moving sources transformed according to the current landmark configuration. As you add or move landmarks, these sources update in real-time.

:::{note}
The warped sources are virtual - the transformation is computed on-the-fly. Export them using [export commands](import_export.md) to save the result.
:::

### Grid Source

The `gridsource` shows a regular grid deformed by the current transformation. This helps visualize:
- Where the deformation is strongest
- Whether the transformation is smooth
- Areas that might be over-deformed

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Grid source showing deformation pattern -->

### Warp Magnitude Source

The `warpmagnitudesource` shows the magnitude of displacement at each point as an intensity image. Brighter areas indicate larger displacements.

---

## Registration Strategies

### Rigid Registration (Few Landmarks)

For simple alignment requiring only translation, rotation, and scaling:
- Place **3-4 landmarks** on well-defined features
- Landmarks should be distributed across the image
- Useful for: correcting rotation, rough positioning

### Non-Rigid Registration (Many Landmarks)

For deformable registration accommodating local distortions:
- Place **10+ landmarks** throughout the volume
- Focus extra landmarks on areas needing local correction
- Useful for: tissue deformation, histology alignment, atlas registration

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Comparison of rigid vs non-rigid registration -->

### Tips for Good Registration

1. **Start coarse, refine fine**: Begin with landmarks on major features, then add detail
2. **Distribute landmarks evenly**: Avoid clustering all landmarks in one area
3. **Use multiple z-planes**: For 3D data, place landmarks at different depths
4. **Check the grid**: Use the grid source to identify poorly constrained areas
5. **Save landmarks regularly**: Use `Ctrl+S` to save your work

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script to launch BigWarp and export results -->

---

## Integration with BDV Playground

After registration in BigWarp:

1. **Warped sources appear in the service**: They can be used like any other source
2. **Display in other viewers**: Add warped sources to existing BDV windows
3. **Further processing**: Apply additional transformations, adjust appearance
4. **Export**: Save the registered result to disk

### Workflow Example

```
1. Import fixed and moving images
2. Launch BigWarp
3. Add landmarks and register
4. Close BigWarp (warped sources remain)
5. Display warped sources alongside fixed sources
6. Export the aligned result
```

<!-- TODO:MISSING_CONTENT: [type: script] - Complete registration and export workflow -->

---

## Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| Transformation looks wrong | Check that landmarks are in the correct panel (moving vs fixed) |
| Excessive deformation | Add more landmarks in the affected area |
| Registration doesn't update | Press `T` to toggle transformation preview |
| Sources look stretched | Verify that fixed and moving sources have correct calibration |

### Saving and Loading Landmarks

BigWarp allows saving landmark configurations:
- **Save**: `File > Export landmarks` in BigWarp
- **Load**: `File > Import landmarks` in BigWarp

This enables iterative refinement across sessions.

<!-- TODO:MISSING_CONTENT: [type: example] - Save/load landmarks workflow -->

---

## Summary

| Command | Purpose |
|---------|---------|
| `BigWarpLauncherCommand` | Launch BigWarp for landmark-based registration |

### Related Resources

- [BigWarp Documentation](https://imagej.net/plugins/bigwarp)
- [Transformations](transformations.md) for basic transforms before BigWarp
- [Import & Export](import_export.md) for saving registered results
