# BigDataViewer BIOP Tools Commands Reference

This document provides a reference for all SciJava commands available in the `bigdataviewer-biop-tools` package.

---

## 1. SPIM Data Commands

Commands for creating, editing, and managing BigDataViewer datasets.

---

### ch.epfl.biop.scijava.command.spimdata.LLS7OpenDatasetCommand

**Description:** Opens a Zeiss Lattice Light Sheet 7 dataset with live deskewing using Bio-Formats and BigDataViewer

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Create BDV Dataset [Zeiss LLS7]`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | czi_file | The CZI file from a Zeiss LLS7 acquisition to open |
| boolean | legacy_xy_mode | When checked, uses legacy XY orientation for compatibility with older datasets |

---

### ch.epfl.biop.scijava.command.spimdata.CreateCZIDatasetCommand

**Description:** Creates a BigStitcher-compatible XML dataset from a CZI file

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Edit>Make CZI Dataset for BigStitcher`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | czi_file | The CZI file to convert for BigStitcher |
| Boolean | erase_if_file_already_exists | When checked, overwrites the output file if it already exists |

#### Output
| Type | Name | Description |
|------|------|-------------|
| File | xml_out | The XML file where the BigStitcher dataset will be saved |

---

### ch.epfl.biop.scijava.command.spimdata.LLS7CropCommand

**Description:** Crops a 3D region from LLS7 sources using an interactive bounding box

**Menu Path:** `Plugins>BigDataViewer-Playground>BDV>LLS7 - Crop 3D`

#### Input
| Type | Name | Description |
|------|------|-------------|
| BdvHandle | bdvh | The BigDataViewer window containing the sources to crop |
| String | image_name | The name for the cropped image |
| SourceAndConverter[] | sources | The source(s) to crop |

#### Output
| Type | Name | Description |
|------|------|-------------|
| RealInterval | interval | The selected 3D bounding box interval |
| Boolean | result | True if the user confirmed the selection, false if cancelled |

---

### ch.epfl.biop.scijava.command.spimdata.ReorderDatasetCommand

**Description:** Reorders a LIF dataset for BigStitcher compatibility (legacy command)

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Edit>(Legacy) Reorder BDV Dataset`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | file | The LIF file to reorder |
| File | xmlout | The XML file where the reordered dataset will be saved |
| int | n_tiles | The number of tiles in the dataset |
| int | n_channels | The number of channels in the dataset |

---

### ch.epfl.biop.scijava.command.spimdata.DatasetToBigStitcherDatasetCommand

**Description:** Converts a BDV dataset to BigStitcher format by removing incompatible attributes and rescaling

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Edit>Make BDVDataset BigStitcher Compatible`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | xmlin | The BDV XML dataset file to convert |
| int | viewsetupreference | View setup index for rescaling reference (-1 to list all and use first) |
| File | xmlout | The XML file where the BigStitcher-compatible dataset will be saved |

---

### ch.epfl.biop.scijava.command.spimdata.RemoveDisplaySettingsCommand

**Description:** Removes display settings attributes from a BDV dataset for compatibility with other tools

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Edit>Remove Display Settings from BDVDataset`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | xmlin | The BDV XML dataset file to modify |
| File | xmlout | The XML file where the modified dataset will be saved |

---

### ch.epfl.biop.scijava.command.spimdata.RemoveEntitiesCommand

**Description:** Removes specified entity types from a BDV dataset for compatibility with other tools

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Edit>Remove Entities from BDVDataset`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | xmlin | The BDV XML dataset file to modify |
| File | xmlout | The XML file where the modified dataset will be saved |
| String | entitiestoremove | Comma-separated list of entity types to remove (e.g., 'displaysettings, fileindex') |

---

### ch.epfl.biop.scijava.command.spimdata.FuseBigStitcherDatasetIntoOMETiffCommand

