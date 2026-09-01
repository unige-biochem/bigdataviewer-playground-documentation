# Exporting Images

Once you have imported, visualized, and processed your data, you need to export it — either to a file on disk or to a standard Fiji ImagePlus for further analysis. BigDataViewer Playground offers several export paths depending on the target format and whether you are exporting sources from the workspace or a snapshot of a BDV viewer.

All main export commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Export`

View-based exports (capturing what you see in a BDV window) are under:

{menuselection}`Plugins > BigDataViewer-Playground > Display > BDV > Export`

Standalone file-to-file conversion tools (Kheops) are under:

{menuselection}`Plugins > BIOP > Kheops`

---

## Export To OME-TIFF

*Source: {kheops-src}`KheopsExportSourcesCommand.java <ch/epfl/biop/kheops/command/KheopsExportSourcesCommand.java>`*

The primary command for saving sources to disk. Produces a pyramidal OME-TIFF — a widely supported format that preserves multi-resolution levels, multi-channel structure, and physical calibration. This is usually the best choice for archiving or sharing processed data.

| Parameter | Description |
|-----------|-------------|
| Sources to export | The sources to save (each source becomes a channel) |
| Output file | Path to the output `.ome.tiff` file |
| Number of resolution levels | Number of pyramid levels to generate |
| Scaling factor between resolution levels | Downsampling factor between consecutive levels |
| Tile Size X / Y | Tile dimensions for the TIFF (negative = no tiling) |
| Number of threads (0 = serial) | Parallel threads for writing |
| Compression type | Compression algorithm (e.g. LZW, ZLIB, Uncompressed) |
| Compress temporary files | Use LZW compression on temporary files during pyramid building (saves disk space) |
| Selected Channels | Channel indices to export (e.g. `0,1` or `0:2`). Leave blank for all |
| Selected Timepoints | Timepoint indices to export. Leave blank for all |
| Selected Slices | Z-slice indices to export. Leave blank for all |
| Override voxel sizes | When checked, uses the custom voxel sizes below instead of the source metadata |
| Voxel size in micrometer (XY) | Custom XY pixel size |
| Voxel Z size in micrometer (Z) | Custom Z pixel size |
| Physical unit | Unit string written into the OME-TIFF metadata |

:::{tip}
The output is always recomputed from the highest resolution level of each source, so the pyramid levels in the OME-TIFF are internally consistent regardless of how many levels the input sources had.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Export > Source - Export To OME-TIFF`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Export To OME-TIFF");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sacs
#@CommandService cs

import ch.epfl.biop.kheops.command.KheopsExportSourcesCommand

