
# sc.fiji.bdvpg.scijava.command.CacheOptionsCommand
Description: Sets Bdv Playground cache options (needs a restart)
## Input
Button button; // Reset to default
String cache_type; // Cache type
int log_ms; // Log cache (ms between log), negative to avoid logging
int mem_for_cache_mb; // Rule: set a size for cache (Mb)
int mem_for_everything_else_mb; // Rule: set a size for the rest of the application (Mb)
int mem_ratio_pc; // Rule: use a ratio of all memory available (%)
PrefService prefs; //
## Output


# sc.fiji.bdvpg.scijava.command.ClearSourceAndConverterService
## Input
SourceAndConverterService sac_service; //
## Output


# sc.fiji.bdvpg.scijava.command.LoadSourceAndConverterServiceState
## Input
Context ctx; //
Boolean erasepreviousstate; // Erase current state
File file; // Open state file (json)
## Output


# sc.fiji.bdvpg.scijava.command.RenameBdv
## Input
BdvHandle bdvh; //
String title; // New Title
## Output


# sc.fiji.bdvpg.scijava.command.SaveSourceAndConverterServiceState
## Input
Context ctx; //
File file; // Save state file (json)
## Output


# sc.fiji.bdvpg.scijava.command.ShowSourceAndConverterServiceWindow
## Input
SourceAndConverterService sacs; //
## Output


# sc.fiji.bdvpg.scijava.command.TestInteractiveCommand
## Input
String a_string; //
## Output


# sc.fiji.bdvpg.scijava.command.TestWidgetDemoCommand
## Input
SourceAndConverter[] non_sorted_sources; //
SourceAndConverter[] sorted_sources; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvCreatorCommand
Description: Creates an empty BDV window
## Input
SourceAndConverterBdvDisplayService sacDisplayService; //
## Output
BdvHandle bdvh; //


# sc.fiji.bdvpg.scijava.command.bdv.BdvDebugOverlayAdderCommand
Description: Adds the overlay of the bdv tiled renderer
## Input
BdvHandle bdvh; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvDefaultViewerSetterCommand
Description: Set preferences of Bdv Window
## Input
String frametitle; //
int height; //
boolean interpolate; //
boolean is2d; //
int numrenderingthreads; //
int numsourcegroups; //
int numtimepoints; //
boolean resetToDefault; // Click this checkbox to ignore all parameters and reset the default viewer
SourceAndConverterBdvDisplayService sacDisplayService; //
String screenscales; //
long targetrenderms; //
int width; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvOrthoCreatorCommand
Description: Creates 3 BDV windows with synchronized orthogonal views
## Input
boolean drawcrosses; // Add cross overlay to show view plane locations
boolean interpolate; // Interpolate
int locationx; // X Front Window location
int locationy; // Y Front Window location
int ntimepoints; // Number of timepoints (1 for a single timepoint)
SourceAndConverterBdvDisplayService sacDisplayService; //
int screen; // Display (0 if you have one screen)
int sizex; // Window Width
int sizey; // Window Height
boolean synchronize_sources; //
## Output
BdvHandle bdvhx; //
BdvHandle bdvhy; //
BdvHandle bdvhz; //


# sc.fiji.bdvpg.scijava.command.bdv.BdvSelectCommand
Description: Select a BDV Windows
## Input
BdvHandle bdvh; // Select BDV Window
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvSettingsCommand
Description: Sets actions linked to key / mouse event in BDV
## Input
Context context; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesAdderCommand
Description: Adds one or several sources to an existing BDV window
## Input
boolean adjustviewonsource; // Adjust View on Source
boolean autocontrast; // Auto Contrast
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle bdvh; // Select BDV Window
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesRemoverCommand
Description: Removes one or several sources from an existing BDV window
## Input
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle bdvh; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvSourcesShowCommand
Description: Displays one or several sources into a new BDV window
## Input
boolean adjustviewonsource; // Adjust View on Source
boolean autocontrast; // Auto Contrast
SourceAndConverterBdvDisplayService bdvDisplayService; //
boolean interpolate; // Interpolate
SourceAndConverter[] sacs; // Select Source(s)
## Output
BdvHandle bdvh; //