**Description:** Fuses a BigStitcher dataset and exports it as a pyramidal OME-TIFF file

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Fuse a BigStitcher dataset to OME-Tiff`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | xml_bigstitcher_file | The BigStitcher XML dataset file to fuse |
| File | output_path_directory | The folder where the fused OME-TIFF will be saved |
| String | range_channels | Channels to export (e.g., '0,1' or '0:2'). Leave blank for all channels |
| String | range_slices | Z-slices to export (e.g., '0:100'). Leave blank for all slices |
| String | range_frames | Timepoints to export (e.g., '0:10'). Leave blank for all timepoints |
| int | n_resolution_levels | Number of pyramid resolution levels to generate (scale factor = 2) |
| String | fusion_method | Method used to blend overlapping tiles |
| boolean | use_lzw_compression | When checked, applies LZW compression to reduce file size |
| boolean | split_slices | When checked, exports each Z-slice as a separate file |
| boolean | split_channels | When checked, exports each channel as a separate file |
| boolean | split_frames | When checked, exports each timepoint as a separate file |
| boolean | override_z_ratio | When checked, uses a custom XY/Z anisotropy ratio instead of the dataset value |
| double | z_ratio | Custom ratio between XY and Z pixel sizes |
| double | x_downsample | Downsampling factor in X (1.0 = no downsampling) |
| double | y_downsample | Downsampling factor in Y (1.0 = no downsampling) |
| double | z_downsample | Downsampling factor in Z (1.0 = no downsampling) |
| boolean | use_interpolation | When checked, applies interpolation during fusion (slower but smoother) |

---

### ch.epfl.biop.scijava.command.spimdata.OpenOperettaDatasetCommand

**Description:** Opens a PerkinElmer Operetta high-content imaging dataset in BigDataViewer

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Create BDV Dataset [Operetta]`

#### Input
| Type | Name | Description |
|------|------|-------------|
| String | unit | Unit for the common coordinate system where all datasets will be positioned |
| File | folder | The 'Images' or 'flex' folder containing your Operetta dataset |
| double | min_display_value | Minimum intensity value for display adjustment |
| double | max_display_value | Maximum intensity value for display adjustment |
| boolean | show | When checked, displays the dataset in a new BigDataViewer window |

#### Output
| Type | Name | Description |
|------|------|-------------|
| String | dataset_name | The name assigned to the opened dataset |

---

### ch.epfl.biop.scijava.command.spimdata.SourceFromImagePlusCommand

**Description:** Converts an ImageJ1 ImagePlus to a BigDataViewer dataset for visualization and processing

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Import>Make BDVDataset from current IJ1 image`

#### Input
| Type | Name | Description |
|------|------|-------------|
| ImagePlus | image | The ImagePlus image to convert to a BDV dataset |

---

### ch.epfl.biop.scijava.command.spimdata.OpenImarisCommand

**Description:** Opens an Imaris .ims file as a BigDataViewer dataset

**Menu Path:** `Plugins>BigDataViewer-Playground>BDVDataset>Create BDV Dataset [Imaris]`

#### Input
| Type | Name | Description |
|------|------|-------------|
| File | file | Path to the Imaris .ims file to open |

#### Output
| Type | Name | Description |
|------|------|-------------|
| AbstractSpimData | spimdata | The opened Imaris dataset |

---

## 2. BDV Commands

Commands for BigDataViewer window operations and export.

---

### ch.epfl.biop.scijava.command.bdv.BdvViewToImagePlusExportCommand

**Description:** Exports sources as ImagePlus with full control over sampling and region

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Export>Current BDV View To ImagePlus`

#### Input
| Type | Name | Description |
|------|------|-------------|
| BdvHandle | bdv_h | The BigDataViewer window to export from |
| String | capturename | Name for the exported ImagePlus |
| SourceAndConverter[] | sacs | The source(s) to export |
| boolean | matchwindowsize | When checked, uses the BDV window dimensions for X and Y size |
| double | xsize | Total width in world coordinates units |
| double | ysize | Total height in world coordinates units |
| double | zsize | Half-thickness above and below the current plane (0 for single slice) |
| String | selected_timepoints_str | Timepoints to export (e.g., '0:10' or '0,2,4'). Leave blank for all |
| double | samplingxyinphysicalunit | Output pixel size in XY (world coordinates units) |
| double | samplingzinphysicalunit | Output pixel size in Z (world coordinates units) |
| boolean | interpolate | When checked, uses interpolation when resampling |
| String | export_mode | Normal loads all data; Virtual creates a lazy-loading stack |
| Boolean | parallel_c | When checked, acquires channels in parallel (Normal mode only) |
| Boolean | parallel_z | When checked, acquires Z-slices in parallel (Normal mode only) |
| Boolean | parallel_t | When checked, acquires timepoints in parallel (Normal mode only) |
| String | unit | Physical unit for the output image calibration |

