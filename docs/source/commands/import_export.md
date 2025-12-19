# Import and Export

BigDataViewer Playground supports various file formats for importing and exporting image data. This section covers the available commands for loading data into the system and saving results.

## Supported Formats

### Import Formats

| Format | Description |
|--------|-------------|
| **XML/HDF5** | Native BDV format, pyramidal, chunked |
| **XML/N5** | N5 backend for BDV |
| **OME-ZARR** | Cloud-ready, S3-compatible format |
| **BigDataServer** | Remote streaming from BDV server |

### Export Formats

| Format | Description |
|--------|-------------|
| **XML/HDF5** | Standard BDV format with multi-resolution |
| **SpimData XML** | Metadata-only export referencing existing data |

---

## Importing Data

### Import Multiple SPIM Data Files

**Command**: `Import - Open multiple files`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.MultipleSpimDataImporterCommand`

Opens multiple image files at once. Supports various BDV-compatible formats including XML/HDF5, XML/N5, and OME-ZARR.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `files` | File(s) to import |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - File selection dialog for multiple imports -->

### Supported File Types

The importer automatically detects the file type:

- **`.xml`** files: Looks for associated HDF5 or N5 data
- **`.zarr`** directories: OME-ZARR format
- **`.json`** files: BDV metadata files

:::{tip}
You can select multiple files at once by holding `Ctrl` (Windows/Linux) or `Cmd` (Mac) while clicking.
:::

---

### Import from BigDataServer

**Command**: `Import - Open from BigDataServer`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.SpimdataBigDataServerImportCommand`

Opens a dataset from a remote BigDataServer. This allows streaming large datasets without downloading them locally.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `urlserver` | URL of the BigDataServer |
| `datasetname` | Name of the dataset to open |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - BigDataServer connection dialog -->

### BigDataServer URL Format

The URL should point to the BigDataServer instance, typically:
```
http://server-address:port
```

:::{note}
BigDataServer streams data on-demand. Only the visible portions are downloaded, making it efficient for large datasets.
:::

<!-- TODO:MISSING_CONTENT: [type: example] - Example BigDataServer URLs and dataset names -->

---

## Exporting Data

### Export to XML/HDF5

**Command**: `Export - Save as XML/HDF5`
**Class**: `sc.fiji.bdvpg.scijava.command.source.XmlHDF5ExporterCommand`

Exports sources to the native BigDataViewer XML/HDF5 format with multi-resolution pyramids for efficient viewing.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to export |
| `xmlfile` | Output file path (.xml) |
| `timepointbegin` | Starting timepoint (0-based) |
| `numberoftimepointtoexport` | Number of timepoints to export |
| `blocksizex`, `blocksizey`, `blocksizez` | HDF5 chunk dimensions |
| `scalefactor` | Scale factor between pyramid levels |
| `thresholdformipmap` | Size threshold for creating new resolution levels |
| `nthreads` | Number of threads for export |
| `entitytype` | How to organize sources (each as independent) |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Export dialog with parameters -->

### Understanding Export Parameters

#### Block Size

The block size determines how data is chunked in the HDF5 file:
- **Smaller blocks** (e.g., 32x32x32): Better for random access
- **Larger blocks** (e.g., 128x128x32): Better for sequential reading

:::{tip}
For typical 3D microscopy data, block sizes of 64x64x32 or 32x32x16 work well.
:::

#### Scale Factor and MipMap Threshold

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

#### Entity Type

Determines how multiple sources are organized:
- **Independent**: Each source is a separate entity (typical use)

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script for batch export with optimal parameters -->

---

### Export SpimData Metadata

**Command**: `Export - Save SpimData`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.SpimDataExporterCommand`

Exports the metadata (transformations, calibrations) for sources as a SpimData XML file. This is useful for:
- Saving registration results
- Creating references to existing data
- Archiving processing parameters

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to export |
| `xmlfilepath` | Output file path (.xml) |

:::{note}
This exports metadata only. The actual image data must already exist and be referenced correctly.
:::

---

## Workflow Examples

### Complete Import-Process-Export Workflow

```
1. Import data: MultipleSpimDataImporterCommand
2. Apply transformations (see Transformations section)
3. Adjust appearance (see Appearance section)
4. Export result: XmlHDF5ExporterCommand
```

<!-- TODO:MISSING_CONTENT: [type: script] - Complete workflow script -->

### Working with Remote Data

```
1. Connect to BigDataServer: SpimdataBigDataServerImportCommand
2. Process data (transformations applied on-the-fly)
3. Export processed result locally: XmlHDF5ExporterCommand
```

:::{tip}
When working with remote data, only export the final result to avoid unnecessary data transfer.
:::

---

## Performance Tips

### Import Performance

- **Local SSD**: Fastest for XML/HDF5
- **Network storage**: Consider BigDataServer for remote access
- **Large datasets**: Use lazy loading (data loaded on-demand)

### Export Performance

| Parameter | Impact |
|-----------|--------|
| `nthreads` | More threads = faster export (up to CPU cores) |
| `blocksizez` | Larger Z blocks improve sequential write speed |
| Compression | HDF5 uses GZIP by default - good balance |

---

## Troubleshooting

### Common Import Issues

| Problem | Solution |
|---------|----------|
| "File not found" | Check that both XML and data files exist |
| Slow loading | Data may be on network storage - consider copying locally |
| Memory errors | Dataset may be too large - check available RAM |

### Common Export Issues

| Problem | Solution |
|---------|----------|
| "Disk full" | HDF5 files can be large - ensure sufficient space |
| Export hangs | Reduce `nthreads` if system becomes unresponsive |
| Corrupted output | Ensure export completes - don't interrupt |

---

## Summary

| Command | Purpose |
|---------|---------|
| `MultipleSpimDataImporterCommand` | Import multiple files |
| `SpimdataBigDataServerImportCommand` | Import from BigDataServer |
| `XmlHDF5ExporterCommand` | Export to XML/HDF5 format |
| `SpimDataExporterCommand` | Export SpimData metadata |
