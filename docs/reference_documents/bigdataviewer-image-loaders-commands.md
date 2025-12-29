# ch.epfl.biop.bdv.img.FixFilePathsCommand
Description: Allows fixing invalid file paths in a BDV dataset by providing replacement paths.
## Input
File[] fixedFilePaths; // Replacement Files
The replacement files in the same order as the invalid files.
File[] invalidFilePaths; // Invalid Files
The files with invalid paths that need to be fixed.
String message; //
## Output
File[] fixedFilePaths; // Replacement Files
The replacement files in the same order as the invalid files.
File[] invalidFilePaths; // Invalid Files
The files with invalid paths that need to be fixed.


# ch.epfl.biop.bdv.img.bioformats.command.BdvShowFileBioFormatsCommand
Description: Opens a file in BigDataViewer using Bio-Formats, with colors from metadata.
## Input
File file; // Input File
The image file to open in BigDataViewer.
String position_convention; // Plane Origin Convention
Defines where the image origin is located.
boolean splitrgbchannels; // Split RGB Channels
When checked, splits RGB images into separate channels (recommended for 16-bit RGB).
String unit; // World coordinate units
Unit for the coordinate system where images will be positioned.
## Output


# ch.epfl.biop.bdv.img.bioformats.command.CreateBdvDatasetBioFormatsCommand
Description: Creates a BDV dataset from one or more Bio-Formats compatible files.
## Input
boolean auto_pyramidize; // Auto-Pyramidize
Generates multi-resolution pyramids for large images without native multiresolution.
Context ctx; //
String datasetname; // Dataset Name
Name for the resulting BDV dataset.
boolean disable_memo; // Disable Memoization
Disables Bio-Formats file caching (not recommended for large files).
File[] files; // Input Files
The image files to include in the dataset.
String plane_origin_convention; // Plane Origin Convention
Defines where the image origin is located.
boolean split_rgb_channels; // Split RGB Channels
When checked, splits RGB images into separate channels.
String unit; // World coordinate units
Unit for the coordinate system where images will be positioned.
## Output
AbstractSpimData spimdata; // BDV Dataset
The resulting BDV dataset.


# ch.epfl.biop.bdv.img.bioformats.command.CreateBdvDatasetBioFormatsSimpleCommand
Description: Creates a BDV dataset from a single Bio-Formats compatible file.
## Input
Context ctx; //
String datasetname; // Dataset Name
Automatically generated from the file name.
File file; // Input File
The image file to open.
## Output
AbstractSpimData spimdata; // BDV Dataset
The resulting BDV dataset.


# ch.epfl.biop.bdv.img.bioformats.command.OpenSampleCommand
Label: Open sample datasets
Description: Opens a sample dataset from a selection of test images (downloads and caches on first use).
## Input
String datasetname; // Sample Dataset
The sample dataset to download and open.
## Output
AbstractSpimData spimData; // BDV Dataset
The resulting BDV dataset.


# ch.epfl.biop.bdv.img.imageplus.command.ImagePlusToBdvDatasetCommand
Description: Creates a BDV dataset from the current ImagePlus window.
## Input
String datasetname; // Dataset Name
Name for the dataset (leave empty to use the image title).
ImagePlus image; // Input Image
The ImagePlus image to convert to a BDV dataset.
## Output
AbstractSpimData spimdata; // BDV Dataset
The resulting BDV dataset.


# ch.epfl.biop.bdv.img.omero.command.CreateBdvDatasetOMEROCommand
Description: Creates a BDV dataset from one or more OMERO image URLs.
## Input
Context context; //
String datasetname; // Dataset Name
Name for the resulting BDV dataset.
String omero_urls; // OMERO URLs
Comma-separated list of OMERO image URLs to include in the dataset.
String plane_origin_convention; // Plane Origin Convention
Defines where the image origin is located.
String unit; // World coordinate units
Unit for the coordinate system where images will be positioned.
## Output
AbstractSpimData spimdata; // BDV Dataset
The resulting BDV dataset.


# ch.epfl.biop.bdv.img.omero.command.OmeroConnectCommand
Description: Connects to an OMERO server using your credentials.
## Input
Context ctx; //
String host; // OMERO Host
The hostname or IP address of the OMERO server.
String message; //
OMEROService omeroService; //
String password; // Password
Your OMERO password.
int port; // Port
The OMERO Ice port (default is 4064).
String username; // Username
Your OMERO username.
## Output
Exception error; // Error
The exception if connection failed, null otherwise.
IOMEROSession omeroSession; // OMERO Session
The active OMERO session if connection succeeds.
Boolean success; // Success
True if the connection was successful.


# ch.epfl.biop.bdv.img.omero.command.OmeroDisconnectCommand
Description: Disconnects from an OMERO server and closes all sessions.
## Input
String host; // OMERO Host
The hostname of the OMERO server to disconnect from.
OMEROService omeroService; //
## Output
Exception error; // Error
The exception if disconnection failed, null otherwise.
Boolean success; // Success
True if the disconnection was successful.


# ch.epfl.biop.bdv.img.qupath.command.CreateBdvDatasetQuPathCommand
Description: Creates a BDV dataset from all images in a QuPath project.
## Input
Context context; //
String datasetname; // Dataset Name
Name for the dataset (leave empty to use the project folder name).
String plane_origin_convention; // Plane Origin Convention
Defines where the image origin is located.
File qupath_project; // QuPath Project
The QuPath project file (project.qpproj) to import.
boolean split_rgb_channels; // Split RGB Channels
When checked, splits RGB images into separate channels.
String unit; // World coordinate units
Unit for the coordinate system where images will be positioned.
## Output
AbstractSpimData spimData; // BDV Dataset
The resulting BDV dataset.

