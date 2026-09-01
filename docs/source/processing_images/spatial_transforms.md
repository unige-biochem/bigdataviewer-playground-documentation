# Spatial Transforms

Commands for spatially transforming sources and inspecting or editing the transform chain of your datasets.

Each source in a dataset carries a **chain of affine transforms** that maps pixel coordinates to world coordinates. The commands here let you add, remove, inspect, or modify entries in that chain — no pixels are rewritten. Transforms are instant and non-destructive.

---

## Source Transforms

These commands add affine transforms to a source's transform chain interactively or programmatically.

All commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Process > Transform`

### Source - Basic Transformation

*Source: {bdvpg-src}`SourceSimpleTransformCommand.java <sc/fiji/bdvpg/command/process/transform/SourceSimpleTransformCommand.java>`*

Performs 90/180/270-degree rotations or mirror flips along X, Y, or Z axes.

| Parameter | Description |
|-----------|-------------|
| Select source(s) | The source(s) to transform |
| Transformation type | Flip (mirror) or Rot (rotate by 90/180/270 degrees) |
| Axis | Axis along which to perform the transformation |
| Global transform | If checked, transforms relative to world origin (0,0,0). Otherwise, keeps each source center unchanged |
| Initial timepoint | First timepoint to apply the transformation (0-based) |
| Number of timepoints | Number of timepoints to apply the transformation to |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Process --> Transform --> Source - Basic Transformation`
::::

::::{tab-item} IJ Macro
```ijm
// Sources are selected interactively from the dialog.
run("Source - Basic Transformation");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.process.transform.SourceSimpleTransformCommand

// type: "Flip", "Rot90", "Rot180", "Rot270"
// axis: "X", "Y", "Z"
cs.run(SourceSimpleTransformCommand, true,
    "sources", sources,
    "type", "Rot90",
    "axis", "Z",
    "global_change", false,
    "ini_timepoint", 0,
    "n_timepoints", 1
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.process.transform import SourceSimpleTransformCommand

# type: "Flip", "Rot90", "Rot180", "Rot270"
# axis: "X", "Y", "Z"
cs.run(SourceSimpleTransformCommand, True,
    ["sources", sources,
     "type", "Rot90",
     "axis", "Z",
     "global_change", False,
     "ini_timepoint", 0,
     "n_timepoints", 1]
).get()
```
::::

:::::

### Source - Interactive Transformation

*Source: {bdvpg-src}`SourceManualTransformCommand.java <sc/fiji/bdvpg/command/process/transform/SourceManualTransformCommand.java>`*

Lets you manually drag sources in a BDV window to position them. The sources you select are the ones that move — all other sources in the window stay fixed as reference.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to manually transform |
| Select BDV Window | The BigDataViewer window used for manual positioning |
| Mode | How to apply the transformation: **Mutate** modifies the existing transform, **Append** adds a new transform layer |

:::{note}
During interactive transformation, you are placed in the coordinate frame of the moving sources — so the moving sources appear stationary while the reference sources move. This is normal. When you confirm the transform, the result is applied to the moving sources.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Process --> Transform --> Source - Interactive Transformation`
::::

:::::

### New Affine Transform

*Source: {biop-src}`AffineTransformCreateCommand.java <ch/epfl/biop/command/register/AffineTransformCreateCommand.java>`*

Creates an affine transform from a 4x3 matrix (12 comma-separated values in row-major order). Use this when you need to apply a known numeric transform to sources via the Dataset transform stack commands.

| Parameter | Description |
|-----------|-------------|
| Transform Matrix | 12 comma-separated values defining a 4x3 affine matrix in row-major order |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Process --> Transform --> New Affine Transform`
::::

::::{tab-item} IJ Macro
```ijm
run("New Affine Transform");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.command.register.AffineTransformCreateCommand

// Identity transform: 1,0,0,0, 0,1,0,0, 0,0,1,0
def result = cs.run(AffineTransformCreateCommand, true,
    "string_matrix", "1,0,0,0,0,1,0,0,0,0,1,0"
).get()

def at3d = result.getOutput("at3d")
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.command.register import AffineTransformCreateCommand

# Identity transform: 1,0,0,0, 0,1,0,0, 0,0,1,0
result = cs.run(AffineTransformCreateCommand, True,
    ["string_matrix", "1,0,0,0,0,1,0,0,0,0,1,0"]
).get()

at3d = result.getOutput("at3d")
```
::::

:::::

### Source - Recenter Sources

*Source: {biop-src}`SourcesRecenterCommand.java <ch/epfl/biop/command/process/transform/SourcesRecenterCommand.java>`*