#### Output
| Type | Name | Description |
|------|------|-------------|
| List<ImagePlus> | images | The exported ImagePlus images |

---

### ch.epfl.biop.scijava.command.bdv.userdefinedregion.GetUserPointsCommand

**Description:** Allows user to interactively select points in the BDV viewer

**Menu Path:** User interaction command (not directly in menu)

#### Input
| Type | Name | Description |
|------|------|-------------|
| String | message_for_user | Message displayed to guide the user |
| int | time_out_in_ms | Timeout in milliseconds (-1 for no timeout) |

#### Output
| Type | Name | Description |
|------|------|-------------|
| List<RealPoint> | pts | The selected points |

---

### ch.epfl.biop.scijava.command.bdv.userdefinedregion.GetUserRectangleCommand

**Description:** Allows user to interactively select a rectangle in the BDV viewer

**Menu Path:** User interaction command (not directly in menu)

#### Input
| Type | Name | Description |
|------|------|-------------|
| String | message_for_user | Message displayed to guide the user |
| int | time_out_in_ms | Timeout in milliseconds (-1 for no timeout) |
| RealPoint | p1 | Initial corner point 1 |
| RealPoint | p2 | Initial corner point 2 |

#### Output
| Type | Name | Description |
|------|------|-------------|
| RealPoint | p1 | Selected corner point 1 |
| RealPoint | p2 | Selected corner point 2 |

---

### ch.epfl.biop.scijava.command.bdv.userdefinedregion.BoxSelectorCommand

**Description:** Allows user to interactively select a 3D box region

**Menu Path:** User interaction command (not directly in menu)

---

## 3. Source Export Commands

Commands for exporting sources to various formats.

---

### ch.epfl.biop.scijava.command.source.ExportToImagePlusCommand

**Description:** Exports selected sources to an ImagePlus image

**Menu Path:** Available through source context menu

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | The sources to export |
| int | timepoint | Timepoint to export |
| int | resolution_level | Resolution level to export |

#### Output
| Type | Name | Description |
|------|------|-------------|
| ImagePlus | imp | The exported ImagePlus |

---

### ch.epfl.biop.scijava.command.source.ExportToMultipleImagePlusCommand

**Description:** Exports selected sources to multiple ImagePlus images (one per source)

---

## 4. Source Manipulation Commands

Commands for manipulating and processing sources.

---

### ch.epfl.biop.scijava.command.source.SourceSetAlphaCommand

**Description:** Sets the alpha (transparency) source for blending operations

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | The sources to set alpha for |
| AlphaSource | alpha_source | The alpha source defining transparency |

---

### ch.epfl.biop.scijava.command.source.SourcesFuserAndResamplerCommand

**Description:** Fuses and resamples multiple sources into a single output source

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sources_in | Sources to fuse |
| SourceAndConverter | model | Model source defining output geometry |
| String | fusion_method | Method for fusion (AVERAGE, MAX, etc.) |
| boolean | interpolate | Whether to interpolate during resampling |

---

### ch.epfl.biop.scijava.command.source.FilterSourcesByNameCommand

**Description:** Filters sources based on their name using a pattern

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to filter |
| String | pattern | Name pattern for filtering |

#### Output
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | filtered_sources | Sources matching the pattern |

---

### ch.epfl.biop.scijava.command.source.SourceTimeShiftCommand

**Description:** Shifts the timepoints of sources

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to time-shift |
| int | time_shift | Number of timepoints to shift |

---

### ch.epfl.biop.scijava.command.source.SourcesPyramidizerCommand

**Description:** Creates a multi-resolution pyramid from sources

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to pyramidize |
| int | n_resolution_levels | Number of pyramid levels |
| int | downscaling | Downscaling factor between levels |

---

### ch.epfl.biop.scijava.command.source.SourcesMakeModelCommand

**Description:** Creates a model source from existing sources for resampling operations

---

