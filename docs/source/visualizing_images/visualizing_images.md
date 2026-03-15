# Visualizing Images

This guide covers how to display your datasets in viewer windows and control their appearance.

BigDataViewer Playground provides two types of viewers:

- **BDV (BigDataViewer)** — a 2D slice viewer that lets you navigate freely through 3D data by slicing at any orientation. This is the primary viewer for most tasks.
- **BVV (BigVolumeViewer)** — a GPU-accelerated 3D volume renderer that shows your data as a translucent volume. Useful for getting a spatial overview of 3D structures.

Both viewers share the same lazy-loading architecture: only the pixels currently visible on screen are fetched, so even terabyte-scale datasets can be explored interactively.

All display commands are found under:

{menuselection}`Plugins --> BigDataViewer-Playground --> Display`

---

## Opening a BDV Window

### BDV - Show Sources

The most common way to visualize your data. Creates a new BDV window and displays the selected sources in it.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to display |
| Adjust View on Sources | Centers and zooms the view to fit the displayed sources |
| Auto Contrast | Automatically adjusts brightness and contrast based on the current timepoint |
| Interpolate | Enables interpolation for smoother rendering |
| Open In New Window | Force creation of a new window (otherwise reuses an existing one) |

:::{tip}
If you have already opened a BDV window and want to add more sources to it, uncheck **Open In New Window**. The sources will be added to the last active BDV window.
:::

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Show Sources`

![BDV window displaying two channels of the LLS7 HeLa dataset](images/bdv_show_sources_BigDataViewer.png)
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Show Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.SingleBdvSourcesShowCommand

cs.run(SingleBdvSourcesShowCommand, true,
    "sources", sources,
    "adjust_view", true,
    "auto_contrast", false,
    "interpolate", true,
    "make_new_window", true
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import SingleBdvSourcesShowCommand

cs.run(SingleBdvSourcesShowCommand, True,
    ["sources", sources,
     "adjust_view", True,
     "auto_contrast", False,
     "interpolate", True,
     "make_new_window", True]
).get()
```
::::

:::::

### BDV - Create

Creates an empty BDV window without any sources. You can then add sources to it later using **BDV - Show Sources** or **BDV - Show Sources In Multiple Windows**.

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Create`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Create");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvCreateCommand

cs.run(BdvCreateCommand, true).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvCreateCommand

cs.run(BdvCreateCommand, True).get()
```
::::

:::::

### BDV - Show Sources In Multiple Windows

Adds sources to several existing BDV windows at once.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to add sources to |
| Select Source(s) | The source(s) to add |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Show Sources In Multiple Windows`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Show Sources In Multiple Windows");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvSourcesShowCommand

cs.run(BdvSourcesShowCommand, true,
    "bdvhs", bdvhs,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvSourcesShowCommand

cs.run(BdvSourcesShowCommand, True,
    ["bdvhs", bdvhs,
     "sources", sources]
).get()
```
::::

:::::

---

## Navigating in BDV

BigDataViewer uses a combination of mouse and keyboard controls for navigation. Here are the essential shortcuts:

### Mouse Controls

| Action | Effect |
|--------|--------|
| Left-click + drag | Pan (translate) the view |
| Right-click + drag (or middle-click + drag) | Rotate the view in 3D |
| Scroll wheel | Zoom in/out |
| Shift + scroll wheel | Walk through Z slices (translate along the viewing axis) |

### Keyboard Shortcuts

| Key | Effect |
|-----|--------|
| {kbd}`X` / {kbd}`Y` / {kbd}`Z` | Align the view to the X, Y, or Z axis |
| {kbd}`Shift+X` / {kbd}`Shift+Y` / {kbd}`Shift+Z` | Align to the opposite direction of that axis |
| {kbd}`I` | Toggle between nearest-neighbor and interpolated rendering |
| {kbd}`S` | Toggle brightness/contrast dialog |
| {kbd}`F6` | Toggle visibility settings (choose which sources are shown) |
| {kbd}`T` | Toggle timepoint slider |
| {kbd}`[` / {kbd}`]` | Step backward/forward through timepoints |
| {kbd}`Numpad 1`–`0` | Toggle visibility of source 1–10 |
| {kbd}`Shift+Numpad 1`–`0` | Toggle whether source 1–10 belongs to the current group |
| {kbd}`F` | Set the view transform to show the entire dataset |

