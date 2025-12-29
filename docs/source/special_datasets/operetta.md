# PerkinElmer Operetta

BigDataViewer Playground supports opening high-content screening data from PerkinElmer Operetta systems.

## Overview

The Operetta is a high-content imaging system used for automated microscopy of multi-well plates. BigDataViewer Playground can:

- Open Operetta datasets directly
- Handle multi-well, multi-field, multi-channel data
- Display all images in a spatial context
- Apply consistent display settings

## Opening Operetta Datasets

### Command: Create BDV Dataset [Operetta]

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Operetta]`
**Class**: `ch.epfl.biop.scijava.command.spimdata.OpenOperettaDatasetCommand`

| Parameter | Description |
|-----------|-------------|
| `folder` | The 'Images' or 'flex' folder containing your Operetta data |
| `unit` | World coordinate units (e.g., "micrometer") |
| `min_display_value` | Minimum intensity for display |
| `max_display_value` | Maximum intensity for display |
| `show` | Open in a new BDV window immediately |

| Output | Description |
|--------|-------------|
| `dataset_name` | Name assigned to the opened dataset |

---

## Dataset Structure

### Operetta Data Organization

Operetta datasets typically contain:
- **Wells**: Multiple wells from a plate (e.g., A1, A2, B1...)
- **Fields**: Multiple imaging positions per well
- **Channels**: Different fluorescence channels
- **Z-stacks**: Optional 3D acquisition
- **Timepoints**: Time-lapse data

### How BDV Playground Handles This

Each field becomes a source in the BDV Playground tree:
- Sources are positioned according to well/field coordinates
- Channels appear as separate sources
- Metadata is preserved for filtering and organization

---

## Workflow

### Basic Opening

```
1. Locate your Operetta 'Images' folder
2. Run Create BDV Dataset [Operetta]
3. Select the folder
4. Set display range (or use defaults)
5. Enable 'show' to open immediately
```

### Viewing the Plate

After opening:
1. Use the BDV navigation to pan across the plate
2. Zoom in to see individual wells
3. Zoom further to see individual fields
4. Use the source tree to select specific wells/channels

### Analyzing Specific Wells

```
1. Open Operetta dataset
2. Filter sources by well name (using metadata)
3. Select specific well sources
4. Export to ImagePlus for analysis
```

---

## Display Settings

### Initial Display Range

The `min_display_value` and `max_display_value` parameters set the initial brightness/contrast:

| Scenario | Recommendation |
|----------|----------------|
| Unknown data | Leave at defaults, adjust in BDV |
| Known intensity range | Set appropriate min/max |
| Comparing experiments | Use consistent values |

### Adjusting After Opening

Use the standard BDV Playground brightness controls to adjust display:
- Right-click on source > Adjust brightness
- Or use interactive brightness command

---

## Performance Considerations

### Large Plates

For plates with many wells/fields:
- Initial loading may take time (metadata parsing)
- Navigation is efficient (lazy loading)
- Consider filtering to subset of wells for analysis

### Memory

- Images are loaded on-demand
- Viewing many fields simultaneously uses more RAM
- Close unused BDV windows to free memory

---

## Common Workflows

### Screen Overview

```
1. Open Operetta dataset
2. Zoom out to see entire plate
3. Identify wells of interest
4. Zoom in for detailed inspection
```

### Well Comparison

```
1. Open dataset
2. Create groups for wells to compare
3. Display selected wells side-by-side
4. Synchronize views for comparison
```

### Export for Analysis

```
1. Open dataset
2. Select wells/fields of interest
3. Export to ImagePlus or OME-TIFF
4. Process in Fiji or other tools
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| No images found | Wrong folder selected | Select the 'Images' or 'flex' folder |
| Missing wells | Incomplete dataset | Verify data integrity on disk |
| Wrong positions | Metadata issue | Check Operetta export settings |
| Slow opening | Large dataset | Normal; wait for metadata parsing |

---

## Related Topics

- [Opening Images](../opening_images/opening_images.md) - General import methods
- [Export Formats](../processing_images/export_formats.md) - Save Operetta data
- [Organizing Sources](../commands/organizing_sources.md) - Group and filter sources