# sc.fiji.bdvpg.scijava.command.bdv.BdvTitleSetterCommand
Description: Sets the title of a BDV Windows
## Input
BdvHandle bdvh; // Select BDV Window
String title; // title
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvViewAdjustOnSourcesCommand
Description: Adjust current Bdv view on the selected sources
## Input
BdvHandle bdvh; // Select BDV Window
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvViewLoggerCommand
Description: Outputs the current view transform of a BDV window into the standard IJ logger
## Input
BdvHandle bdvh; //
LogService ls; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.BdvViewTransformatorCommand
Description: Applies a simple view transform (translation / rotation) to a BDV window
## Input
BdvHandle bdvh; // Select BDV Windows
Double rotatearoundx; // Rotate around X
Double rotatearoundy; // Rotate around Y
Double rotatearoundz; // Rotate around Z
Double translatex; // Translate in X
Double translatey; // Translate in Y
Double translatez; // Translate in Z
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvCloseCommand
Description: Closes one or several bdv windows.
## Input
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle[] bdvhs; // Select BDV Windows
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvCrossAdderCommand
Description: Adds a centering cross onto BDV windows
## Input
BdvHandle[] bdvhs; // Select BDV Windows
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourceNameOverlayAdderCommand
Description: Adds a source name overlay onto BDV windows
## Input
BdvHandle[] bdvhs; // Select BDV Windows
int fontSize; // Font Size
String fontString; //
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourceNavigatorSliderAdderCommand
Description: Adds a source slider onto BDV windows
## Input
BdvHandle[] bdvhs; // Select BDV Windows
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourcesAdderCommand
Description: Adds one or several sources into several existing BDV windows
## Input
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle[] bdvhs; // Select BDV Windows
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvSourcesRemoverCommand
Description: Removes one or several sources from several existing BDV windows
## Input
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle[] bdvhs; // Select BDV Windows
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvTimepointAdapterCommand
Description: Adapts the bdv windows timepoints to the number of timepoints present in their sources.
## Input
SourceAndConverterBdvDisplayService bdvDisplayService; //
BdvHandle[] bdvhs; // Select BDV Windows
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvTimepointsSetterCommand
Description: Sets the number of timepoints in one or several BDV Windows
## Input
BdvHandle[] bdvhs; // Select BDV Windows
int numberoftimepoints; // Number of timepoints, min = 1
## Output


# sc.fiji.bdvpg.scijava.command.bdv.MultiBdvZSliderAdderCommand
Description: Adds a z slider onto BDV windows
## Input
BdvHandle[] bdvhs; // Select BDV Windows
## Output


# sc.fiji.bdvpg.scijava.command.bvv.BvvOrthoWindowCreatorCommand
Description: Creates 3 BVV windows with synchronized orthogonal views
## Input
boolean interpolate; // Interpolate
int locationx; // X Front Window location
int locationy; // Y Front Window location
int ntimepoints; // Number of timepoints (1 for a single timepoint)
int screen; // Display (0 if you have one screen)
int sizex; // Window Width
int sizey; // Window Height
boolean synchronize_sources; //
## Output
BvvHandle bvvhx; //
BvvHandle bvvhy; //
BvvHandle bvvhz; //


# sc.fiji.bdvpg.scijava.command.bvv.BvvSetTimepointsNumberCommand
Description: Sets the number of timepoints in one or several BVV Windows
## Input
BvvHandle[] bvvhs; // Select BVV Windows
int numberoftimepoints; // Number of timepoints, min = 1
## Output


# sc.fiji.bdvpg.scijava.command.bvv.BvvSourcesAdderCommand
Description: Show sources in a BigVolumeViewer window - limited to 16 bit images
## Input
boolean adjustviewonsource; // Adjust View on Source
BvvHandle bvvh; // Select BVV Window(s)
SourceAndConverter[] sacs; // Select source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bvv.BvvSourcesRemoverCommand
Description: Removes one or several sources from an existing BVV window
## Input
BvvHandle bvvh; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.bvv.BvvWindowCreatorCommand
Description: Creates an empty Bvv window
## Input
String windowtitle; // Title of the new BVV window
## Output
BvvHandle bvvh; //