:::{note}
These are the default BigDataViewer key bindings. They can be customized via **BDV - Preferences - Set (Key) Bindings**.
:::

---

## Orthogonal Views

### BDV - Create Orthogonal Views

Opens three synchronized BDV windows showing XY (front), ZY (right), and XZ (bottom) views. Navigating in one window automatically updates the other two.

| Parameter | Description |
|-----------|-------------|
| Window Width / Height | Size in pixels for each BDV window |
| X/Y Front Window Location | Screen position for the front (XY) window |
| Number of timepoints | Total number of timepoints (use 1 for a single timepoint) |
| Display | Screen index for window placement (use 0 if you have one screen) |
| Add cross overlay | Draws a cross at the center of each window |
| Interpolate | Enables interpolation for smoother rendering |
| Synchronize sources | Sources added to one window will automatically appear in all three |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Create Orthogonal Views`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Create Orthogonal Views");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvOrthoCreateCommand

cs.run(BdvOrthoCreateCommand, true,
    "sizex", 512,
    "sizey", 512,
    "locationx", 0,
    "locationy", 0,
    "ntimepoints", 1,
    "screen", 0,
    "drawcrosses", true,
    "interpolate", true,
    "synchronize_sources", true
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvOrthoCreateCommand

cs.run(BdvOrthoCreateCommand, True,
    ["sizex", 512,
     "sizey", 512,
     "locationx", 0,
     "locationy", 0,
     "ntimepoints", 1,
     "screen", 0,
     "drawcrosses", True,
     "interpolate", True,
     "synchronize_sources", True]
).get()
```
::::

:::::

::::{grid} 2
:::{grid-item}
![XY — front view](images/bdv_orthogonal_views_BigDataViewer-XY.png)
:::
:::{grid-item}
![ZY — right view](images/bdv_orthogonal_views_BigDataViewer-ZY.png)
:::
:::{grid-item}
![XZ — bottom view](images/bdv_orthogonal_views_BigDataViewer-XZ.png)
:::
:::{grid-item}
:::
::::

---

## Grid Overview

When working with many sources (e.g. multiple tiles or channels), it can be helpful to see them all at once.

### BDV - Show Sources On Grid

Arranges selected sources in a grid layout within a new BDV window. Each cell shows one source, giving you a quick overview of all your data.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to display on the grid |
| Number of Columns | Number of columns in the grid layout |
| Split by Entities | Comma-separated entity types to split by (e.g. `channel, fileseries`) |
| Start Timepoint | The timepoint to use for determining source dimensions |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Show Sources On Grid`

![Both channels of the LLS7 HeLa dataset arranged in a 2-column grid](images/bdv_grid_overview_BigDataViewer.png)
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Show Sources On Grid");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import ch.epfl.biop.command.display.bdv.SourcesOverviewCommand

cs.run(SourcesOverviewCommand, true,
    "sources", sources,
    "n_columns", 2,
    "entities_split", "channel",
    "timepoint_begin", 0
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from ch.epfl.biop.command.display.bdv import SourcesOverviewCommand

cs.run(SourcesOverviewCommand, True,
    ["sources", sources,
     "n_columns", 2,
     "entities_split", "channel",
     "timepoint_begin", 0]
).get()
```
::::

:::::

### BDV - Create Grid BDV

Creates an empty BDV window pre-configured for grid display. You can then add sources to it.

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Create Grid BDV`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Create Grid BDV");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.command.display.bdv.BdvGridCreateCommand

cs.run(BdvGridCreateCommand, true).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.command.display.bdv import BdvGridCreateCommand

cs.run(BdvGridCreateCommand, True).get()
```
::::

:::::

---

## Adjusting Source Appearance

These commands control how individual sources look in any viewer window — color, brightness, and visibility. They affect display only, never the underlying data.

### Source - Set Color

