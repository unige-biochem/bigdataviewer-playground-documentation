# Headless Registration (Automated)

All the commands used previously also exist directly in Fiji's search bar and are **macro recordable**. This is the basis of how we will perform headless registration.

:::{note}
A registration may fail (for instance if SIFT does not find any corresponding landmarks). The macro way of batching can't handle this failure currently. If you want to handle registration failures, scripting should be done with another language (groovy, jython).
:::

## Recording the Macro

1. **Close and restart Fiji** (NO NEED if you started the recorder at the start of Part A)
2. Run `Plugins > Macros > Record…`
3. Repeat the commands we've done previously, but running them from Fiji's search bar

### Summary of Commands

Here's a summary of what we've done:

1. `Dataset - Create [QuPath]`
2. `Create Registration Pair`
3. `Register Pair - Center Moving Sources On Fixed Sources`
4. `Register Pair - Affine SIFT 2D`
5. `Register Pair - Spline Elastix 2D`
6. `Register Pair - Export To QuPath`


:::{note}
If you want to clean up and clear memory, you can run the command `Delete Registration Pair`. You can also run `State - Clear` when you're fully done with a specific QuPath project.
:::
 
4. Press **Create** on the recorder window

## Editing the Recorded Macro

You will get a draft macro that will need to be slightly tweaked to perform registration in a fully automated manner.

### Initial Recorded Macro

```{code-block} imagej
:caption: ImageJ Macro

run("Dataset - Create [QuPath]",
    "qupath_project=C:\\Users\\Nicolas\\Documents\\warpy-demo-project.qpproj datasetname=warpy-demo-project split_rgb_channels=false plane_origin_convention=[TOP_LEFT] unit=MILLIMETER");

run("BDV - Set Style (Playground)",
    "resettodefault=false width=640 height=480 screenscales=[1, 0.5, 0.25, 0.125] numrenderingthreads=3 numtimepoints=10 framerate=10 fontSize=18 font=Courier interpolate=false");

run("BDV - Show Sources",
    "sources=[Lbdv.viewer.SourceAndConverter;@2f96ec0d auto_contrast=true adjust_view=true make_new_window=true interpolate=false");

run("Create Registration Pair",
    "fixed_sources=[Lbdv.viewer.SourceAndConverter;@5300cdb5 moving_sources=[Lbdv.viewer.SourceAndConverter;@2a8dfadc registration_name=dab_fluo");

run("Register Pair - Add GUI",
    "registration_pair=dab_fluo");

run("Register Pair - Center Moving Sources On Fixed Sources");

run("Register Pair - Affine SIFT 2D",
    "bounds=intersection px=1.277347001011156 py=0.5464955005773834 sx=2.0596159999999992 sy=1.5418389999999995 transformation_model=AFFINE channels_fixed_csv=0 channels_moving_csv=0 pixel_size_micrometer=1.0 invert_moving=false invert_fixed=false");

run("Register Pair - Spline Elastic 2D",
    "bounds=intersection px=1.0915305234120407 py=0.595938721809441 sx=2.022231206667339 sy=1.495165183359435 nb_control_points_x=8 channels_fixed_csv=0 channels_moving_csv=0 pixel_size_micrometer=2.0 show_imageplus_registration_result=false");

run("Register Pair - Export To QuPath",
    "allow_overwrite=true");

```

### Required Edits

You can get rid of all unnecessary commands for batch processing (anything GUI related: BIOP Style, Show Sources, ...).

#### 1. Replace px, py, sx, sy with 0

All the `px`, `py`, `sx`, and `sy` parameters are irrelevant since we specify intersection or union, but they still need to be there.

- Replace these parameter values with **0**

#### 2. Format Parameters on Multiple Lines

Take the time to format all parameters in multiple lines for readability:

```{code-block} imagej
:caption: ImageJ Macro

run("Dataset - Create [QuPath]",
    "qupath_project=C:\\Users\\Nicolas\\Documents\\warpy-demo-project.qpproj "+
    "datasetname=warpy-demo-project "+
    "split_rgb_channels=false "+
    "plane_origin_convention=[TOP_LEFT] "+
    "unit=MILLIMETER");

run("Create Registration Pair",
    "fixed_sources=[Lbdv.viewer.SourceAndConverter;@5300cdb5 "+
    "moving_sources=[Lbdv.viewer.SourceAndConverter;@2a8dfadc "+
    "registration_name=dab_fluo");

run("Register Pair - Center Moving Sources On Fixed Sources");

run("Register Pair - Affine SIFT 2D",
    "bounds=intersection "+
    "px=0 py=0 sx=0 sy=0 "+
    "transformation_model=AFFINE "+
    "channels_fixed_csv=0 "+
    "channels_moving_csv=0 "+
    "pixel_size_micrometer=1.0 "+
    "invert_moving=false "+
    "invert_fixed=false");

run("Register Pair - Spline Elastic 2D",
    "bounds=intersection "+
    "px=0 py=0 sx=0 sy=0 "+
    "nb_control_points_x=8 "+
    "channels_fixed_csv=0 "+
    "channels_moving_csv=0 "+
    "pixel_size_micrometer=2.0 "+
    "show_imageplus_registration_result=false");

run("Register Pair - Export To QuPath",
    "allow_overwrite=true");
```

#### 3. Fix Source Selection

The remaining blocking point is the way to set the **fixed sources** and **moving sources** in the `Create Registration Pair` command. These parameters are unfortunately not well recorded, and running the script will give an error.

The way to specify the sources is to write the path of the sources as it appears in the BDV Sources window. Multiple paths can lead to the same sources.

