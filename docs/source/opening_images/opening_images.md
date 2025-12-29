# Opening and Saving Images

BigDataViewer Playground provides multiple ways to open, import, and save images. This section covers all available methods for loading and storing image data.

:::{important}
There's a key distinction between **opening** and **visualizing** images in BigDataViewer Playground:

- **Opening**: Images are loaded into the hierarchical tree structure but not immediately displayed
- **Visualizing**: Images are displayed in BDV windows from the hierarchical tree using right-click contextual menus

All opened images appear in the BigDataViewer Playground window (accessible via `Plugins › BigDataViewer-Playground › Show Bdv Playground Window`).
:::

## Supported File Formats and Data Sources

BigDataViewer Playground supports a wide range of image formats and data sources:

### Bio-Formats Supported Files

Any file format supported by [Bio-Formats](https://bio-formats.readthedocs.io/en/latest/supported-formats.html) can be opened, including:

- Olympus/Evident `.vsi`
- Zeiss `.czi` (tick "Split RGB channels" for 16-bit RGB images)
- Pyramidal OME-TIFF `.ome.tif`
- Aperio `.svs`, `.afi`
- Imaris `.ims`
- Dicom `.dcm`, `.dicom`
- Hamamatsu `.ndpi`, `.ndpis`
- JPEG2000 `.jp2`
- Keller Lab Block `.klb`
- Vectra QPTIFF `.qptiff`
- Ventana BIF `.bif`

:::{note}
Leica `.lif` files have limited support as their multi-resolution data is not fully handled by Bio-Formats.
:::

### Multi-Resolution (Pyramidal) Files

For optimal performance with large images, pyramidal (multi-resolution) files are recommended. These contain pre-computed downsampled versions that enable efficient tiled loading.

:::{tip}
If your images aren't pyramidal, consider converting them to OME-TIFF format using:
- [Kheops](https://github.com/BIOP/ijp-kheops) Fiji plugin
- [NGFF converter by Glencoe](https://www.glencoesoftware.com/products/ngff-converter/) (choose OME-TIFF)
- Upload to OMERO database (pyramidal levels computed by server)
:::

### Calibrated Images

All images should be properly calibrated with physical units (microns, millimeters) rather than pixels. This ensures correct spatial relationships and processing.

### Additional Supported Sources

- **OMERO databases**: Stream images directly from OMERO servers
- **QuPath projects**: Import entire QuPath projects as BDV datasets
- **BigDataServer**: Remote image streaming
- **Imaris files**: Direct import of Imaris datasets
- **XML BDV datasets**: BigDataViewer's native XML format
- **N5 format**: Cloud-optimized data storage
- **OME-ZARR**: Next-generation OME-NGFF format (requires MoBiE update site)

---

## Methods for Opening Images

### 1. Open XML BDV Datasets

XML BDV datasets are the general format for BigDataViewer, containing metadata and references to image data stored in various backends.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Open XML BDV Datasets` (or type *open xml bdv* in Fiji's search bar)
- Drag & drop: XML files can be dragged directly into the BDV Playground window

**Features:**
- Contains positions, voxel size, channel descriptions, and backend specifications
- Supports multiple backends (HDF5, N5, Tiff, Remote, Imaris, Bio-Formats, OMERO, etc.)
- Generated for BigStitcher, BDV Playground, and other BDV plugins
- Backend type is defined within the XML file itself

:::{figure-md} xml-bdv-dataset
:class: placeholder

![Placeholder for XML BDV Dataset interface](https://via.placeholder.com/600x400?text=XML+BDV+Dataset+Interface)

Example of opening an XML BDV dataset in BigDataViewer Playground.
:::

#### Command Reference: Import Multiple Files

**Command**: `Import - Open multiple files`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.MultipleSpimDataImporterCommand`

Opens multiple image files at once. Supports various BDV-compatible formats including XML/HDF5, XML/N5, and OME-ZARR.

| Parameter | Type | Description |
|-----------|------|-------------|
| `files` | File[] | File(s) to import |

**Supported File Types:**
- **`.xml`** files: Looks for associated HDF5 or N5 data
- **`.zarr`** directories: OME-ZARR format
- **`.json`** files: BDV metadata files

:::{tip}
You can select multiple files at once by holding `Ctrl` (Windows/Linux) or `Cmd` (Mac) while clicking.
:::

---

### 2. Open Bio-Formats Files

Directly open Bio-Formats supported files as BDV datasets.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Open [BioFormats Bdv Bridge]` (alternatively type *bridge* in Fiji's search bar)
- Drag & drop: Bio-Formats supported files can be dragged directly into the BDV Playground window

**Features:**
- Supports multi-series, multi-resolution bio-formats API
- Can include multiple files in a single dataset
- Handles large whole-slide imaging (WSI) datasets

:::{figure-md} bioformats-bridge
:class: placeholder

![Placeholder for BioFormats Bridge interface](https://via.placeholder.com/600x400?text=BioFormats+Bridge+Interface)

BioFormats Bdv Bridge interface showing file selection.
:::

#### Command Reference: Create BDV Dataset (Bio-Formats)

**Command**: `BDVDataset › Open [BioFormats Bdv Bridge]`
**Class**: `ch.epfl.biop.bdv.img.bioformats.command.CreateBdvDatasetBioFormatsCommand`

Bridge between Bio-Formats and BigDataViewer. Creates a BDV dataset from a set of Bio-Formats supported files.

| Parameter | Type | Description |
|-----------|------|-------------|
| `files` | File[] | Dataset files |
| `datasetname` | String | Name of this dataset |
| `unit` | String | World coordinate units. Unit for the common coordinate system where all datasets will be positioned. Image calibrations will be converted to these units. |
| `plane_origin_convention` | String | Plane Origin Convention |
| `split_rgb_channels` | boolean | Split RGB channels (recommended for 16-bit RGB images) |
| `auto_pyramidize` | boolean | Compute image pyramid for large images without multiresolution (recommended) |
| `disable_memo` | boolean | Check to disable memoization (not recommended) |

**Output**: `AbstractSpimData spimdata`

#### Command Reference: Create BDV Dataset (Bio-Formats - Simple)

**Command**: `BDVDataset › Open [BioFormats Bdv Bridge] (simple)`
**Class**: `ch.epfl.biop.bdv.img.bioformats.command.CreateBdvDatasetBioFormatsSimpleCommand`

Simplified version of the Bio-Formats bridge with fewer options.

| Parameter | Type | Description |
|-----------|------|-------------|
| `file` | File | File to open |
| `datasetname` | String | Dataset name |

**Output**: `AbstractSpimData spimdata`

#### Command Reference: Show File in BDV (Bio-Formats)

**Command**: `BDVDataset › Show [BioFormats]`
**Class**: `ch.epfl.biop.bdv.img.bioformats.command.BdvShowFileBioFormatsCommand`

Support Bio-Formats multiresolution API. Set colors based on bioformats metadata. Do not attempt auto contrast. Directly show the images.

| Parameter | Type | Description |
|-----------|------|-------------|
| `file` | File | File to open |
| `position_convention` | String | Image metadata location |
| `splitrgbchannels` | boolean | Split RGB channels if you have 16 bits RGB images |
| `unit` | String | World coordinate units |

---

### 3. Open QuPath Projects

Import entire QuPath projects as BDV datasets.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Create BDV Dataset [QuPath]`

**Requirements:**
- QuPath project must use Bio-Formats or OMERO ICE image server
- Images should be calibrated (physical units, not pixels)

:::{warning}
Avoid adding or deleting images in QuPath after importing to BDV Playground, as this may cause inconsistencies.
:::

:::{figure-md} qupath-project
:class: placeholder

![Placeholder for QuPath project import](https://via.placeholder.com/600x400?text=QuPath+Project+Import)

Importing a QuPath project as a BDV dataset.
:::

#### Command Reference: Create BDV Dataset (QuPath)

**Command**: `BDVDataset › Create BDV Dataset [QuPath]`
**Class**: `ch.epfl.biop.bdv.img.qupath.command.CreateBdvDatasetQuPathCommand`

Create a BDV dataset from a QuPath json project file. The image servers supported are Bio-Formats and OMERO image servers with the ICE API.

| Parameter | Type | Description |
|-----------|------|-------------|
| `qupath_project` | File | QuPath project file (.json) |
| `datasetname` | String | Dataset name (leave empty to name it like the QuPath project) |
| `unit` | String | World coordinate units |
| `plane_origin_convention` | String | Plane Origin Convention |
| `split_rgb_channels` | boolean | Split RGB channels |

**Output**: `AbstractSpimData spimData`

---

### 4. Open OMERO Images

Stream images directly from OMERO databases.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Create BDV Dataset [OMERO]`

**Requirements:**
- The OMERO 5.5-5.6 Fiji's update site should be enabled

:::{figure-md} omero-import
:class: placeholder

![Placeholder for OMERO import interface](https://via.placeholder.com/600x400?text=OMERO+Import+Interface)

OMERO dataset creation interface with credential prompt.
:::

#### Command Reference: Connect to OMERO

**Command**: `OMERO › Connect to OMERO`
**Class**: `ch.epfl.biop.bdv.img.omero.command.OmeroConnectCommand`

Connect to an OMERO server.

| Parameter | Type | Description |
|-----------|------|-------------|
| `host` | String | OMERO host |
| `port` | int | OMERO Ice port |
| `username` | String | Enter your username |
| `password` | String | Enter your password |

**Output**:
- `IOMEROSession omeroSession`
- `Boolean success`
- `Exception error` (if connection fails)

#### Command Reference: Create BDV Dataset (OMERO)

**Command**: `BDVDataset › Create BDV Dataset [OMERO]`
**Class**: `ch.epfl.biop.bdv.img.omero.command.CreateBdvDatasetOMEROCommand`

Bridge between OMERO and BigDataViewer. Creates a BDV dataset from a set of OMERO URLs.

| Parameter | Type | Description |
|-----------|------|-------------|
| `omero_urls` | String | OMERO URLs, comma separated |
| `datasetname` | String | Name of this dataset |
| `unit` | String | World coordinate units |
| `plane_origin_convention` | String | Plane Origin Convention |

**Output**: `AbstractSpimData spimdata`

:::{tip}
OMERO URLs typically follow the format: `omero://server:port/image/123` where `123` is the image ID.
:::

#### Command Reference: Disconnect from OMERO

**Command**: `OMERO › Disconnect from OMERO`
**Class**: `ch.epfl.biop.bdv.img.omero.command.OmeroDisconnectCommand`

Disconnect from an OMERO server.

| Parameter | Type | Description |
|-----------|------|-------------|
| `host` | String | OMERO host |

**Output**:
- `Boolean success`
- `Exception error` (if disconnection fails)

---

### 5. Import Current ImageJ Image

Convert the currently open ImageJ image to a BDV dataset.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › Sources › Import › Make BDVDataset from current IJ1 image`

**Features:**
- Wraps ImageJ data
- Can potentially be saved as XML BDV dataset, as long as the original image was loaded from a file.
- Preserves image metadata

#### Command Reference: ImagePlus to BDV Dataset

**Command**: `Sources › Import › Make BDVDataset from current IJ1 image`
**Class**: `ch.epfl.biop.bdv.img.imageplus.command.ImagePlusToBdvDatasetCommand`

Opens the current ImagePlus as a BDV Dataset.

| Parameter | Type | Description |
|-----------|------|-------------|
| `image` | ImagePlus | The ImagePlus to convert (current image if run from menu) |
| `datasetname` | String | Dataset name (leave empty to name it like the ImagePlus title) |

**Output**: `AbstractSpimData spimdata`

---

### 6. Import from BigDataServer

Stream large datasets remotely without downloading them locally.

**How to open:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Open from BigDataServer`

#### Command Reference: Open from BigDataServer

**Command**: `Import - Open from BigDataServer`
**Class**: `sc.fiji.bdvpg.scijava.command.spimdata.SpimdataBigDataServerImportCommand`

Opens a dataset from a remote BigDataServer. This allows streaming large datasets without downloading them locally.

| Parameter | Type | Description |
|-----------|------|-------------|
| `urlserver` | String | URL of the BigDataServer |
| `datasetname` | String | Name of the dataset to open |

**BigDataServer URL Format:**
```
http://server-address:port
```

:::{note}
BigDataServer streams data on-demand. Only the visible portions are downloaded, making it efficient for large datasets.
:::

---

## Advanced Opening Options

### Batch Import

Multiple files can be included in a single BDV dataset, creating a hierarchical organization.

### Drag and Drop

XML BDV datasets and Bio-Formats supported files can be dragged and dropped directly into the BDV Playground window for quick loading.

### Mixed Source Types

Different source types (Bio-Formats, OMERO, QuPath) can be combined in the same BDV Playground session.

---

## Technical Details

### BigDataViewer Dataset Backends

BDV datasets use different backends implementing the Java `ImageLoader` interface:

- **BigDataViewer Core**: XML/HDF5, Catmaid, Imaris, OpenConnectome, N5, BigDataServer
- **BIOP Image Loaders**: Bio-Formats, OMERO, QuPath projects (meta-loader)
- **MoBiE**: OME-ZARR format

### Hierarchical Tree Structure

All opened images appear in a hierarchical tree within the BDV Playground window:

- Right-click on sources to visualize them
- Organize sources into groups
- Manage source visibility and properties

:::{figure-md} bdv-tree-structure
:class: placeholder

![Placeholder for BDV tree structure](https://via.placeholder.com/400x600?text=BDV+Tree+Structure)

Hierarchical tree structure showing organized image sources.
:::

### Import Formats Overview

| Format | Description |
|--------|-------------|
| **XML/HDF5** | Native BDV format, pyramidal, chunked |
| **XML/N5** | N5 backend for BDV |
| **OME-ZARR** | Cloud-ready, S3-compatible format |
| **BigDataServer** | Remote streaming from BDV server |
| **Bio-Formats** | All Bio-Formats supported formats |
| **OMERO** | OMERO server images via ICE API |

---

## Saving BDV Datasets

Any BDV dataset created using the opening methods above can be saved as an XML file for later reuse. This allows you to preserve your dataset configuration and quickly reload it without re-importing all sources.

### How to Save BDV Datasets

**Method:**
- Menu: `Plugins › BigDataViewer-Playground › BDVDataset › Save BDVDataset`
- Select the sources you want to save (they should be stemming from a single import step - for instance if you want 2 bio-formats file inside a single dataset, you need to open them in a single step).
- Specify an XML file path for saving

**Features:**
- **Metadata-only storage**: Only dataset configuration and spatial calibration is saved, not image pixel data
- **Source preservation**: Maintains all source information and hierarchy
- **Quick reload**: Can be reopened using the "Open XML BDV Datasets" method
- **Backend agnostic**: Works with any backend type (Bio-Formats, OMERO, QuPath, etc.)

:::{important}
Saved XML files contain only metadata and source references, not the actual image data. The original image files must remain accessible at their original locations for the saved dataset to work properly.
:::

#### Command Reference: Export SpimData Metadata

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

## Exporting to Other Formats

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

## Troubleshooting

### Common Import Issues

| Problem | Solution |
|---------|----------|
| "File not found" | Check that both XML and data files exist |
| Slow loading | Data may be on network storage - consider copying locally |
| Memory errors | Dataset may be too large - check available RAM |
| Performance issues with large images | Use pyramidal/multi-resolution files |
| Calibration problems | Verify pixel size is set correctly; check units are physical (not pixels) |
| Zeiss CZI issues | Use the Zeiss Quick Start Loader or tick "Split RGB channels" |

### Common Export Issues

| Problem | Solution |
|---------|----------|
| "Disk full" | HDF5 files can be large - ensure sufficient space |
| Export hangs | Reduce `nthreads` if system becomes unresponsive |
| Corrupted output | Ensure export completes - don't interrupt |

### Import Performance Tips

- **Local SSD**: Fastest for XML/HDF5
- **Network storage**: Consider BigDataServer for remote access
- **Large datasets**: Use lazy loading (data loaded on-demand)

### Export Performance Tips

| Parameter | Impact |
|-----------|--------|
| `nthreads` | More threads = faster export (up to CPU cores) |
| `blocksizez` | Larger Z blocks improve sequential write speed |
| Compression | HDF5 uses GZIP by default - good balance |

---

## Best Practices

1. **Use pyramidal files** for large images to improve performance
2. **Calibrate all images** with physical units before importing
3. **Combine similar images** in batch imports
4. **Use appropriate backends** for your data source type
5. **Save your datasets** as XML files for quick reloading
6. **For remote data**, only export the final result to avoid unnecessary data transfer

---

## Command Reference Summary

### Import Commands

| Command | Class | Purpose |
|---------|-------|---------|
| Open multiple files | `MultipleSpimDataImporterCommand` | Import multiple XML/HDF5/N5/ZARR files |
| Open from BigDataServer | `SpimdataBigDataServerImportCommand` | Stream from BigDataServer |
| Open [BioFormats Bdv Bridge] | `CreateBdvDatasetBioFormatsCommand` | Import Bio-Formats files |
| Open [BioFormats Bdv Bridge] (simple) | `CreateBdvDatasetBioFormatsSimpleCommand` | Simplified Bio-Formats import |
| Show [BioFormats] | `BdvShowFileBioFormatsCommand` | Show Bio-Formats file directly |
| Create BDV Dataset [QuPath] | `CreateBdvDatasetQuPathCommand` | Import QuPath project |
| Connect to OMERO | `OmeroConnectCommand` | Connect to OMERO server |
| Create BDV Dataset [OMERO] | `CreateBdvDatasetOMEROCommand` | Import OMERO images |
| Disconnect from OMERO | `OmeroDisconnectCommand` | Disconnect from OMERO |
| Make BDVDataset from IJ1 image | `ImagePlusToBdvDatasetCommand` | Convert current ImagePlus |

### Export Commands

| Command | Class | Purpose |
|---------|-------|---------|
| Save SpimData | `SpimDataExporterCommand` | Export metadata as XML |
| Save as XML/HDF5 | `XmlHDF5ExporterCommand` | Export to XML/HDF5 format |