Changes the display color of one or more sources.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to recolor |
| Color | The new display color |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Source --> Source - Set Color`

![LLS7 HeLa channels displayed in cyan and magenta](images/source_set_color_BigDataViewer.png)
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Set Color");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.source.SourceColorChangeCommand
import net.imglib2.type.numeric.ARGBType

def color = new ARGBType(ARGBType.rgba(0, 255, 0, 255)) // green

cs.run(SourceColorChangeCommand, true,
    "sources", sources,
    "color", color
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.source import SourceColorChangeCommand
from net.imglib2.type.numeric import ARGBType

color = ARGBType(ARGBType.rgba(0, 255, 0, 255))  # green

cs.run(SourceColorChangeCommand, True,
    ["sources", sources,
     "color", color]
).get()
```
::::

:::::

### Source - Set Brightness

Sets the display range (min and max intensity values) for one or more sources. This is the equivalent of adjusting the "Brightness & Contrast" in Fiji.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to adjust |
| Min | Minimum value of the display range |
| Max | Maximum value of the display range |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Source --> Source - Set Brightness`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Set Brightness");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.source.SourceBrightnessAdjustCommand

cs.run(SourceBrightnessAdjustCommand, true,
    "sources", sources,
    "min", 0.0,
    "max", 1000.0
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.source import SourceBrightnessAdjustCommand

cs.run(SourceBrightnessAdjustCommand, True,
    ["sources", sources,
     "min", 0.0,
     "max", 1000.0]
).get()
```
::::

:::::

### Source - Make Visible

Toggles sources on so they are drawn in all BDV windows where they are present.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to show |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Source --> Source - Make Visible`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Make Visible");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.source.SourceVisibilityONCommand

cs.run(SourceVisibilityONCommand, true,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.source import SourceVisibilityONCommand

cs.run(SourceVisibilityONCommand, True,
    ["sources", sources]
).get()
```
::::

:::::

### Source - Make Invisible

Hides sources in all BDV windows where they are present.

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The source(s) to hide |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Source --> Source - Make Invisible`
::::

::::{tab-item} IJ Macro
```ijm
run("Source - Make Invisible");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.source.SourceVisibilityOFFCommand

