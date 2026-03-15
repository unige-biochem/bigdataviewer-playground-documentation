# Source Utilities

Utility commands for managing multi-resolution pyramids, timepoints, and sources in the workspace.

---

## Multi-Resolution

These commands manage the pyramid (multi-resolution) levels of your sources. Pyramid levels are crucial for interactive navigation — they let the viewer load lower-resolution tiles when zoomed out, keeping browsing responsive even on very large datasets.

### Source - Pyramidize

Generates multi-resolution pyramid levels for sources that don't already have them (e.g. sources derived from processing operations).

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Pyramidize`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to add pyramid levels to |

### Source - Crop Resolution Levels

Creates a new source with only a subset of the original resolution levels. Useful when you want to restrict which pyramid levels are available — for example, to skip the lowest-resolution levels or to start from a specific level.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Crop Resolution Levels`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to crop resolution levels from |
| Min Level | Minimum resolution level to keep (0 = highest resolution) |
| Max Level | Maximum resolution level to keep (inclusive) |
| Name Suffix | Suffix to append to the source name |

---

## Timepoint Operations

Commands for manipulating the time dimension of your sources.

### Source - Freeze Timepoint

Creates a new source that shows a single fixed timepoint across a range of timepoints. Useful for creating a static reference from a time-series — for example, freezing a pre-treatment timepoint so it can be compared side-by-side with later timepoints.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Freeze Timepoint`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to freeze |
| Timepoint to copy | The timepoint to replicate |
| Timepoint start | Start of the output time range |
| Timepoint end (excluded) | End of the output time range (exclusive) |
| Output Name | Suffix for the resulting source |

### Source - Shift Timepoints

Creates a new source with timepoints offset by a fixed amount. Useful for aligning time-series data that was acquired with different starting times.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Source - Shift Timepoints`

| Parameter | Description |
|-----------|-------------|
| Select Sources | The sources to time-shift |
| Time Shift | Number of timepoints to shift (positive = forward, negative = backward) |
| Output Name | Suffix for the resulting source |

---

## Source Management

Utility commands for managing sources in the workspace.

| Command | Menu path | Description |
|---------|-----------|-------------|
| Source - Delete | `Process > Source - Delete` | Removes selected sources from the workspace |
| Source - Duplicate | `Process > Source - Duplicate` | Creates a copy of the selected sources |
| Source - Add Metadata | `Process > Source - Add Metadata` | Attaches a key-value metadata string to selected sources (useful for filtering in the tree view) |