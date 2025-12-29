# Interactive Tools

This section covers interactive selection and manipulation tools in BigDataViewer Playground.

:::{note}
This section is under development. Documentation for interactive tool commands is being added.
:::

## Overview

BigDataViewer Playground provides interactive tools for selecting regions of interest and defining spatial parameters directly in the viewer.

## Selection Tools

### Point Selection

Interactively select points in 3D space within BDV windows.

**Commands:**
- `GetUserPointsCommand` - Interactive point selection

**Use Cases:**
- Defining landmarks for registration
- Marking positions of interest
- Specifying coordinates for processing

### Rectangle Selection (2D)

Select rectangular regions in the current view plane.

**Commands:**
- `GetUserRectangleCommand` - Interactive rectangle selection

**Use Cases:**
- Defining regions for 2D registration
- Selecting areas for cropping
- Specifying ROIs for analysis

### 3D Box Selection

Select 3D bounding boxes interactively.

**Commands:**
- `BoxSelectorCommand` - Interactive 3D box selection

**Use Cases:**
- Defining volumes for cropping
- Specifying regions for export
- Setting boundaries for processing

## View Export Tools

Export the current BDV view to ImagePlus format.

**Commands:**
- `BdvViewToImagePlusExportCommand` - Export current view with options
- `BasicBdvViewToImagePlusExportCommand` - Simple view export

## Visualization Tools

**Commands:**
- `OverviewerCommand` - Create overview visualization
- `ShowGridBdvCommand` - Display sources in grid layout

## Planned Documentation

The following pages will be added:

- Point selection tutorial
- Region selection guide
- 3D box selection workflow
- View export options

## See Also

- [Navigation & Overlays](../commands/navigation_overlays.md)
- [Viewers](../commands/viewers.md)