### ch.epfl.biop.scijava.command.source.GetVoronoiEllipseSampleCommand

**Description:** Samples sources using Voronoi tessellation with elliptical regions

---

### ch.epfl.biop.scijava.command.source.SliceSourceCommand

**Description:** Extracts a single slice from volumetric sources

---

## 5. Source Registration Commands (including Warpy)

Commands for registering sources using various algorithms.

---

### ch.epfl.biop.scijava.command.source.register.Elastix2DAffineRegisterCommand

**Description:** Performs 2D affine registration using Elastix

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Obsolete>Elastix 2D Affine Register`

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs_fixed | Fixed reference sources |
| SourceAndConverter[] | sacs_moving | Moving sources to register |
| int | tp_fixed | Timepoint for fixed sources |
| int | tp_moving | Timepoint for moving sources |
| int | level_fixed_source | Resolution level for fixed sources |
| int | level_moving_source | Resolution level for moving sources |
| double | px, py, pz | Region of interest position |
| double | sx, sy | Region of interest size |
| double | px_size_in_current_unit | Pixel size for registration |
| boolean | interpolate | Use interpolation |
| boolean | show_image_registration | Display registration result |
| int | max_iteration_per_scale | Maximum iterations per scale |
| double | background_offset_value_moving | Background offset for moving image |
| double | background_offset_value_fixed | Background offset for fixed image |

#### Output
| Type | Name | Description |
|------|------|-------------|
| AffineTransform3D | at3d | The computed affine transform |

---

### ch.epfl.biop.scijava.command.source.register.Elastix2DSplineRegisterCommand

**Description:** Performs 2D B-spline deformable registration using Elastix

---

### ch.epfl.biop.scijava.command.source.register.Elastix2DSparsePointsRegisterCommand

**Description:** Performs sparse point-based registration using Elastix

---

### ch.epfl.biop.scijava.command.source.register.Sift2DAffineRegisterCommand

**Description:** Performs 2D affine registration using SIFT feature matching

---

### ch.epfl.biop.scijava.command.source.register.SourcesAffineTransformCommand

**Description:** Applies an affine transform to sources

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to transform |
| AffineTransform3D | transform | The affine transform to apply |

---

### ch.epfl.biop.scijava.command.source.register.SourcesRealTransformCommand

**Description:** Applies a RealTransform to sources

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to transform |
| RealTransform | transform | The transform to apply |

---

### ch.epfl.biop.scijava.command.source.register.SelectSourcesForRegistrationCommand

**Description:** Helper command to select sources for registration workflows

---

### ch.epfl.biop.scijava.command.source.register.AffineTransformCreatorCommand

**Description:** Creates an affine transform from parameters

---

### ch.epfl.biop.scijava.command.source.register.WarpyRegisterCommand

**Description:** Interactive wizard for registering QuPath entries with visual landmark editing

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>QuPath - Create Warpy Registration`

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | fixed_sources | Reference source(s) from the QuPath project |
| SourceAndConverter[] | moving_sources | Source(s) to be registered to the fixed reference |
| boolean | verbose | Enable verbose logging |

---

### ch.epfl.biop.scijava.command.source.register.WarpyMultiscaleRegisterCommand

**Description:** Performs automated multiscale registration between QuPath entries, saved to the project

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>QuPath - Create Warpy Multiscale Registration`

#### Input
| Type | Name | Description |
|------|------|-------------|
| int | n_scales | Number of resolution scales for registration (more scales = more precise but slower) |
| SourceAndConverter[] | fixed_sources | Reference source(s) from the QuPath project |
| SourceAndConverter[] | moving_sources | Source(s) to be registered to the fixed reference |
| boolean | remove_z_offset | When checked, removes Z position offsets from sources for 2D registration |
| boolean | center_moving_image | When checked, initially centers the moving image on the fixed image |
| int | pixels_per_block | Size in pixels of each image block used for local registration |
| int | max_iteration_number_per_scale | Maximum number of iterations for each registration at each scale |

---

### ch.epfl.biop.scijava.command.source.register.WarpyEditRegistrationCommand

**Description:** Opens BigWarp to manually edit an existing Warpy registration between QuPath entries

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>QuPath - Edit Warpy Registration`

