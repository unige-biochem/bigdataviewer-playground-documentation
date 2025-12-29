# Import and Export

## Importing Data

:::{note}
**Import commands have moved!** For comprehensive documentation on opening and importing images, including Bio-Formats, OMERO, QuPath, and BigDataServer, see the [Opening and Saving Images](../opening_images/opening_images.md) section.
:::

---

## Exporting Data

### Export to XML/HDF5

**Command**: `Export - Save as XML/HDF5`
**Class**: `sc.fiji.bdvpg.scijava.command.source.XmlHDF5ExporterCommand`

Exports sources to the native BigDataViewer XML/HDF5 format with multi-resolution pyramids for efficient viewing.

| Parameter | Type | Description |
|-----------|------|-------------|
| `sacs` | SourceAndConverter[] | Source(s) to export |
| `xmlfile` | File | Output file path (.xml) |
| `timepointbegin` | int | Starting timepoint (0-based) |
| `numberoftimepointtoexport` | int | Number of timepoints to export |
| `blocksizex`, `blocksizey`, `blocksizez` | int | HDF5 chunk dimensions |
| `scalefactor` | int | Scale factor between pyramid levels |
| `thresholdformipmap` | int | Size threshold for creating new resolution levels |
| `nthreads` | int | Number of threads for export |
| `entitytype` | String | How to organize sources (each as independent) |

#### Understanding Export Parameters

**Block Size:**
The block size determines how data is chunked in the HDF5 file:
- **Smaller blocks** (e.g., 32x32x32): Better for random access
- **Larger blocks** (e.g., 128x128x32): Better for sequential reading

:::{tip}
For typical 3D microscopy data, block sizes of 64x64x32 or 32x32x16 work well.
:::

**Scale Factor and MipMap Threshold:**
The exporter creates a multi-resolution pyramid:
- **`scalefactor`**: How much each level is downsampled (e.g., 2 = half size)
- **`thresholdformipmap`**: Minimum dimension size before creating a new level

Example with `scalefactor=2` and `thresholdformipmap=64`:
```
Level 0: 1024 x 1024 x 256  (original)
Level 1:  512 x  512 x 128
Level 2:  256 x  256 x  64
Level 3:  128 x  128 x  32  (stops here, below threshold)
```

---

### Export SpimData Metadata

**Command**: `Export - Save SpimData`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.SpimDataExporterCommand`

Exports the metadata (transformations, calibrations) for sources as a SpimData XML file. This is useful for:
- Saving registration results
- Creating references to existing data
- Archiving processing parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `sacs` | SourceAndConverter[] | Source(s) to export |
| `xmlfilepath` | File | Output file path (.xml) |

:::{note}
This exports metadata only. The actual image data must already exist and be referenced correctly.
:::

---

## Performance Tips

### Export Performance

| Parameter | Impact |
|-----------|--------|
| `nthreads` | More threads = faster export (up to CPU cores) |
| `blocksizez` | Larger Z blocks improve sequential write speed |
| Compression | HDF5 uses GZIP by default - good balance |

---

## Troubleshooting

### Common Export Issues

| Problem | Solution |
|---------|----------|
| "Disk full" | HDF5 files can be large - ensure sufficient space |
| Export hangs | Reduce `nthreads` if system becomes unresponsive |
| Corrupted output | Ensure export completes - don't interrupt |

---

## Summary

| Command | Class | Purpose |
|---------|-------|---------|
| `XmlHDF5ExporterCommand` | Export to XML/HDF5 format |
| `SpimDataExporterCommand` | Export metadata as XML |

For import commands, see [Opening and Saving Images](../opening_images/opening_images.md).