cs.run(KheopsExportSourcesCommand, true,
    "sacs", sacs,
    "file", new java.io.File("/path/to/output.ome.tiff"),
    "n_resolution_levels", 5,
    "downscaling", 2,
    "tile_size_x", 512,
    "tile_size_y", 512,
    "n_threads", 4,
    "compression", "LZW",
    "compress_temp_files", false,
    "range_channels", "",
    "range_frames", "",
    "range_slices", "",
    "override_voxel_size", false,
    "vox_size_xy_um", 1.0,
    "vox_size_z_um", 1.0,
    "unit", "MICROMETER"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sacs
#@CommandService cs

from ch.epfl.biop.kheops.command import KheopsExportSourcesCommand
from java.io import File

cs.run(KheopsExportSourcesCommand, True,
    ["sacs", sacs,
     "file", File("/path/to/output.ome.tiff"),
     "n_resolution_levels", 5,
     "downscaling", 2,
     "tile_size_x", 512,
     "tile_size_y", 512,
     "n_threads", 4,
     "compression", "LZW",
     "compress_temp_files", False,
     "range_channels", "",
     "range_frames", "",
     "range_slices", "",
     "override_voxel_size", False,
     "vox_size_xy_um", 1.0,
     "vox_size_z_um", 1.0,
     "unit", "MICROMETER"]
).get()
```
::::

:::::

---

## Export To ImagePlus

*Source: {biop-src}`SourcesToMultipleImagePlusExportCommand.java <ch/epfl/biop/command/exporter/SourcesToMultipleImagePlusExportCommand.java>`*

Converts sources back to standard Fiji ImagePlus stacks. Use this when you need to hand your data off to classic ImageJ/Fiji plugins that don't work with BDV sources.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to export |
| Resolution Level | Pyramid level to export (0 = highest resolution) |
| Export Mode | **Normal** loads all data into memory; **Virtual** creates a lazy-loading stack |
| Split by Entities | Comma-separated entity types to split by (e.g. `channel, imagename`) |
| Selected Channels | Channel indices to export (e.g. `0:2` or `0,1`). Leave blank for all |
| Selected Timepoints | Timepoint indices to export. Leave blank for all |
| Selected Slices | Z-slice indices to export. Leave blank for all |
| Monitor Progress | Show a progress indicator during export |
| Export in Parallel | Export multiple images simultaneously |
| Parallel Channels / Timepoints / Slices | Acquire each dimension in parallel (Normal mode only) |

:::{important}
**Normal** mode loads the entire exported region into RAM. For large sources, use a higher resolution level or subset the slices/timepoints to avoid running out of memory. **Virtual** mode is memory-efficient but slower for random access.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Export > Source - Export To ImagePlus`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Export To ImagePlus");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.exporter.SourcesToMultipleImagePlusExportCommand

cs.run(SourcesToMultipleImagePlusExportCommand, true,
    "sources", sources,
    "level", 0,
    "export_mode", "Normal",
    "entities_split", "channel",
    "range_channels", "",
    "range_frames", "",
    "range_slices", "",
    "monitor", true,
    "parallel", false
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.exporter import SourcesToMultipleImagePlusExportCommand

cs.run(SourcesToMultipleImagePlusExportCommand, True,
    ["sources", sources,
     "level", 0,
     "export_mode", "Normal",
     "entities_split", "channel",
     "range_channels", "",
     "range_frames", "",
     "range_slices", "",
     "monitor", True,
     "parallel", False]
).get()
```
::::

:::::

---

## Export To XML/HDF5 Dataset

*Source: {bdvpg-src}`SourceXMLHDF5ExportCommand.java <sc/fiji/bdvpg/command/exporter/SourceXMLHDF5ExportCommand.java>`*

Exports sources to the native BigDataViewer XML/HDF5 format. This is useful when you want to save processed sources in a format that can be re-opened directly in BigDataViewer or BigStitcher.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to export |
| Output file (XML) | Path to the output `.xml` file (the `.h5` file is created alongside it) |
| Each source is an independent | How to treat each source in the dataset (e.g. Channel, Tile, Illumination) |
| Timepoint start | First timepoint to export (0-based) |
| Number of timepoints | Number of timepoints to export |
| Block size X / Y / Z | HDF5 chunk size in each dimension |
| Scale factor | Downsampling factor between pyramid levels |
| MipMap threshold | Minimum dimension size (in pixels) above which a new pyramid level is created |
| Number of Threads | Parallel threads for writing |

:::{tip}
The **entity type** parameter controls how sources are organized in the XML/HDF5 structure. Choose **Channel** if each source is a different fluorescence channel, **Tile** if they are spatial tiles, etc. This affects how the dataset appears when re-opened.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Export > Source - Export To XML/HDF5 Dataset`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Export To XML/HDF5 Dataset");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.exporter.SourceXMLHDF5ExportCommand

cs.run(SourceXMLHDF5ExportCommand, true,
    "sources", sources,
    "xml_file", new java.io.File("/path/to/output.xml"),
    "entity_type", "Channel",
    "timepoint_begin", 0,
    "number_of_timepoints_to_export", 1,
    "block_size_x", 32,
    "block_size_y", 32,
    "block_size_z", 4,
    "scale_factor", 2,
    "threshold_mipmap", 16,
    "n_threads", 4
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.exporter import SourceXMLHDF5ExportCommand
from java.io import File

cs.run(SourceXMLHDF5ExportCommand, True,
    ["sources", sources,
     "xml_file", File("/path/to/output.xml"),
     "entity_type", "Channel",
     "timepoint_begin", 0,
     "number_of_timepoints_to_export", 1,
     "block_size_x", 32,
     "block_size_y", 32,
     "block_size_z", 4,
     "scale_factor", 2,
     "threshold_mipmap", 16,
     "n_threads", 4]
).get()
```
::::

:::::

---

## Fuse BigStitcher Dataset To OME-TIFF

*Source: {biop-src}`BigStitcherDatasetToOMETIFFFuseCommand.java <ch/epfl/biop/command/exporter/BigStitcherDatasetToOMETIFFFuseCommand.java>`*

A specialized command for BigStitcher users: reads a BigStitcher XML dataset (with computed tile registrations), fuses the tiles, and writes the result as a pyramidal OME-TIFF. This is a one-step export that combines fusion and file writing.

| Parameter | Description |
|-----------|-------------|
| BigStitcher XML File | The BigStitcher `.xml` dataset file |
| Output Folder | Directory where the fused OME-TIFF will be saved |
| Fusion Method | Blending method for overlapping tiles |
| Use Interpolation | Apply interpolation during fusion (smoother but slower) |
| Resolution Levels | Number of pyramid levels (scale factor = 2) |
| Downsample X / Y / Z | Downsampling factor in each dimension (1.0 = no downsampling) |
| Selected Channels | Channels to export. Leave blank for all |
| Selected Timepoints | Timepoints to export. Leave blank for all |
| Selected Slices | Z-slices to export. Leave blank for all |
| Split Channels / Frames / Slices | Export each channel / timepoint / slice as a separate file |
| Use LZW Compression | Apply LZW compression to reduce file size |
| Override Z Anisotropy | Use a custom XY/Z ratio instead of the dataset value |
| XY/Z Anisotropy Ratio | Custom ratio between XY and Z pixel sizes (only used if override is checked) |

:::{tip}
To prepare a dataset for this command, first convert it with **Dataset - Make BigStitcher Compatible** (see [Opening Images](#dataset-operations)), then run tile registration in BigStitcher.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Export > Dataset - Fuse BigStitcher Dataset To OME-TIFF`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - Fuse BigStitcher Dataset To OME-TIFF");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.command.exporter.BigStitcherDatasetToOMETIFFFuseCommand

cs.run(BigStitcherDatasetToOMETIFFFuseCommand, true,
    "xml_bigstitcher_file", new java.io.File("/path/to/dataset.xml"),
    "output_path_directory", new java.io.File("/path/to/output/"),
    "fusion_method", "Linear Blending",
    "use_interpolation", true,
    "n_resolution_levels", 5,
    "x_downsample", 1.0,
    "y_downsample", 1.0,
    "z_downsample", 1.0,
    "range_channels", "",
    "range_frames", "",
    "range_slices", "",
    "split_channels", false,
    "split_frames", false,
    "split_slices", false,
    "use_lzw_compression", true,
    "override_z_ratio", false
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.command.exporter import BigStitcherDatasetToOMETIFFFuseCommand
from java.io import File

cs.run(BigStitcherDatasetToOMETIFFFuseCommand, True,
    ["xml_bigstitcher_file", File("/path/to/dataset.xml"),
     "output_path_directory", File("/path/to/output/"),
     "fusion_method", "Linear Blending",
     "use_interpolation", True,
     "n_resolution_levels", 5,
     "x_downsample", 1.0,
     "y_downsample", 1.0,
     "z_downsample", 1.0,
     "range_channels", "",
     "range_frames", "",
     "range_slices", "",
     "split_channels", False,
     "split_frames", False,
     "split_slices", False,
     "use_lzw_compression", True,
     "override_z_ratio", False]
).get()
```
::::

:::::

---

## BDV View Exports

These commands capture what you see in a BigDataViewer window — including the current orientation, zoom level, and visible sources — and export it as an ImagePlus or as new BDV sources. They are particularly useful for extracting oblique slices or quick snapshots.

### BDV - Export Current View As ImagePlus

*Source: {biop-src}`BdvViewToImagePlusExportCommand.java <ch/epfl/biop/command/display/bdv/export/BdvViewToImagePlusExportCommand.java>`*

Full-control export: you specify the output pixel size, region extent, and Z thickness. The exported ImagePlus is sampled at the current BDV view orientation.

| Parameter | Description |
|-----------|-------------|
| BDV Window | The BDV window to export from |
| Select Source(s) | Sources to include in the export |
| Capture Name | Name for the exported ImagePlus |
| Export Mode | **Normal** (in-memory) or **Virtual** (lazy-loading) |
| XY Pixel Size | Output pixel size in XY (world coordinate units) |
| Z Pixel Size | Output pixel size in Z (world coordinate units) |
| Size X / Y | Total width and height in world coordinate units |
| Half Thickness Z | Half-depth above and below the current plane (0 = single slice) |
| Match Window Size | When checked, uses the BDV window dimensions for X and Y |
| Selected Timepoints | Timepoints to export. Leave blank for all |
| Interpolate | Use interpolation when resampling |
| Parallel Channels / Timepoints / Slices | Acquire each dimension in parallel (Normal mode only) |
| Unit | Physical unit for the exported image calibration |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Display > BDV > Export > BDV - Export Current View As ImagePlus`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Export Current View As ImagePlus");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@bdv.util.BdvHandle bdv_h
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.display.bdv.export.BdvViewToImagePlusExportCommand

cs.run(BdvViewToImagePlusExportCommand, true,
    "bdv_h", bdv_h,
    "sources", sources,
    "capture_name", "capture",
    "export_mode", "Normal",
    "sampling_xy", 1.0,
    "sampling_z", 1.0,
    "size_x", 500.0,
    "size_y", 500.0,
    "size_z", 0.0,
    "interpolate", true,
    "selected_timepoints_str", "",
    "unit", "MICROMETER"
).get()
```
::::

::::{tab-item} Python
```python
#@bdv.util.BdvHandle bdv_h
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.display.bdv.export import BdvViewToImagePlusExportCommand

cs.run(BdvViewToImagePlusExportCommand, True,
    ["bdv_h", bdv_h,
     "sources", sources,
     "capture_name", "capture",
     "export_mode", "Normal",
     "sampling_xy", 1.0,
     "sampling_z", 1.0,
     "size_x", 500.0,
     "size_y", 500.0,
     "size_z", 0.0,
     "interpolate", True,
     "selected_timepoints_str", "",
     "unit", "MICROMETER"]
).get()
```
::::

:::::

### BDV - Export Current View As ImagePlus (Match Window)

*Source: {biop-src}`BdvViewToImagePlusBasicExportCommand.java <ch/epfl/biop/command/display/bdv/export/BdvViewToImagePlusBasicExportCommand.java>`*

A simplified version that automatically matches the BDV window dimensions for X and Y. You only need to specify the Z thickness and pixel size.

| Parameter | Description |
|-----------|-------------|
| BDV Window | The BDV window to export from |
| Capture Name | Name for the exported ImagePlus |
| Export Mode | **Normal** or **Virtual** |
| XY Pixel Size | Output pixel size in XY |
| Z Pixel Size | Output pixel size in Z |
| Half Thickness Z | Half-depth above and below current plane (0 = single slice) |
| Selected Timepoints | Timepoints to export. Leave blank for all |
| Interpolate | Use interpolation |
| Parallel Channels / Timepoints / Slices | Parallel acquisition (Normal mode only) |
| Unit | Physical unit |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Display > BDV > Export > BDV - Export Current View As ImagePlus (Match Window)`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Export Current View As ImagePlus (Match Window)");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@bdv.util.BdvHandle bdv_h
#@CommandService cs

import ch.epfl.biop.command.display.bdv.export.BdvViewToImagePlusBasicExportCommand

cs.run(BdvViewToImagePlusBasicExportCommand, true,
    "bdv_h", bdv_h,
    "capture_name", "capture",
    "export_mode", "Normal",
    "sampling_xy", 1.0,
    "sampling_z", 1.0,
    "z_size", 0.0,
    "interpolate", true,
    "selected_timepoints_str", "",
    "unit", "MICROMETER"
).get()
```
::::

::::{tab-item} Python
```python
#@bdv.util.BdvHandle bdv_h
#@CommandService cs

from ch.epfl.biop.command.display.bdv.export import BdvViewToImagePlusBasicExportCommand

cs.run(BdvViewToImagePlusBasicExportCommand, True,
    ["bdv_h", bdv_h,
     "capture_name", "capture",
     "export_mode", "Normal",
     "sampling_xy", 1.0,
     "sampling_z", 1.0,
     "z_size", 0.0,
     "interpolate", True,
     "selected_timepoints_str", "",
     "unit", "MICROMETER"]
).get()
```
::::

:::::

### BDV - Export Current View As Sources

*Source: {biop-src}`BdvViewToSourcesExportCommand.java <ch/epfl/biop/command/display/bdv/export/BdvViewToSourcesExportCommand.java>`*

Instead of producing an ImagePlus, this command creates new BDV sources resampled at the current view orientation. The result stays in the BDV workspace as a lazy source — useful for extracting an oblique reslice that you want to process further or export later.

| Parameter | Description |
|-----------|-------------|
| BDV Window | The BDV window whose view orientation defines the slice |
| Sources | The sources to reslice |
| XY Sampling | Pixel size in XY (world coordinate units) |
| Z Sampling | Pixel size in Z (world coordinate units) |
| Size X / Y | Width and height of the slice (world coordinate units) |
| Half Thickness Z | Half-depth above and below the current plane |
| Match Window Size | Use BDV window dimensions for X and Y |
| Interpolate | Use interpolation |
| Reuse MipMaps | Use existing pyramid levels for efficiency |
| Cache | Cache computed slices in memory |

:::{tip}
**Oblique reslicing workflow:** Navigate the BDV viewer to the exact orientation you want, then run **Export Current View As Sources**. The resulting sources are aligned to that oblique plane and can be visualized, processed, or exported to OME-TIFF like any other source.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BigDataViewer-Playground > Display > BDV > Export > BDV - Export Current View As Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Export Current View As Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@bdv.util.BdvHandle bdv_h
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.display.bdv.export.BdvViewToSourcesExportCommand

cs.run(BdvViewToSourcesExportCommand, true,
    "bdv_h", bdv_h,
    "sources", sources,
    "sampling_xy_in_physical_unit", 1.0,
    "sampling_z_in_physical_unit", 1.0,
    "x_size", 500.0,
    "y_size", 500.0,
    "z_size", 0.0,
    "match_window_size", true,
    "interpolate", true,
    "reuse_mipmaps", true,
    "cache", true
).get()
```
::::

::::{tab-item} Python
```python
#@bdv.util.BdvHandle bdv_h
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.display.bdv.export import BdvViewToSourcesExportCommand

cs.run(BdvViewToSourcesExportCommand, True,
    ["bdv_h", bdv_h,
     "sources", sources,
     "sampling_xy_in_physical_unit", 1.0,
     "sampling_z_in_physical_unit", 1.0,
     "x_size", 500.0,
     "y_size", 500.0,
     "z_size", 0.0,
     "match_window_size", True,
     "interpolate", True,
     "reuse_mipmaps", True,
     "cache", True]
).get()
```
::::

:::::

---

## Kheops: Standalone File Conversion

Kheops is a standalone file conversion tool that converts Bio-Formats–readable files directly to pyramidal OME-TIFF — without going through the BDV workspace. Use Kheops when you simply need to convert file formats (e.g. `.czi`, `.lif`, `.nd2` → `.ome.tiff`) without any processing.

### Kheops - Convert File to Pyramidal OME TIFF

*Source: {kheops-src}`KheopsCommand.java <ch/epfl/biop/kheops/command/KheopsCommand.java>`*

Converts a single file. Each series in the input becomes a separate OME-TIFF.

| Parameter | Description |
|-----------|-------------|
| Select an input file | The file to convert (any Bio-Formats–readable format) |
| Output folder | Where to save the OME-TIFF(s). If left empty, saves next to the input file |
| Compression type | Compression algorithm |
| Compress temporary files (LZW) | Compress temp files during pyramid building |
| Series subset | Which series to convert (leave blank for all) |
| Channels subset | Which channels to convert |
| Timepoints subset | Which timepoints to convert |
| Slices subset | Which Z-slices to convert |
| Split Channels / Timepoints / Slices | Export each as a separate file |
| Override voxel sizes | Use custom voxel sizes instead of file metadata |
| XY Voxel size in micrometer | Custom XY pixel size |
| Z Voxel size in micrometer | Custom Z pixel size |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BIOP > Kheops > Kheops - Convert File to Pyramidal OME TIFF`
::::

::::{tab-item} IJ Macro
```ijm
run("Kheops - Convert File to Pyramidal OME TIFF");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.kheops.command.KheopsCommand

cs.run(KheopsCommand, true,
    "input_path", new java.io.File("/path/to/input.czi"),
    "output_dir", new java.io.File("/path/to/output/"),
    "compression", "LZW",
    "compress_temp_files", false,
    "subset_series", "",
    "subset_channels", "",
    "subset_frames", "",
    "subset_slices", "",
    "split_channels", false,
    "split_frames", false,
    "split_slices", false,
    "override_voxel_size", false,
    "vox_size_xy", 1.0,
    "vox_size_z", 1.0
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.kheops.command import KheopsCommand
from java.io import File

cs.run(KheopsCommand, True,
    ["input_path", File("/path/to/input.czi"),
     "output_dir", File("/path/to/output/"),
     "compression", "LZW",
     "compress_temp_files", False,
     "subset_series", "",
     "subset_channels", "",
     "subset_frames", "",
     "subset_slices", "",
     "split_channels", False,
     "split_frames", False,
     "split_slices", False,
     "override_voxel_size", False,
     "vox_size_xy", 1.0,
     "vox_size_z", 1.0]
).get()
```
::::

:::::

### Kheops - Batch Convert Files to Pyramidal OME TIFF

*Source: {kheops-src}`KheopsBatchCommand.java <ch/epfl/biop/kheops/command/KheopsBatchCommand.java>`*

Converts multiple files in parallel. Same parameters as the single-file version, but accepts multiple input files.

| Parameter | Description |
|-----------|-------------|
| Select input files | The files to convert |
| Output folder | Where to save all OME-TIFFs |
| Compression type | Compression algorithm |
| Compress temporary files (LZW) | Compress temp files during pyramid building |
| Series / Channels / Timepoints / Slices subset | Subset selections (apply to all files) |
| Override voxel sizes | Use custom voxel sizes |
| XY / Z Voxel size in micrometer | Custom pixel sizes |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BIOP > Kheops > Kheops - Batch Convert Files to Pyramidal OME TIFF`
::::

::::{tab-item} IJ Macro
```ijm
run("Kheops - Batch Convert Files to Pyramidal OME TIFF");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.kheops.command.KheopsBatchCommand

cs.run(KheopsBatchCommand, true,
    "input_paths", [new java.io.File("/path/to/file1.czi"), new java.io.File("/path/to/file2.czi")] as java.io.File[],
    "output_dir", new java.io.File("/path/to/output/"),
    "compression", "LZW",
    "compress_temp_files", false,
    "subset_series", "",
    "subset_channels", "",
    "subset_frames", "",
    "subset_slices", "",
    "override_voxel_size", false,
    "vox_size_xy", 1.0,
    "vox_size_z", 1.0
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.kheops.command import KheopsBatchCommand
from java.io import File

cs.run(KheopsBatchCommand, True,
    ["input_paths", [File("/path/to/file1.czi"), File("/path/to/file2.czi")],
     "output_dir", File("/path/to/output/"),
     "compression", "LZW",
     "compress_temp_files", False,
     "subset_series", "",
     "subset_channels", "",
     "subset_frames", "",
     "subset_slices", "",
     "override_voxel_size", False,
     "vox_size_xy", 1.0,
     "vox_size_z", 1.0]
).get()
```
::::

:::::

### Kheops - Export ImagePlus To OME-TIFF

*Source: {kheops-src}`KheopsExportImagePlusCommand.java <ch/epfl/biop/kheops/command/KheopsExportImagePlusCommand.java>`*

Converts an already-open Fiji ImagePlus to pyramidal OME-TIFF. Useful when you have processed an image with classic Fiji tools and want to save it in a multi-resolution format.

| Parameter | Description |
|-----------|-------------|
| Image | The open ImagePlus to export |
| Output folder | Where to save the OME-TIFF |
| Compression type | Compression algorithm |
| Compress temporary files (LZW) | Compress temp files during pyramid building |
| Channels / Timepoints / Slices subset | Subset selections |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins > BIOP > Kheops > Kheops - Export ImagePlus To OME-TIFF`
::::

::::{tab-item} IJ Macro
```ijm
run("Kheops - Export ImagePlus To OME-TIFF");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@ij.ImagePlus image
#@CommandService cs

import ch.epfl.biop.kheops.command.KheopsExportImagePlusCommand

cs.run(KheopsExportImagePlusCommand, true,
    "image", image,
    "output_dir", new java.io.File("/path/to/output/"),
    "compression", "LZW",
    "compress_temp_files", false,
    "subset_channels", "",
    "subset_frames", "",
    "subset_slices", ""
).get()
```
::::

::::{tab-item} Python
```python
#@ij.ImagePlus image
#@CommandService cs

from ch.epfl.biop.kheops.command import KheopsExportImagePlusCommand
from java.io import File

cs.run(KheopsExportImagePlusCommand, True,
    ["image", image,
     "output_dir", File("/path/to/output/"),
     "compression", "LZW",
     "compress_temp_files", False,
     "subset_channels", "",
     "subset_frames", "",
     "subset_slices", ""]
).get()
```
::::

:::::

---

## Choosing an Export Path

| Goal | Command |
|------|---------|
| Save processed sources as a portable, shareable file | **Source - Export To OME-TIFF** |
| Save sources for re-opening in BigDataViewer / BigStitcher | **Source - Export To XML/HDF5 Dataset** |
| Fuse registered tiles from BigStitcher into a single file | **Dataset - Fuse BigStitcher Dataset To OME-TIFF** |
| Hand off sources to classic Fiji plugins (e.g. for measurement) | **Source - Export To ImagePlus** |
| Capture a quick snapshot or oblique slice from BDV | **BDV - Export Current View As ImagePlus** |
| Extract an oblique reslice for further BDV processing | **BDV - Export Current View As Sources** |
| Convert raw acquisition files to OME-TIFF (no processing) | **Kheops** commands |