# sc.fiji.bdvpg.scijava.command.source.AddMetadataCommand
Description: Adds a metadata string to selected sources
## Input
String key; // Key
SourceAndConverterService sac_service; //
SourceAndConverter[] sacs; // Select Source(s)
String value; // Value
## Output


# sc.fiji.bdvpg.scijava.command.source.BasicTransformerCommand
Description: Performs basic transformation (rotate / flip) along X Y Z axis for several sources. If global is selected, the transformation is performed relative to the global origin (0,0,0). If global is not selected, the center of each source is unchanged.
## Input
String axis; //
SourceAndConverterBdvDisplayService bdvDisplayService; //
boolean globalchange; // Global transform (relative to the origin of the world)
int initimepoint; // Initial timepoint (0 based)
int ntimepoints; // Number of timepoints (min 1)
SourceAndConverter[] sacs; // Select source(s)
String type; //
## Output


# sc.fiji.bdvpg.scijava.command.source.BigWarpLauncherCommand
Description: Starts BigWarp from existing sources
## Input
String bigwarpname; // Window title for BigWarp
SourceAndConverterBdvDisplayService bsds; //
SourceAndConverter[] fixedsources; // Fixed Source(s)
SourceAndConverter[] movingsources; // Moving Source(s)
SourceAndConverterService sac_service; //
## Output
BdvHandle bdvhp; //
BdvHandle bdvhq; //
SourceAndConverter gridsource; //
SourceAndConverter[] warpedsources; //
SourceAndConverter warpmagnitudesource; //


# sc.fiji.bdvpg.scijava.command.source.BrightnessAdjusterCommand
## Input
double max; //
double min; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.ColorSourceCreatorCommand
Description: Duplicate one or several sources and sets a new color for these sources
## Input
ColorRGB color; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.InteractiveBrightnessAdjusterCommand
## Input
String customsourcelabel; // Sources :
Label the sources controlled by this window
double max; //
double maxslider; // relative Maximum
String message; //
double min; //
double minslider; // relative Minimum
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.LUTSourceCreatorCommand
Description: Duplicate one or several sources and sets an (identical) Look Up Table for these duplicated sources
## Input
String choice; // LUT name
ConvertService cs; //
LUTService lutservice; //
SourceAndConverter[] sacs; // Select Source(s)
ColorTable table; // LUT
## Output
SourceAndConverter[] sacs_out; //


# sc.fiji.bdvpg.scijava.command.source.MakeGroupCommand
Description: Adds a node in the tree view which selects the sources specified in the command
## Input
boolean displaysources; // Display Sources
String groupname; // Name of the group
SourceAndConverterService sac_service; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.MakeMetadataFilterNodeCommand
Description: Adds a node in the tree view which selects the sources which contain a certain key metadata and which matches a certain regular expression
## Input
String groupname; // Name of the node
String key; // Select Metadata Key
SourceAndConverterService sac_service; //
String valueregex; // Regular expression for Metadata Value (".*" matches everything)
## Output


# sc.fiji.bdvpg.scijava.command.source.ManualTransformCommand
Description: Manual transformation of selected sources. Works only with a single bdv window (the active one).The sources that are not displayed but selected are transformed. During the registration, the user isplaced in the reference of the moving sources. That's why they are not moving during the registration.
## Input
BdvHandle bdvh; //
String mode; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.NewSourceCommand
Description: Defines an empty source which occupied the same volume as a model source but with a potentially different voxel size. Works with a single timepoint.
## Input
SourceAndConverter model; // Model Source
Defines the portion of space covered by the new source
String name; // Source name
int timepoint; // Timepoint (0 based index)
double voxsizex; // Voxel Size X
double voxsizey; // Voxel Size Y
double voxsizez; // Voxel Size Z
## Output
SourceAndConverter sac; //


# sc.fiji.bdvpg.scijava.command.source.SampleSourceCreatorCommand
## Input
String samplename; // Sample name
## Output
SourceAndConverter sac; //