cs.run(SourceVisibilityOFFCommand, true,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.source import SourceVisibilityOFFCommand

cs.run(SourceVisibilityOFFCommand, True,
    ["sources", sources]
).get()
```
::::

:::::

---

## Managing BDV Windows

### BDV - Adjust View On Sources

Reframes the current view to fit the selected sources. Useful when you have lost your bearings or want to quickly navigate to a specific source.

| Parameter | Description |
|-----------|-------------|
| Select BDV Window | The BDV window to adjust |
| Select Source(s) | The source(s) to frame |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Adjust View On Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Adjust View On Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle bdvh
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvViewSourcesAdjustCommand

cs.run(BdvViewSourcesAdjustCommand, true,
    "bdvh", bdvh,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle bdvh
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvViewSourcesAdjustCommand

cs.run(BdvViewSourcesAdjustCommand, True,
    ["bdvh", bdvh,
     "sources", sources]
).get()
```
::::

:::::

### BDV - Remove Sources

Removes sources from one or more BDV windows. This only removes them from the viewer — it does not delete the sources from the dataset.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The windows to remove sources from |
| Select Source(s) | The source(s) to remove |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Remove Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Remove Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvSourcesRemoveCommand

cs.run(BdvSourcesRemoveCommand, true,
    "bdvhs", bdvhs,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvSourcesRemoveCommand

cs.run(BdvSourcesRemoveCommand, True,
    ["bdvhs", bdvhs,
     "sources", sources]
).get()
```
::::

:::::

### BDV - Close

Closes one or more BDV windows.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to close |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> BDV - Close`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Close");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.BdvCloseCommand

cs.run(BdvCloseCommand, true,
    "bdvhs", bdvhs
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv import BdvCloseCommand

cs.run(BdvCloseCommand, True,
    ["bdvhs", bdvhs]
).get()
```
::::

:::::

### BDV - Set Title

Changes the title of a BDV window.

| Parameter | Description |
|-----------|-------------|
| Select BDV Window | The BDV window to rename |
| Title | The new window title |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Set Title`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Set Title");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle bdvh
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvTitleSetCommand

cs.run(BdvTitleSetCommand, true,
    "bdvh", bdvh,
    "title", "My BDV Window"
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle bdvh
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvTitleSetCommand

cs.run(BdvTitleSetCommand, True,
    ["bdvh", bdvh,
     "title", "My BDV Window"]
).get()
```
::::

:::::

---

## Overlays

Overlays add visual annotations on top of the viewer without modifying the data.

### BDV - Add Center Cross Overlay

Draws a crosshair at the center of the BDV window. Helpful for orthogonal view setups to see where the three planes intersect.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to add the overlay to |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Overlay --> BDV - Add Center Cross Overlay`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Center Cross Overlay");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.overlay.BdvOverlayCrossAddCommand

cs.run(BdvOverlayCrossAddCommand, true,
    "bdvhs", bdvhs
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.overlay import BdvOverlayCrossAddCommand

cs.run(BdvOverlayCrossAddCommand, True,
    ["bdvhs", bdvhs]
).get()
```
::::

:::::

### BDV - Add Sources Name Overlay

Displays the name of each visible source as a text label on the viewer.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The windows to add overlays to |
| Font | Font family for the labels |
| Font Size | Font size for the labels |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Overlay --> BDV - Add Sources Name Overlay`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Sources Name Overlay");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.overlay.BdvOverlaySourceNameAddCommand

cs.run(BdvOverlaySourceNameAddCommand, true,
    "bdvhs", bdvhs,
    "fontString", "Helvetica",
    "fontSize", 12
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.overlay import BdvOverlaySourceNameAddCommand

cs.run(BdvOverlaySourceNameAddCommand, True,
    ["bdvhs", bdvhs,
     "fontString", "Helvetica",
     "fontSize", 12]
).get()
```
::::

:::::

### BDV - Add Debug Overlay

Shows the internal tiled rendering grid. Primarily useful for debugging rendering performance.

| Parameter | Description |
|-----------|-------------|
| Select BDV Window | The BDV window to add the debug overlay to |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Overlay --> BDV - Add Debug Overlay`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Debug Overlay");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle bdvh
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.overlay.BdvOverlayDebugAddCommand

cs.run(BdvOverlayDebugAddCommand, true,
    "bdvh", bdvh
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle bdvh
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.overlay import BdvOverlayDebugAddCommand

cs.run(BdvOverlayDebugAddCommand, True,
    ["bdvh", bdvh]
).get()
```
::::

:::::

---

## BDV Settings

These commands add UI elements or configure defaults for BDV windows.

### BDV - Add Z Slider

Adds a Z-position slider to the bottom of BDV windows, giving you a familiar way to scroll through Z slices.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to add the slider to |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Add Z Slider`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Z Slider");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvZSliderAddCommand

cs.run(BdvZSliderAddCommand, true,
    "bdvhs", bdvhs
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvZSliderAddCommand

cs.run(BdvZSliderAddCommand, True,
    ["bdvhs", bdvhs]
).get()
```
::::

:::::

### BDV - Add Sources Slider

Adds a slider to step through sources one by one. Useful when you have many sources and want to flip through them.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to add the slider to |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Add Sources Slider`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Sources Slider");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvSourceNavigatorAddCommand

cs.run(BdvSourceNavigatorAddCommand, true,
    "bdvhs", bdvhs
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvSourceNavigatorAddCommand

cs.run(BdvSourceNavigatorAddCommand, True,
    ["bdvhs", bdvhs]
).get()
```
::::

:::::

### BDV - Add Editor

Installs a source selection editor on BDV windows. Press the toggle key to switch between navigation and editor mode.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The windows to install the editor on |
| Toggle key | Keyboard shortcut to toggle between navigation and editor mode |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Add Editor`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Add Editor");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvEditorInstallCommand

cs.run(BdvEditorInstallCommand, true,
    "bdvhs", bdvhs,
    "toggle_key", "E"
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvEditorInstallCommand

cs.run(BdvEditorInstallCommand, True,
    ["bdvhs", bdvhs,
     "toggle_key", "E"]
).get()
```
::::

:::::

### Timepoints

BDV windows have a fixed number of timepoints. If your data has more timepoints than the window allows, you won't be able to navigate to them.

**Set Number Of Timepoints** lets you specify the number manually. **Adapt Number Of Timepoints To Sources** automatically sets it to match the sources currently in the window.

#### BDV - Set Number Of Timepoints

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to update |
| Number of timepoints | The new timepoint count |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Set Number Of Timepoints`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Set Number Of Timepoints");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvTimepointsSetCommand

cs.run(BdvTimepointsSetCommand, true,
    "bdvhs", bdvhs,
    "numberoftimepoints", 100
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvTimepointsSetCommand

cs.run(BdvTimepointsSetCommand, True,
    ["bdvhs", bdvhs,
     "numberoftimepoints", 100]
).get()
```
::::

:::::

#### BDV - Adapt Number Of Timepoints To Sources

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | The BDV windows to update |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Adapt Number Of Timepoints To Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Adapt Number Of Timepoints To Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvTimepointsAdaptCommand

cs.run(BdvTimepointsAdaptCommand, true,
    "bdvhs", bdvhs
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvTimepointsAdaptCommand

cs.run(BdvTimepointsAdaptCommand, True,
    ["bdvhs", bdvhs]
).get()
```
::::

:::::

### BDV - Preferences - Set (Key) Bindings

Opens a dialog to customize the keyboard and mouse bindings for BDV windows.

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Preferences - Set (Key) Bindings`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Preferences - Set (Key) Bindings");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvSettingsSetCommand

cs.run(BdvSettingsSetCommand, true).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvSettingsSetCommand

cs.run(BdvSettingsSetCommand, True).get()
```
::::

:::::

---

## Customizing BDV Defaults

These commands configure the default appearance and behavior of **newly created** BDV windows. They do not affect windows that are already open.

### BDV - Set Style (Default)

| Parameter | Description |
|-----------|-------------|
| Window title | Default title for new BDV windows |
| Window width / height | Default window dimensions in pixels |
| Interpolate | Enable interpolation by default |
| 2D mode | Restricts navigation to 2D (only Z-rotations allowed) |
| Number of timepoints | Default number of timepoints |
| Number of rendering threads | Threads used for rendering |
| Number of source groups | Source groups available in the window |
| Screen scales | Comma-separated scale factors for multi-resolution rendering (e.g. `1, 0.5, 0.25`) |
| Target render time (ms) | Target time per frame in milliseconds |
| Reset to default | Ignore all parameters and reset to defaults |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Set Style (Default)`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Set Style (Default)");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bdv.settings.BdvStyleDefaultSetCommand

cs.run(BdvStyleDefaultSetCommand, true,
    "frame_title", "BigDataViewer",
    "width", 800,
    "height", 600,
    "interpolate", true,
    "is2d", false,
    "n_timepoints", 1,
    "num_rendering_threads", 3,
    "num_source_groups", 10,
    "screen_scales", "1, 0.5, 0.25",
    "target_render_ms", 30,
    "reset_to_default", false
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bdv.settings import BdvStyleDefaultSetCommand

cs.run(BdvStyleDefaultSetCommand, True,
    ["frame_title", "BigDataViewer",
     "width", 800,
     "height", 600,
     "interpolate", True,
     "is2d", False,
     "n_timepoints", 1,
     "num_rendering_threads", 3,
     "num_source_groups", 10,
     "screen_scales", "1, 0.5, 0.25",
     "target_render_ms", 30,
     "reset_to_default", False]
).get()
```
::::

:::::

### BDV - Set Style (BIOP)

An alternative default style provided by the BIOP team. Includes additional options like font and font size for the source name overlay.

| Parameter | Description |
|-----------|-------------|
| Window title | Default title for new BDV windows |
| Window width / height | Default window dimensions in pixels |
| Font | Font family for the source name overlay |
| Font Size | Font size for the source name overlay |
| Interpolate | Enable interpolation by default |
| 2D mode | Restricts navigation to 2D |
| Number of timepoints | Default number of timepoints |
| Number of rendering threads | Threads used for rendering |
| Number of source groups | Source groups available in the window |
| Screen scales | Multi-resolution scale factors |
| Target render time (ms) | Target time per frame in milliseconds |
| Reset to default | Ignore all parameters and reset to defaults |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Set Style (BIOP)`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Set Style (BIOP)");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.bdv.supplier.biop.BdvStyleBIOPSetCommand

cs.run(BdvStyleBIOPSetCommand, true,
    "frametitle", "BigDataViewer",
    "width", 800,
    "height", 600,
    "font", "Helvetica",
    "fontSize", 12,
    "interpolate", true,
    "is2d", false,
    "numtimepoints", 1,
    "numrenderingthreads", 3,
    "numsourcegroups", 10,
    "screenscales", "1, 0.5, 0.25",
    "targetrenderms", 30,
    "resetToDefault", false
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.bdv.supplier.biop import BdvStyleBIOPSetCommand

cs.run(BdvStyleBIOPSetCommand, True,
    ["frametitle", "BigDataViewer",
     "width", 800,
     "height", 600,
     "font", "Helvetica",
     "fontSize", 12,
     "interpolate", True,
     "is2d", False,
     "numtimepoints", 1,
     "numrenderingthreads", 3,
     "numsourcegroups", 10,
     "screenscales", "1, 0.5, 0.25",
     "targetrenderms", 30,
     "resetToDefault", False]
).get()
```
::::

:::::

### BDV - Set Style (Alpha)

A style that supports alpha (transparency) blending and white background. Useful when preparing figures or overlaying partially transparent sources.

| Parameter | Description |
|-----------|-------------|
| Window title | Default title for new BDV windows |
| Window width / height | Default window dimensions in pixels |
| Interpolate | Enable interpolation by default |
| 2D mode | Restricts navigation to 2D |
| Number of timepoints | Default number of timepoints |
| Number of rendering threads | Threads used for rendering |
| Number of source groups | Source groups available in the window |
| Screen scales | Multi-resolution scale factors |
| Target render time (ms) | Target time per frame in milliseconds |
| Use alpha layer | Enable alpha (transparency) blending |
| Reset to default | Ignore all parameters and reset to defaults |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Settings --> BDV - Set Style (Alpha)`
::::

::::{tab-item} IJ Macro
```ijm
run("BDV - Set Style (Alpha)");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import ch.epfl.biop.command.display.bdv.settings.BdvStyleAlphaSetCommand

cs.run(BdvStyleAlphaSetCommand, true,
    "frametitle", "BigDataViewer",
    "width", 800,
    "height", 600,
    "interpolate", true,
    "is2d", false,
    "numtimepoints", 1,
    "numrenderingthreads", 3,
    "numsourcegroups", 10,
    "screenscales", "1, 0.5, 0.25",
    "targetrenderms", 30,
    "usealphalayer", true,
    "resetToDefault", false
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from ch.epfl.biop.command.display.bdv.settings import BdvStyleAlphaSetCommand

cs.run(BdvStyleAlphaSetCommand, True,
    ["frametitle", "BigDataViewer",
     "width", 800,
     "height", 600,
     "interpolate", True,
     "is2d", False,
     "numtimepoints", 1,
     "numrenderingthreads", 3,
     "numsourcegroups", 10,
     "screenscales", "1, 0.5, 0.25",
     "targetrenderms", 30,
     "usealphalayer", True,
     "resetToDefault", False]
).get()
```
::::

:::::

---

## Synchronizing Viewers

When working with multiple viewer windows, you can synchronize them so they move together.

### Viewers - Synchronize Views

Locks the navigation of multiple BDV and/or BVV windows together. When you pan, zoom, or rotate in one window, all synchronized windows follow. A small popup window appears — close it to stop the synchronization.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows to synchronize | BDV windows to include |
| Select BVV Windows to synchronize | BVV windows to include |
| Synchronize timepoints | Also synchronizes the current timepoint across windows |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Viewers - Synchronize Views`
::::

::::{tab-item} IJ Macro
```ijm
run("Viewers - Synchronize Views");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.ViewSynchronizeCommand

cs.run(ViewSynchronizeCommand, true,
    "bdvhs", bdvhs,
    "bvvhs", [] as Object[],
    "synchronizetime", true
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display import ViewSynchronizeCommand

cs.run(ViewSynchronizeCommand, True,
    ["bdvhs", bdvhs,
     "bvvhs", [],
     "synchronizetime", True]
).get()
```
::::

:::::

### Viewers - Synchronize States

Synchronizes which sources are visible across multiple viewer windows. When you toggle a source on or off in one window, all synchronized windows update. Close the popup window to stop.

| Parameter | Description |
|-----------|-------------|
| Select BDV Windows | BDV windows to synchronize |
| Select BVV Windows | BVV windows to synchronize |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> Viewers - Synchronize States`
::::

::::{tab-item} IJ Macro
```ijm
run("Viewers - Synchronize States");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BdvHandle[] bdvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.StateSynchronizeCommand

cs.run(StateSynchronizeCommand, true,
    "bdvhs", bdvhs,
    "bvvhs", [] as Object[]
).get()
```
::::

::::{tab-item} Python
```python
#@BdvHandle[] bdvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display import StateSynchronizeCommand

cs.run(StateSynchronizeCommand, True,
    ["bdvhs", bdvhs,
     "bvvhs", []]
).get()
```
::::

:::::

---

## Capturing the Current View

The current BDV view can be exported as a standard Fiji ImagePlus or as new sources for further processing. These commands are covered in detail in the Exporting Images guide, but here is a quick overview:

| Command | What it does |
|---------|-------------|
| BDV - Export Current View As ImagePlus | Full control over pixel size, region, and Z thickness |
| BDV - Export Current View As ImagePlus (Match Window) | Quick capture using the current window dimensions |
| BDV - Export Current View As Sources | Creates new sources resampled at the current view orientation (oblique slicing) |

{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BDV --> Export`

---

## Volume Rendering with BVV

BigVolumeViewer (BVV) renders your data as a 3D volume using GPU acceleration. This is useful for getting a spatial overview of structures that are hard to appreciate in 2D slices.

:::{note}
BVV requires a GPU with OpenGL 3.3+ support. It may not be available on all systems.
:::

### BVV - Create

Creates an empty BVV window.

| Parameter | Description |
|-----------|-------------|
| Window title | Title for the new BVV window |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BVV --> BVV - Create`
::::

::::{tab-item} IJ Macro
```ijm
run("BVV - Create");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bvv.BvvCreateCommand

cs.run(BvvCreateCommand, true,
    "windowtitle", "BigVolumeViewer"
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bvv import BvvCreateCommand

cs.run(BvvCreateCommand, True,
    ["windowtitle", "BigVolumeViewer"]
).get()
```
::::

:::::

### BVV - Show Sources

Adds sources to an existing BVV window.

| Parameter | Description |
|-----------|-------------|
| Select BVV Window | The BVV window to add sources to |
| Select source(s) | The source(s) to display |
| Adjust View on Source | Centers and zooms the view to fit the added sources |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BVV --> BVV - Show Sources`

![BVV volume rendering of the LLS7 HeLa dataset](images/bvv_show_sources_BigVolumeViewer.png)
::::

::::{tab-item} IJ Macro
```ijm
run("BVV - Show Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BvvHandle bvvh
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bvv.BvvSourcesShowCommand

cs.run(BvvSourcesShowCommand, true,
    "bvvh", bvvh,
    "sources", sources,
    "adjust_view", true
).get()
```
::::

::::{tab-item} Python
```python
#@BvvHandle bvvh
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bvv import BvvSourcesShowCommand

cs.run(BvvSourcesShowCommand, True,
    ["bvvh", bvvh,
     "sources", sources,
     "adjust_view", True]
).get()
```
::::

:::::

### BVV - Create Orthogonal Views

Creates three synchronized BVV windows with orthogonal orientations, analogous to the BDV orthogonal views but with volume rendering.

| Parameter | Description |
|-----------|-------------|
| Window Width / Height | Size in pixels for each BVV window |
| X/Y Front Window Location | Screen position for the front (XY) window |
| Number of timepoints | Total number of timepoints |
| Display | Screen index for window placement |
| Interpolate | Enables interpolation for smoother rendering |
| Synchronize sources | Sources added to one window will automatically appear in all three |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BVV --> BVV - Create Orthogonal Views`
::::

::::{tab-item} IJ Macro
```ijm
run("BVV - Create Orthogonal Views");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@CommandService cs

import sc.fiji.bdvpg.command.display.bvv.BvvOrthoCreateCommand

cs.run(BvvOrthoCreateCommand, true,
    "sizex", 512,
    "sizey", 512,
    "locationx", 0,
    "locationy", 0,
    "ntimepoints", 1,
    "screen", 0,
    "interpolate", true,
    "synchronize_sources", true
).get()
```
::::

::::{tab-item} Python
```python
#@CommandService cs

from sc.fiji.bdvpg.command.display.bvv import BvvOrthoCreateCommand

cs.run(BvvOrthoCreateCommand, True,
    ["sizex", 512,
     "sizey", 512,
     "locationx", 0,
     "locationy", 0,
     "ntimepoints", 1,
     "screen", 0,
     "interpolate", True,
     "synchronize_sources", True]
).get()
```
::::

:::::

::::{grid} 2
:::{grid-item}
![XY — front view](images/bvv_orthogonal_views_BigVolumeViewer-XY.png)
:::
:::{grid-item}
![ZY — right view](images/bvv_orthogonal_views_BigVolumeViewer-ZY.png)
:::
:::{grid-item}
![XZ — bottom view](images/bvv_orthogonal_views_BigVolumeViewer-XZ.png)
:::
:::{grid-item}
:::
::::

### BVV - Remove Sources

Removes sources from BVV windows.

| Parameter | Description |
|-----------|-------------|
| Select BVV Windows | The BVV windows to remove sources from |
| Select Source(s) | The source(s) to remove |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BVV --> BVV - Remove Sources`
::::

::::{tab-item} IJ Macro
```ijm
run("BVV - Remove Sources");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BvvHandle[] bvvhs
#@SourceAndConverter[] sources
#@CommandService cs

import sc.fiji.bdvpg.command.display.bvv.BvvSourcesRemoveCommand

cs.run(BvvSourcesRemoveCommand, true,
    "bvvhs", bvvhs,
    "sources", sources
).get()
```
::::

::::{tab-item} Python
```python
#@BvvHandle[] bvvhs
#@SourceAndConverter[] sources
#@CommandService cs

from sc.fiji.bdvpg.command.display.bvv import BvvSourcesRemoveCommand

cs.run(BvvSourcesRemoveCommand, True,
    ["bvvhs", bvvhs,
     "sources", sources]
).get()
```
::::

:::::

### BVV - Set Number Of Timepoints

Sets the number of timepoints available in BVV windows.

| Parameter | Description |
|-----------|-------------|
| Select BVV Windows | The BVV windows to update |
| Number of timepoints | The new timepoint count |

:::::{tab-set}

::::{tab-item} GUI
{menuselection}`Plugins --> BigDataViewer-Playground --> Display --> BVV --> Settings --> BVV - Set Number Of Timepoints`
::::

::::{tab-item} IJ Macro
```ijm
run("BVV - Set Number Of Timepoints");
```
::::

::::{tab-item} Groovy
```imagej-groovy
#@BvvHandle[] bvvhs
#@CommandService cs

import sc.fiji.bdvpg.command.display.bvv.settings.BvvTimepointsSetCommand

cs.run(BvvTimepointsSetCommand, true,
    "bvvhs", bvvhs,
    "numberoftimepoints", 100
).get()
```
::::

::::{tab-item} Python
```python
#@BvvHandle[] bvvhs
#@CommandService cs

from sc.fiji.bdvpg.command.display.bvv.settings import BvvTimepointsSetCommand

cs.run(BvvTimepointsSetCommand, True,
    ["bvvhs", bvvhs,
     "numberoftimepoints", 100]
).get()
```
::::

:::::