#### Input
| Type | Name | Description |
|------|------|-------------|
| boolean | remove_z_offsets | When checked, removes Z position offsets from sources for 2D editing |
| SourceAndConverter[] | fixed_sources | Reference source(s) from the QuPath project |
| SourceAndConverter[] | moving_sources | Source(s) that were registered to the fixed reference |

---

### ch.epfl.biop.scijava.command.source.register.WarpyExportRegisteredImageCommand

**Description:** Exports Warpy-registered sources from a QuPath project to a fused OME-TIFF file

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>QuPath - Export Warpy Registered Image`

#### Input
| Type | Name | Description |
|------|------|-------------|
| boolean | remove_z_offsets | When checked, removes Z position offsets from sources |
| boolean | pre_compute_transform | When checked, pre-computes the deformation field (faster for >40 landmarks) |
| int | pre_compute_downsample_xy | Downsampling factor for pre-computed deformation field (higher = faster but less precise) |
| SourceAndConverter[] | fixed_sources | Reference source(s) that define the output geometry |
| SourceAndConverter[] | moving_sources | Registered source(s) to export |
| boolean | include_fixed_sources | When checked, includes fixed sources as channels in the exported image |
| boolean | interpolate | When checked, uses interpolation when resampling |
| double | upsample | Factor to up (>1) or downsample (<1) the exported image resolution |

---

### ch.epfl.biop.scijava.command.source.register.RegisterWholeSlideScans2DCommand

**Description:** Obsolete command for aligning 2D whole slide scans

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Obsolete>Align Slides (2D)`

---

### ch.epfl.biop.scijava.command.source.register.MultiscaleRegisterCommand

**Description:** Obsolete command for multiscale 2D registration

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Obsolete>Multiscale Registration (2D)`

---

### ch.epfl.biop.scijava.command.source.register.Wizard2DWholeScanRegisterCommand

**Description:** Interactive wizard for whole slide 2D registration

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Wizard Align Slides (2D)`

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter | fixed | Fixed reference source |
| SourceAndConverter | moving | Moving source used for registration to the reference |
| SourceAndConverter[] | sources_to_transform | Sources to transform, including the moving source if needed |
| boolean | remove_z_offset | Remove images z-offsets |
| boolean | center_moving_image | Center moving image with fixed image |
| boolean | manual_rigid_registration | Perform manual rigid registration step |
| boolean | automated_affine_registration | Perform automated affine registration step |
| boolean | automated_spline_registration | Perform semi-automated spline registration step |
| boolean | manual_spline_registration | Perform manual spline registration (BigWarp) step |
| double | coarse_pixel_size_um | Pixel size for coarse registration in microns |
| double | patch_size_um | Patch size for registration in microns |
| double | precise_pixel_size_um | Pixel size for precise patch registration in microns |
| int | max_iteration_number_per_scale | Number of iterations for each scale |
| boolean | show_details | Show results of automated registrations |

#### Output
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | transformed_sources | The transformed sources |
| RealTransform | transformation | The computed transformation |

---

## 6. Transform Commands

Commands for creating and applying geometric transforms to sources.

---

### ch.epfl.biop.scijava.command.transform.RemoveZOffsetCommand

**Description:** Removes the Z position offset from sources, centering them at Z=0

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Transform>Remove Z Offset`

#### Input
| Type | Name | Description |
|------|------|-------------|
| int | timepoint | Timepoint used to compute the Z offset |
| SourceAndConverter[] | sacs | The sources to remove Z offset from |
| String | mode | Mutate modifies existing transform; Append adds a new transform layer |

---

### ch.epfl.biop.scijava.command.transform.SourcesRecenterCommand

**Description:** Moves sources so their center is at the specified coordinates

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Transform>Recenter sources`

#### Input
| Type | Name | Description |
|------|------|-------------|
| int | timepoint | Timepoint used for computing the recentering transform |
| double | cx | Target X coordinate for the source center |
| double | cy | Target Y coordinate for the source center |
| double | cz | Target Z coordinate for the source center |
| SourceAndConverter[] | sacs | The sources to recenter |
| String | mode | Mutate modifies existing transform; Append adds a new transform layer |

---