# sc.fiji.bdvpg.scijava.command.source.SourceColorChangerCommand
## Input
ColorRGB color; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.SourceTransformerCommand
Description: Applies an affine transformation on several sources.
## Input
int initimepoint; // Initial timepoint (0 based)
double m00; //
double m01; //
double m02; //
double m10; //
double m11; //
double m12; //
double m20; //
double m21; //
double m22; //
String matrixCsv; // Matrix as comma separated numbers
int ntimepoints; // Number of timepoints (min 1)
SourceAndConverter[] sacs; // Select source(s)
double tx; //
double ty; //
double tz; //
## Output


# sc.fiji.bdvpg.scijava.command.source.SourcesDuplicatorCommand
## Input
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.SourcesInvisibleMakerCommand
## Input
SourceAndConverterBdvDisplayService bsds; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.SourcesRemoverCommand
## Input
SourceAndConverterService bss; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.SourcesResamplerCommand
## Input
boolean cache; //
int defaultmipmaplevel; // MipMap level if not re-used (0 = max resolution)
boolean interpolate; //
SourceAndConverter model; //
String name; // Name(s) of the resampled source(s)
boolean reusemipmaps; // Re-use MipMaps
SourceAndConverter[] sacs; // Select Source(s)
## Output
SourceAndConverter[] sacs_out; //


# sc.fiji.bdvpg.scijava.command.source.SourcesVisibleMakerCommand
## Input
SourceAndConverterBdvDisplayService bsds; //
SourceAndConverter[] sacs; // Select Source(s)
## Output


# sc.fiji.bdvpg.scijava.command.source.TransformedSourceWrapperCommand
## Input
SourceAndConverter[] sacs; // Select Source(s)
## Output
SourceAndConverter[] sacs_out; //


# sc.fiji.bdvpg.scijava.command.source.XmlHDF5ExporterCommand
## Input
int blocksizex; //
int blocksizey; //
int blocksizez; //
String entitytype; // Each source is an independent
int nthreads; // # of Threads
int numberoftimepointtoexport; // Number of timepoint to export (minimum 1)
SourceAndConverter[] sacs; // Select Source(s)
int scalefactor; // Scale factor between pyramid levels
int thresholdformipmap; // Dimensions in pixel above which a new resolution level should be created
int timepointbegin; // Timepoint start (0 = first timepoint)
File xmlfile; // Output file (XML)
## Output


# sc.fiji.bdvpg.scijava.command.spimdata.BigDataBrowserPlugInCommand
## Input
CommandService cs; //
LogService ls; //
String serverurl; //
## Output


# sc.fiji.bdvpg.scijava.command.spimdata.MultipleSpimDataImporterCommand
## Input
File[] files; //
String message; //
## Output


# sc.fiji.bdvpg.scijava.command.spimdata.SpimDataExporterCommand
## Input
Context context; //
SourceAndConverter[] sacs; // Select source(s)
File xmlfilepath; // Output File (XML)
## Output


# sc.fiji.bdvpg.scijava.command.spimdata.SpimdataBigDataServerImportCommand
Label: Command that opens a BDV dataset from a BigDataServer. Click on Show to display it.
## Input
String datasetname; // Dataset Name
String urlserver; // Big Data Server URL
## Output


# sc.fiji.bdvpg.scijava.command.viewer.StateSynchronizerCommand
Description: Synchronizes the state of a set of BDV or BVV windows. A window popup should be closed to stop the synchronization
## Input
BdvHandle[] bdvhs; // Select Bdv Windows to synchronize
BvvHandle[] bvvhs; // Select Bvv Windows to synchronize
## Output


# sc.fiji.bdvpg.scijava.command.viewer.ViewSynchronizerCommand
Description: Synchronizes the view of a set of BDV or BVV windows. A window popup should be closed to stop the synchronization
## Input
BdvHandle[] bdvhs; // Select Bdv Windows to synchronize
BvvHandle[] bvvhs; // Select Bvv Windows to synchronize
boolean synchronizetime; // Synchronize timepoints
## Output