Moves sources so their center is at the specified world coordinates. Useful for aligning sources to a common reference point.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to recenter |
| Center X/Y/Z | Target world coordinates for the source center |
| Timepoint | Timepoint used for computing the recentering transform |
| Mode | **Mutate** modifies the existing transform; **Append** adds a new transform layer |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Process --> Transform --> Source - Recenter Sources`
::::

::::{tab-item} IJ Macro
```ijm
// Sources are selected interactively from the dialog.
run("Source - Recenter Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.process.transform.SourcesRecenterCommand

cs.run(SourcesRecenterCommand, true,
    "sources", sources,
    "cx", 0.0,
    "cy", 0.0,
    "cz", 0.0,
    "timepoint", 0,
    "mode", "Append"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.process.transform import SourcesRecenterCommand

cs.run(SourcesRecenterCommand, True,
    ["sources", sources,
     "cx", 0.0,
     "cy", 0.0,
     "cz", 0.0,
     "timepoint", 0,
     "mode", "Append"]
).get()
```
::::

:::::

### Source - Remove Z Offset

*Source: {biop-src}`SourcesZOffsetRemoveCommand.java <ch/epfl/biop/command/process/transform/SourcesZOffsetRemoveCommand.java>`*

Removes the Z position offset from sources, shifting them to Z=0. Useful when imported data has a large Z offset that makes navigation awkward.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to remove Z offset from |
| Timepoint | Timepoint used to compute the Z offset |
| Apply to all timepoints | If checked, removes Z offset for each timepoint independently |
| Mode | **Mutate** modifies the existing transform; **Append** adds a new transform layer |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Process --> Transform --> Source - Remove Z Offset`
::::

::::{tab-item} IJ Macro
```ijm
// Sources are selected interactively from the dialog.
run("Source - Remove Z Offset");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.process.transform.SourcesZOffsetRemoveCommand

cs.run(SourcesZOffsetRemoveCommand, true,
    "sources", sources,
    "timepoint", 0,
    "apply_to_all_timepoints", false,
    "mode", "Append"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.process.transform import SourcesZOffsetRemoveCommand

cs.run(SourcesZOffsetRemoveCommand, True,
    ["sources", sources,
     "timepoint", 0,
     "apply_to_all_timepoints", False,
     "mode", "Append"]
).get()
```
::::

:::::

:::{note}
**About "Make Transformable"**: Sources created from a dataset already carry a mutable affine transform chain and can be transformed directly. The command **Source - Make Transformable** (`Process > Source - Make Transformable`) is only needed for sources that were not created from a dataset (e.g. procedurally generated sources). It wraps the source in a TransformedSource so that interactive and programmatic transforms can be applied.
:::

---

(dataset-transform-stack)=

## Dataset Transform Stack

These commands let you inspect and edit the full transform chain of a dataset — the ordered list of affine transforms stored in the XML file for each source. They operate on the dataset level and are especially useful for manual corrections or advanced registration workflows.

All commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Dataset > Transform Stack`

### Dataset - View Transforms

*Source: {bdvpg-src}`DatasetTransformViewCommand.java <sc/fiji/bdvpg/command/dataset/transform/DatasetTransformViewCommand.java>`*

Displays the full transform chain for each selected source as a table.

| Parameter | Description |
|-----------|-------------|
| Sources | The sources whose transforms you want to inspect |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - View Transforms`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - View Transforms");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.dataset.transform.DatasetTransformViewCommand

cs.run(DatasetTransformViewCommand, true,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.dataset.transform import DatasetTransformViewCommand

cs.run(DatasetTransformViewCommand, True,
    ["sources", sources]
).get()
```
::::

:::::

### Dataset - Add Transforms

*Source: {bdvpg-src}`DatasetTransformAddCommand.java <sc/fiji/bdvpg/command/dataset/transform/DatasetTransformAddCommand.java>`*

Appends a new affine transform to the chain at a given position.

| Parameter | Description |
|-----------|-------------|
| Sources | The sources to modify |
| Transform Name | A label for this transform entry |
| Transform Matrix | 12 comma-separated values defining the 3D affine (row-major, no last row) |
| Position | Index in the chain where the transform is inserted (-1 = append at end) |
| Timepoint Range | Timepoints to apply to (e.g. `0:last` or `0:5`) |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Add Transforms`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - Add Transforms");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.dataset.transform.DatasetTransformAddCommand

cs.run(DatasetTransformAddCommand, true,
    "sources", sources,
    "transform_name", "Manual correction",
    "transform_matrix", "1,0,0,0,0,1,0,0,0,0,1,0",
    "position", -1,
    "timepoint_range", "0:last"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.dataset.transform import DatasetTransformAddCommand

cs.run(DatasetTransformAddCommand, True,
    ["sources", sources,
     "transform_name", "Manual correction",
     "transform_matrix", "1,0,0,0,0,1,0,0,0,0,1,0",
     "position", -1,
     "timepoint_range", "0:last"]
).get()
```
::::

:::::

### Dataset - Remove Transforms

*Source: {bdvpg-src}`DatasetTransformRemoveCommand.java <sc/fiji/bdvpg/command/dataset/transform/DatasetTransformRemoveCommand.java>`*

Removes one or more transforms from the chain by index.

| Parameter | Description |
|-----------|-------------|
| Sources | The sources to modify |
| Transform Index Range | Indices of transforms to remove (e.g. `-1` for the last, `0:2` for the first three) |
| Timepoint Range | Timepoints to apply to (e.g. `0:last`) |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Remove Transforms`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - Remove Transforms");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.dataset.transform.DatasetTransformRemoveCommand

cs.run(DatasetTransformRemoveCommand, true,
    "sources", sources,
    "transform_index_range", "-1",
    "timepoint_range", "0:last"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.dataset.transform import DatasetTransformRemoveCommand

cs.run(DatasetTransformRemoveCommand, True,
    ["sources", sources,
     "transform_index_range", "-1",
     "timepoint_range", "0:last"]
).get()
```
::::

:::::

### Dataset - Set Transforms

*Source: {bdvpg-src}`DatasetTransformSetCommand.java <sc/fiji/bdvpg/command/dataset/transform/DatasetTransformSetCommand.java>`*

Overwrites a transform at a specific position in the chain.

| Parameter | Description |
|-----------|-------------|
| Sources | The sources to modify |
| Transform Index Range | Indices of transforms to overwrite |
| Transform Name | New label for the transform entry |
| Transform Matrix | 12 comma-separated values defining the 3D affine |
| Timepoint Range | Timepoints to apply to (e.g. `0:last`) |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Set Transforms`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - Set Transforms");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.dataset.transform.DatasetTransformSetCommand

cs.run(DatasetTransformSetCommand, true,
    "sources", sources,
    "transform_index_range", "-1",
    "transform_name", "Manual correction",
    "transform_matrix", "1,0,0,0,0,1,0,0,0,0,1,0",
    "timepoint_range", "0:last"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.dataset.transform import DatasetTransformSetCommand

cs.run(DatasetTransformSetCommand, True,
    ["sources", sources,
     "transform_index_range", "-1",
     "transform_name", "Manual correction",
     "transform_matrix", "1,0,0,0,0,1,0,0,0,0,1,0",
     "timepoint_range", "0:last"]
).get()
```
::::

:::::

(dataset-add-deskew-transform)=
### Dataset - Add Deskew Transform

*Source: {biop-src}`DatasetDeskewCommand.java <ch/epfl/biop/command/dataset/DatasetDeskewCommand.java>`*

Appends a deskew transform to the chain of SpimData-backed sources. Light-sheet microscopes that
scan at an angle — the Zeiss LLS7 among them — acquire planes that are sheared with respect to the
sample. Adding the deskew as a *transform* means no pixel is resampled: the data stays on disk in
its raw geometry and BigDataViewer displays it correctly.

| Parameter | Description |
|-----------|-------------|
| Select source(s) | Sources whose SpimData transforms will be modified |
| Stack (scan) axis | Axis of the raw data along which the planes are stacked, i.e. the scan direction (`X`, `Y`, `Z`; default `Z`) |
| Shear direction axis | In-plane axis along which the successive planes are shifted (`X`, `-X`, `Y`, `-Y`, `Z`, `-Z`; default `X`) |
| Deskew angle (degrees) | Angle between the scan direction and the image plane (30 degrees for a Zeiss LLS7) |
| Flip axis (before deskew) | Axis flipped before the deskew is applied, if any (`None`, `X`, `Y`, `Z`) |
| Put the stack axis along Z | Rotates the data after the deskew so that the deskewed stack axis points along Z |
| Deskew around the image origin | Applies the deskew around the origin of each image instead of the origin of the physical space |
| Transform name | Name given to the transform added in the transform chain |

:::{tip}
The dialog has a **Set the parameters for a Zeiss LLS7 dataset** button that fills in the whole
parameter set for LLS7 data in one click. Use it as a starting point if your microscope is an LLS7.
:::

:::{note}
This command only works on sources backed by a SpimData dataset — the same restriction as the other
commands in this section. The deskew is *appended* to the existing chain, so running it twice applies
it twice; use [Dataset - Remove Transforms](#dataset-transform-stack) to undo.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Dataset --> Transform Stack --> Dataset - Add Deskew Transform`
::::

::::{tab-item} IJ Macro
```ijm
run("Dataset - Add Deskew Transform");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.dataset.DatasetDeskewCommand

cs.run(DatasetDeskewCommand, true,
    "sources", sources,
    "stack_axis", "Z",
    "shear_axis", "X",
    "angle", 30.0,
    "flip_axis", "None",
    "reorient_along_z", false,
    "around_image_origin", true,
    "transform_name", "Deskew"
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.dataset import DatasetDeskewCommand

cs.run(DatasetDeskewCommand, True,
    ["sources", sources,
     "stack_axis", "Z",
     "shear_axis", "X",
     "angle", 30.0,
     "flip_axis", "None",
     "reorient_along_z", False,
     "around_image_origin", True,
     "transform_name", "Deskew"]
).get()
```
::::

:::::