**Example paths:**
- `warpy-demo-project>ImageName>Fluo`
- `warpy-demo-project>QuPathEntryIdEntity>QuPathEntryIdEntity 1`

To select several sources, identify the parent of this path.

**Corrected example:**

```{code-block} imagej
:caption: ImageJ Macro
run("Create Registration Pair",
    "fixed_sources=[warpy-demo-project>QuPathEntryIdEntity>QuPathEntryIdEntity 2] "+
    "moving_sources=[warpy-demo-project>QuPathEntryIdEntity>QuPathEntryIdEntity 1] "+
    "registration_name=dab_fluo");
```

- Edit the macro according to your choices to get the right selection of fixed and moving sources
- Add a `print("Done")` message at the end

### Important: Add Registration Pair Parameter

:::{warning}
When registration commands are run through the GUI, there is a parameter missing in the recorder that tells the software which registration pair to work on.
:::

You can correct this by adding a line to each registration command:

**Before:**
```{code-block} imagej
:caption: ImageJ Macro
run("Register Pair - Center Moving Sources On Fixed Sources");
```

**After:**
```{code-block} imagej
:caption: ImageJ Macro
run("Register Pair - Center Moving Sources On Fixed Sources",
    "registration_pair=[dab_fluo]");
```

**Complete corrected command:**

```{code-block} imagej
:caption: ImageJ Macro
run("Register Pair - Affine SIFT 2D",
    "registration_pair=[dab_fluo] "+
    "bounds=intersection "+
    "px=0 "+
    "py=0 "+
    "sx=0 "+
    "sy=0 "+
    "channels_fixed_csv=0 "+
    "channels_moving_csv=0 "+
    "pixel_size_micrometer=1.0 "+
    "invert_moving=true "+
    "invert_fixed=false");
```

**OR** run the command outside of the GUI during the registration process when recording.

When you run the command from outside the registration pair GUI, you will be prompted to specify which registration pair you need to work on (don't forget to click the line, even if it's a single line):

![Select Registration Pair](images/page_24_img_1.png)

![Script Parameters Dialog](images/page_25_img_1.png)

## Optional: Add Script Parameters

A last thing that can be done is to modularize the hard-coded parameters and use SciJava script parameters instead.

## Final Macro Example

You can find an example of a full macro including SciJava parameters:

```{code-block} imagej
:caption: ImageJ Macro
#@ File qupath_project (label="QuPath Project File")
#@ String registration_dataset_name (label = "Name of Dataset for registration", value="Warpy demo project")
#@ Integer fixed_source_qupath_entry_id (label = "Fixed Source QuPath Entry ID", value=2)
#@ Integer moving_source_qupath_entry_id (label = "Moving Source QuPath Entry ID", value=1)
#@ String registration_pair_name (label = "Name of registration pair", value="Fluo to DAB")

// Make sure there are no sources before we start with the registration
run("State - Clear");

// Load the data from the QuPath project
run("Dataset - Create [QuPath]",
    "qupath_project=["+qupath_project+"] "+
    "datasetname=["+registration_dataset_name+"] "+
    "unit=MILLIMETER "+
    "split_rgb_channels=false "+
    "plane_origin_convention=[TOP LEFT]");

// This macro will only create one registration pair, but of course we could do multiple,
// as long as they are uniquely named
run("Create Registration Pair",
    "fixed_sources=["+registration_dataset_name+">QuPathEntryIdEntity>QuPathEntryIdEntity "+fixed_source_qupath_entry_id+"] "+
    "moving_sources=["+registration_dataset_name+">QuPathEntryIdEntity>QuPathEntryIdEntity "+moving_source_qupath_entry_id+"] "+
    "registration_name=["+registration_pair_name+"]");

// First registration: Centering the two sources
run("Register Pair - Center Moving Sources On Fixed Sources",
    "registration_pair=["+registration_pair_name+"]");

// An affine transform using Scale Invariant Features
run("Register Pair - Affine SIFT 2D",
    "registration_pair=["+registration_pair_name+"] "+
    "bounds=intersection "+
    "px=0 "+
    "py=0 "+
    "sx=0 "+
    "sy=0 "+
    "channels_fixed_csv=0 "+
    "channels_moving_csv=0 "+
    "pixel_size_micrometer=1.0 "+
    "invert_moving=true "+
    "invert_fixed=false");

// A fancier local registration using a grid of 8x8 spline registrations
run("Register Pair - Spline Elastix 2D",
    "registration_pair=["+registration_pair_name+"] "+
    "bounds=intersection "+
    "px=0 "+
    "py=0 "+
    "sx=0 "+
    "sy=0 "+
    "nb_control_points_x=8 "+
    "channels_fixed_csv=0 "+
    "channels_moving_csv=0 "+
    "pixel_size_micrometer=2.0 "+
    "show_imageplus_registration_result=false");

// Finish the job: Export the necessary results to QuPath so Warpy can detect the work we did
run("Register Pair - Export To QuPath",
    "registration_pair=["+registration_pair_name+"] "+
    "allow_overwrite=true");

print("Registration Workflow Demo Finished");
```

## Running the Macro

1. Save your macro
2. Close and open Fiji
3. Open the macro
4. Run the macro and make sure it proceeds completely until "Done" appears, without any user input (except script parameters if you've added some)

---

## Next Steps

- **[Using Registration in QuPath](qupath-usage.md)** - Transfer annotations and create combined images
- **[Serial Sections Registration](serial-sections.md)** - Register multiple sequential slices
