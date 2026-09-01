# Installation

## Data

We will be using data from this repository: [doi.org/10.5281/zenodo.5675686](https://doi.org/10.5281/zenodo.5675686)

1. Download the file `warpy-demo-project.zip`
2. Unzip it to a location on your computer

## Software

### ImageJ/Fiji

Please follow the instructions found in [the bdv-playground installation instructions](../../installation/installation.md).

### QuPath

QuPath is required as well as the Warpy extension.

1. **Install QuPath 0.6+**
   - Download from [https://qupath.github.io/](https://qupath.github.io/)
   - Follow installation instructions for your operating system

2. **Install the Warpy extension via the BIOP catalog:**
   - Open QuPath
   - Go to `Extensions → Manage extensions`
   - Click `Manage extension catalogs`
   - Enter the catalog URL: `https://github.com/BIOP/qupath-biop-catalog`
   - Browse and install the Warpy extension

## Installation Check

:::{note}
Elastix and Transformix need no separate installation. On first use, Appose builds a
self-contained environment providing itk-elastix, on any operating system. This happens once
and takes a few minutes, so make sure you are online the first time you run a registration.
:::

### Test QuPath Project

1. Open QuPath
2. Drag and drop the `project.qpproj` file from `warpy-demo-project` into the main window
3. You will be asked to update the URLs of the images - please do this
4. Make sure you can view and browse the third/last image of the project
   - This indicates that Warpy is installed and working

## Next Steps

Once installation is complete, proceed to:
- **[Registration with GUI](registration-gui.md)** for the interactive workflow
- **[Automated Registration](registration-automated.md)** for batch processing
