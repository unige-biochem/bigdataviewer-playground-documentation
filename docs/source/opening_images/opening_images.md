# Opening Images

This guide covers how to get your image data into BigDataViewer Playground.

## What Is a Dataset?

When you open images in BigDataViewer Playground, they become a **dataset**. Understanding what a dataset is will help you work with every other feature.

A dataset is a unified representation of your images that holds two things:

1. **A recipe to read the raw data** — the dataset doesn't copy your pixels. It stores a reference to the original source (a file on disk, an OMERO server, a QuPath project, etc.) and reads data on demand.
2. **Spatial metadata** — position, orientation, and calibration of each image, stored as a chain of 3D affine transforms. Each channel and timepoint can have its own chain of transforms.

This design means you can open terabyte-scale images instantly — no data is loaded until you actually look at it or export it. And when you register, drift-correct, or transform your data, those operations simply add transforms to the chain rather than rewriting pixels.

### Saving and Reloading Datasets

Datasets can be **saved to an XML file** and reloaded later. The XML file stores:

- Which backend to use (Bio-Formats, OMERO, etc.) and how to reach the raw data
- The full chain of affine transforms for each channel and timepoint
- Display settings

This means you can set up a complex multi-image, multi-channel dataset, save it, and pick up exactly where you left off — or share it with a collaborator who has access to the same raw files.

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Dataset - Save XML Dataset`

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Dataset --> Open XML Dataset`

---

## Creating a Dataset

All dataset creation commands are found under:

{menuselection}`Plugins --> BigDataViewer-Playground --> Import`

Each command creates a dataset from a different source. The most common starting point is **Bio-Formats**, which handles the widest range of file formats.

### Dataset - Create [Bio-Formats]

The general-purpose importer. Supports any file format that Bio-Formats can read (CZI, LIF, ND2, OME-TIFF, and [many more](https://bio-formats.readthedocs.io/en/latest/supported-formats.html)).

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [Bio-Formats]`

| Parameter | Description |
|-----------|-------------|
| Input Files | One or more image files to include in the dataset |
| Dataset Name | Name for the resulting dataset |
| Plane Origin Convention | Where the image origin is located |
| World coordinate units | Unit for the coordinate system (e.g. MICROMETER) |
| Split RGB Channels | Separate RGB into individual channels |
| Auto-Pyramidize | Generate multi-resolution levels for large images that lack them natively |
| Disable Memoization | Turn off Bio-Formats caching (not recommended for large files) |

:::{tip}
**Working with CZI files?** Enable the **Quick Start CZI Reader** update site for significantly faster loading. See the [Installation Guide](../installation/installation.md#fast-czi-file-reading).
:::

### Dataset - Create [Current ImagePlus]

Wraps an image that is already open in Fiji as a dataset, so you can use it with BigDataViewer Playground tools.

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [Current ImagePlus]`

| Parameter | Description |
|-----------|-------------|
| Input Image | The ImagePlus window to convert |
| Dataset Name | Name for the dataset (leave empty to use the image title) |

### Dataset - Create [OMERO]

Creates a dataset from images stored on an OMERO server. You must connect to the server first using `Plugins > BIOP > OMERO > Omero - Connect`.

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [OMERO]`

| Parameter | Description |
|-----------|-------------|
| OMERO URLs | Comma-separated list of OMERO image URLs |
| Dataset Name | Name for the resulting dataset |
| Plane Origin Convention | Where the image origin is located |
| World coordinate units | Unit for the coordinate system |

### Dataset - Create [QuPath]

Imports all images from a QuPath project as a single dataset.


{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [QuPath]`

| Parameter | Description |
|-----------|-------------|
| QuPath Project | The QuPath project file (`.qpproj`) |
| Dataset Name | Name for the dataset (leave empty to use the project folder name) |
| Plane Origin Convention | Where the image origin is located |
| World coordinate units | Unit for the coordinate system |
| Split RGB Channels | Separate RGB into individual channels |

### Dataset - Create [Operetta]

Opens PerkinElmer Operetta high-content imaging datasets.

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [Operetta]`

| Parameter | Description |
|-----------|-------------|
| Operetta Images Folder | The `Images` or `flex` folder from your Operetta dataset |
| World coordinate units | Unit for the coordinate system |
| Min/Max Display Value | Initial display range |
| Show in Viewer | Immediately display in a BigDataViewer window |

### Dataset - Create [CZI LLS7]

Specialized importer for Zeiss Lattice Light Sheet 7 data. Automatically applies the correct skew transformation so the data displays with proper 3D geometry.

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Create [CZI LLS7]`

| Parameter | Description |
|-----------|-------------|
| CZI LLS7 File | The `.czi` file from an LLS7 acquisition |
| Use Legacy XY Mode | For compatibility with older datasets |

See the [LLS7 Timelapse workflow](../workflows/lls7_timelapse.md) for a complete processing guide.

### Dataset - Samples

Opens a sample dataset for testing and exploration. Downloads and caches on first use.

{menuselection}`Plugins --> BigDataViewer-Playground --> Import --> Dataset - Samples`

---

## Dataset Operations

Once you have datasets, several commands help you manipulate them at the dataset level.

### Combine XML Datasets

Merges multiple saved XML datasets into one, either as additional timepoints or additional channels.

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Dataset - Combine XML Datasets`

| Parameter | Description |
|-----------|-------------|
| Input XML Files | The XML files to combine (order matters) |
| Dataset Name | Name for the merged dataset |
| Combine Mode | Combine as separate timepoints or separate channels |
| Filter Setup IDs | Optional: include only specific setups (e.g. `0:5,10`) |

### View and Edit Transforms

The transform chain attached to each source can be inspected and modified:

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - View Transforms`

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Add Transforms`

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Remove Transforms`

{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Set Transforms`

These commands let you view, append, remove, or overwrite affine transforms at specific timepoints and positions in the chain. This is useful for manual corrections or advanced registration workflows.

### Other Dataset Commands

| Command | Purpose |
|---------|---------|
| Dataset - Remove Entities | Strip entity types for compatibility with other tools |
| Dataset - Make BigStitcher Compatible | Convert a dataset to BigStitcher format |