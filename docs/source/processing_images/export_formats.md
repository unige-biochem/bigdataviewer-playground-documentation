# Export Formats

BigDataViewer Playground supports exporting sources to various formats for downstream analysis, archiving, and sharing.

## Overview

| Format | Use Case | Multi-resolution | Compression |
|--------|----------|------------------|-------------|
| **OME-TIFF** | QuPath, general analysis | Yes (pyramidal) | LZW, JPEG-2000 |
| **XML/HDF5** | BDV ecosystem | Yes | GZIP |
| **ImagePlus** | ImageJ/Fiji analysis | No | N/A |
| **SpimData XML** | Metadata only | N/A | N/A |

---

## Export to OME-TIFF

OME-TIFF is the recommended format for exporting processed results. It's compatible with QuPath, OMERO, and many analysis tools.

### From Registration Pairs

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Register Pair - Export registration to OME-TIFF`

See [Warpy Workflow](../registration/warpy_workflow.md) for details.

### From BigStitcher Datasets

**Menu**: `Plugins > BigDataViewer-Playground > BDVDataset > Fuse a BigStitcher dataset to OME-Tiff`

| Parameter | Description |
|-----------|-------------|
| `xml_bigstitcher_file` | Input BigStitcher XML |
| `output_path_directory` | Output folder |
| `n_resolution_levels` | Pyramid levels (e.g., 4) |
| `use_lzw_compression` | Enable LZW compression |
| `split_slices/channels/frames` | Export as separate files |

### OME-TIFF Options

#### Resolution Levels

| Levels | Description |
|--------|-------------|
| 1 | Single resolution (no pyramid) |
| 3-4 | Typical for most images |
| 5-6 | Very large whole-slide images |

#### Compression

| Type | Trade-off |
|------|-----------|
| **None** | Fastest, largest files |
| **LZW** | Good compression, lossless |
| **JPEG-2000** | Better compression, slower |
| **JPEG-2000 Lossy** | Smallest, quality loss |

:::{tip}
LZW compression is a good default - it's lossless, well-supported, and provides reasonable file sizes.
:::

---

## Export to XML/HDF5

The native BigDataViewer format, ideal for staying within the BDV ecosystem.

### Command: Export to XML/HDF5

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Save as XML/HDF5`
**Class**: `sc.fiji.bdvpg.scijava.command.source.XmlHDF5ExporterCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to export |
| `xmlfile` | Output XML file path |
| `timepointbegin` | Starting timepoint (0-based) |
| `numberoftimepointtoexport` | Number of timepoints |
| `blocksizex/y/z` | HDF5 chunk dimensions |
| `scalefactor` | Downsampling between levels |
| `thresholdformipmap` | Size threshold for new levels |
| `nthreads` | Parallel threads |
| `entitytype` | How to organize sources |

### Block Size Recommendations

| Use Case | Block Size |
|----------|------------|
| Random access | 32x32x32 |
| Sequential reading | 64x64x32 |
| 2D time-lapse | 128x128x1 |

### Pyramid Generation

The `scalefactor` and `thresholdformipmap` parameters control automatic pyramid generation:

```
Example: scalefactor=2, thresholdformipmap=64

Level 0: 1024 x 1024 x 256 (original)
Level 1: 512 x 512 x 128
Level 2: 256 x 256 x 64
Level 3: 128 x 128 x 32 (stops - below threshold)
```

---

## Export to ImagePlus

For analysis in ImageJ/Fiji, export sources to ImagePlus format.

### From BDV View

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Current BDV View To ImagePlus`
**Class**: `ch.epfl.biop.scijava.command.bdv.BdvViewToImagePlusExportCommand`

| Parameter | Description |
|-----------|-------------|
| `bdv_h` | BDV window to export from |
| `sacs` | Source(s) to export |
| `capturename` | Name for ImagePlus |
| `matchwindowsize` | Use BDV window dimensions |
| `xsize/ysize/zsize` | Output size in world units |
| `samplingxyinphysicalunit` | Output XY pixel size |
| `samplingzinphysicalunit` | Output Z pixel size |
| `interpolate` | Use interpolation |
| `export_mode` | Normal or Virtual (lazy) |

### From Sources Directly

**Class**: `ch.epfl.biop.scijava.command.source.ExportToImagePlusCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Sources to export |
| `timepoint` | Timepoint to export |
| `resolution_level` | Resolution level (0 = full) |

### Virtual vs Normal Export

| Mode | Description | Use When |
|------|-------------|----------|
| **Normal** | Loads all data into RAM | Small datasets, immediate analysis |
| **Virtual** | Lazy-loading stack | Large datasets, viewing only |

---

## Export SpimData Metadata

Save only the metadata (positions, transforms, calibrations) without pixel data.

### Command: Export SpimData

**Menu**: `Plugins > BigDataViewer-Playground > Sources > Export > Save SpimData`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.SpimDataExporterCommand`

| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to export metadata for |
| `xmlfilepath` | Output XML file path |

:::{note}
This exports metadata only. The original image data must remain accessible for the saved dataset to work.
:::

Use cases:
- Saving registration transforms
- Archiving spatial configuration
- Sharing processing parameters

---

## Export Workflow Recommendations

### For QuPath Analysis

```
1. Process/register images in BDV Playground
2. Export to OME-TIFF with:
   - 4+ resolution levels
   - LZW compression
   - Appropriate pixel size
3. Import into QuPath
```

### For ImageJ Analysis

```
1. Process in BDV Playground
2. Export specific region via BDV view
3. Set appropriate output resolution
4. Analyze in ImageJ
```

### For Archiving

```
1. Process/register images
2. Export to XML/HDF5 for BDV compatibility
   OR
3. Export to OME-TIFF for broader compatibility
4. Include metadata export for reproducibility
```

### For Sharing

```
1. Export to OME-TIFF (most compatible)
2. Use LZW compression
3. Include appropriate resolution levels
4. Document processing parameters
```

---

## Performance Tips

### Large Dataset Export

| Issue | Solution |
|-------|----------|
| Slow export | Increase `nthreads` |
| Memory errors | Use lower resolution, split files |
| Disk full | Check space, use compression |

### Export Speed Optimization

| Factor | Recommendation |
|--------|----------------|
| Threads | Match CPU cores |
| Compression | LZW for balance |
| Resolution | Only needed levels |
| Network storage | Copy locally first |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Export hangs | Memory full | Reduce data size, increase RAM |
| Corrupted file | Interrupted export | Delete and re-export |
| Can't open result | Wrong format | Verify file extension and format |
| Very large file | No compression | Enable LZW compression |
| Poor quality | Wrong resolution | Increase output resolution |

---

## Format Comparison

| Feature | OME-TIFF | XML/HDF5 | ImagePlus |
|---------|----------|----------|-----------|
| Multi-resolution | Yes | Yes | No |
| Compression | Multiple | GZIP | N/A |
| QuPath compatible | Yes | No | Via TIFF |
| BDV compatible | Via loader | Native | Via import |
| Metadata | OME-XML | Custom | Limited |
| Max file size | ~4GB/file | Very large | ~2GB |

---

## Related Topics

- [Fusion](fusion.md) - Prepare data for export
- [Resampling](resampling.md) - Control output resolution
- [Import & Export Commands](../commands/import_export.md) - Command reference