### ch.epfl.biop.scijava.command.transform.Rotation3DTransformCommand

**Description:** Applies interactive 3D rotation to sources around a specified center point

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Transform>Rotation 3D Transform`

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | The sources to rotate (must be wrapped as TransformedSource) |
| int | rx | Rotation angle around X axis in degrees |
| int | ry | Rotation angle around Y axis in degrees |
| double | rz | Rotation angle around Z axis in degrees |
| double | cx | X coordinate of rotation center |
| double | cy | Y coordinate of rotation center |
| double | cz | Z coordinate of rotation center |

---

### ch.epfl.biop.scijava.command.transform.Elliptic3DTransformCreatorCommand

**Description:** Creates a new elliptical 3D transform with specified radii, rotation, and center

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Transform>New Elliptic 3D Transform`

#### Input
| Type | Name | Description |
|------|------|-------------|
| double | radius_x | Radius along the first ellipse axis |
| double | radius_y | Radius along the second ellipse axis |
| double | radius_z | Radius along the third ellipse axis |
| double | rotation_x | Euler rotation angle around X axis (radians) |
| double | rotation_y | Euler rotation angle around Y axis (radians) |
| double | rotation_z | Euler rotation angle around Z axis (radians) |
| double | center_x | X coordinate of ellipse center |
| double | center_y | Y coordinate of ellipse center |
| double | center_z | Z coordinate of ellipse center |

#### Output
| Type | Name | Description |
|------|------|-------------|
| Elliptical3DTransform | e3dt | The created elliptical 3D transform |

---

### ch.epfl.biop.scijava.command.transform.Elliptic3DTransformerCommand

**Description:** Applies an elliptical 3D transform to sources for spherical/ellipsoidal projection

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Transform>Elliptic 3D Transform Sources`

#### Input
| Type | Name | Description |
|------|------|-------------|
| Elliptical3DTransform | e3dt | The elliptical 3D transform to apply |
| SourceAndConverter[] | sacs_in | The sources to transform |

---

## 7. Pair Registration Commands (Warpy workflow)

Commands for the registration pair workflow, enabling step-by-step registration with GUI support.

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationCreateCommand

**Description:** Creates a new registration pair from fixed and moving sources for the Warpy workflow

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Create registration pair`

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | fixed_sources | The reference source(s) that will remain stationary during registration |
| SourceAndConverter[] | moving_sources | The source(s) to be registered and aligned to the fixed source(s) |
| String | registration_name | A unique name to identify this registration pair |

#### Output
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The created registration pair object |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationAddGUICommand

**Description:** Opens a BigDataViewer window with controls for performing registrations

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Registration pair - Add GUI`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to visualize and control |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationDeleteCommand

**Description:** Removes a registration pair from memory and closes associated resources

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Delete registration pair`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to delete |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationCenterCommand

**Description:** Applies a translation to center the moving sources over the fixed sources

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair - Center moving sources on fixed sources`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to apply the registration to |

#### Output
| Type | Name | Description |
|------|------|-------------|
| boolean | success | True if the registration completed successfully |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationSift2DAffineCommand

**Description:** Performs automatic 2D affine registration using SIFT feature matching

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair 2D - Sift Affine`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to apply the registration to |
| String | bounds | How to define the region of interest: intersection of sources, union of sources, or custom coordinates |
| double | px, py, sx, sy | ROI position and size (only used when ROI Mode is 'custom') |
| String | channels_fixed_csv | Channel indices of the fixed image to use for registration (comma separated) |
| String | channels_moving_csv | Channel indices of the moving image to use for registration (comma separated) |
| double | pixel_size_micrometer | Pixel size in micrometers for resampling during registration |
| boolean | invert_moving | When checked, inverts the intensity of the moving image before matching |
| boolean | invert_fixed | When checked, inverts the intensity of the fixed image before matching |

#### Output
| Type | Name | Description |
|------|------|-------------|
| boolean | success | True if the registration completed successfully |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationElastix2DAffineCommand

