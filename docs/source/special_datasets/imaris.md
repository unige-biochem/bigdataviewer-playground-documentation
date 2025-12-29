# Imaris Files

BigDataViewer Playground can directly open Bitplane Imaris `.ims` files, providing access to multi-resolution data without conversion.

## Overview

Imaris is a popular 3D/4D visualization and analysis software. Its native `.ims` format stores:

- Multi-resolution pyramids
- Multiple channels
- Time-series data
- Metadata and display settings

BigDataViewer Playground reads Imaris files directly, leveraging the built-in pyramid structure for efficient visualization.

## Opening Imaris Files

### Command: Create BDV Dataset [Imaris]

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Create BDV Dataset [Imaris]`
**Class**: `ch.epfl.biop.scijava.command.spimdata.OpenImarisCommand`

| Parameter | Description |
|-----------|-------------|
| `file` | Path to the Imaris `.ims` file |

| Output | Description |
|--------|-------------|
| `spimdata` | The opened Imaris dataset |

### Workflow

```
1. Run Create BDV Dataset [Imaris]
2. Select your .ims file
3. Dataset appears in BDV Playground tree
4. Right-click to display in BDV window
```

---

## Imaris Format Features

### Multi-Resolution Support

Imaris files contain pre-computed resolution levels:
- Smooth zooming in BigDataViewer
- Efficient navigation of large datasets
- No additional pyramidization needed

### Channel Handling

Each Imaris channel becomes a separate source:
- Individual color control
- Independent visibility
- Separate brightness/contrast

### Time-Series

Time-lapse Imaris files are fully supported:
- Use time slider in BDV
- Navigate through timepoints
- Export specific time ranges

---

## Workflow Examples

### Basic Visualization

```
1. Open .ims file
2. Display in BDV window
3. Navigate with standard BDV controls
4. Adjust channel colors and brightness
```

### Channel Comparison

```
1. Open multi-channel .ims file
2. Toggle channels on/off to compare
3. Adjust individual channel colors
4. Create merged view
```

### Export to Other Formats

```
1. Open .ims file
2. Select sources to export
3. Export to OME-TIFF or XML/HDF5
4. Use in other analysis tools
```

### Integration with Fiji Analysis

```
1. Open .ims file in BDV Playground
2. Navigate to region of interest
3. Export current view to ImagePlus
4. Analyze with Fiji tools
```

---

## Performance

### Efficient Loading

- Multi-resolution pyramid enables fast navigation
- Only visible data is loaded
- Large files (100+ GB) work smoothly

### Comparison with Other Formats

| Aspect | Imaris | Converting to HDF5 |
|--------|--------|-------------------|
| Speed | Native, fast | Requires conversion time |
| Pyramid | Pre-computed | Must be generated |
| Compatibility | Imaris-specific | Broader BDV ecosystem |

---

## Limitations

### Read-Only Access

- BDV Playground reads Imaris files but doesn't write back
- To save changes, export to another format

### Imaris-Specific Features

Some Imaris features are not imported:
- Surfaces and spots (analysis objects)
- Measurement results
- Annotations

Only the image data and basic metadata are accessible.

---

## When to Use Imaris Import

**Good for:**
- Viewing existing Imaris datasets in Fiji
- Combining Imaris data with other sources
- Exporting subsets for analysis
- Quick visualization without conversion

**Consider alternatives when:**
- You need to modify and save back to Imaris
- You need Imaris-specific analysis features
- You're starting a new project (use native BDV formats)

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| File won't open | Corrupted or unsupported version | Try opening in Imaris first to verify |
| Missing channels | Incomplete file | Check file integrity |
| Slow initial open | Large file, first access | Normal; metadata parsing takes time |
| Wrong colors | Default colors applied | Adjust in BDV Playground |

---

## Related Topics

- [Opening Images](../opening_images/opening_images.md) - General import methods
- [Export Formats](../processing_images/export_formats.md) - Save to other formats
- [Visualizing Images](../visualizing_images/visualizing_images.md) - Display options