**Description:** Performs automatic 2D affine registration using Elastix

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair 2D - Elastix Affine`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to apply the registration to |
| String | bounds | How to define the region of interest |
| double | px, py, sx, sy | ROI position and size (only used when ROI Mode is 'custom') |
| String | channels_fixed_csv | Channel indices of the fixed image to use for registration |
| String | channels_moving_csv | Channel indices of the moving image to use for registration |
| double | pixel_size_micrometer | Pixel size in micrometers for resampling during registration |
| boolean | show_imageplus_registration_result | When checked, displays the registration result as an ImagePlus for verification |

#### Output
| Type | Name | Description |
|------|------|-------------|
| boolean | success | True if the registration completed successfully |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationElastix2DSplineCommand

**Description:** Performs automatic 2D B-spline deformable registration using Elastix

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair 2D - Elastix Spline`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to apply the registration to |
| int | nb_control_points_x | Number of B-spline control points along X axis (minimum 2, more = finer deformation) |
| String | bounds | How to define the region of interest |
| double | px, py, sx, sy | ROI position and size (only used when ROI Mode is 'custom') |
| String | channels_fixed_csv | Channel indices of the fixed image to use for registration |
| String | channels_moving_csv | Channel indices of the moving image to use for registration |
| double | pixel_size_micrometer | Pixel size in micrometers for resampling during registration |
| boolean | show_imageplus_registration_result | When checked, displays the registration result as an ImagePlus for verification |

#### Output
| Type | Name | Description |
|------|------|-------------|
| boolean | success | True if the registration completed successfully |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationBigWarp2DSplineCommand

**Description:** Opens BigWarp for interactive manual landmark-based spline registration

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair 2D - BigWarp Spline`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to apply the registration to |

#### Output
| Type | Name | Description |
|------|------|-------------|
| boolean | success | True if the registration completed successfully |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationEditLastRegistrationCommand

**Description:** Re-opens the last registration step for editing (e.g., adjust landmarks)

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair - Edit last registration`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair whose last step will be edited |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationRemoveLastRegistrationCommand

**Description:** Removes the last registration step from the registration pair

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Register>Register Pair - Remove last registration`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair whose last step will be removed |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationExportToQuPathCommand

**Description:** Exports the registration transforms to a QuPath project for use in Warpy

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Export>Register Pair - Export registration to QuPath project`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to export |
| boolean | allow_overwrite | When checked, overwrites existing registration files in the QuPath project |

---

### ch.epfl.biop.registration.scijava.command.PairRegistrationExportToOMETIFFCommand

**Description:** Exports the registered images as a pyramidal OME-TIFF file

**Menu Path:** `Plugins>BigDataViewer-Playground>Sources>Export>Register Pair - Export registration to OME-TIFF`

#### Input
| Type | Name | Description |
|------|------|-------------|
| RegistrationPair | registration_pair | The registration pair to export |
| boolean | interpolate | When checked, uses interpolation when resampling the moving image |
| String | channels_fixed_csv | Channels from fixed image to include (comma separated, empty for none, '*' for all) |
| String | channels_moving_csv | Channels from moving image to include (comma separated, empty for none, '*' for all) |
| File | file_path | Path where the OME-TIFF will be saved |
| int | n_resolution_levels | Number of pyramid resolution levels to generate |
| int | downscaling | Scale factor between consecutive resolution levels |
| int | tile_size_x | Width of tiles in pixels (negative for no tiling) |
| int | tile_size_y | Height of tiles in pixels (negative for no tiling) |
| int | n_threads | Number of parallel threads for export (0 = serial processing) |
| String | compression | Compression algorithm for the output file (LZW, Uncompressed, JPEG-2000, JPEG-2000 Lossy, JPEG) |
| boolean | compress_temp_files | When checked, compresses temporary files to save disk space during export |

---

## 8. Deconvolution Commands

Commands for image deconvolution.

---

### ch.epfl.biop.scijava.command.source.deconvolve.SourcesDeconvolverCommand

**Description:** Performs deconvolution on sources using various algorithms

#### Input
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | sacs | Sources to deconvolve |
| SourceAndConverter | psf | Point spread function source |
| String | algorithm | Deconvolution algorithm to use |
| int | n_iterations | Number of deconvolution iterations |

#### Output
| Type | Name | Description |
|------|------|-------------|
| SourceAndConverter[] | deconvolved_sources | The deconvolved sources |
