# Sources: Appearance (Colors, LUTs, Brightness)

Controlling how sources are displayed is essential for effective visualization. BigDataViewer Playground provides several commands to adjust colors, apply Look-Up Tables (LUTs), and fine-tune brightness and contrast.

## Color Management

### Change Source Color

**Command**: `Sources - Set color`
**Class**: `sc.fiji.bdvpg.scijava.command.source.SourceColorChangerCommand`

Changes the display color of one or more sources. This modifies the existing sources directly.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to modify |
| `color` | New color (RGB picker) |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Color picker dialog and result showing colored source -->

:::{tip}
Use contrasting colors when displaying multiple channels to make them easily distinguishable.
:::

---

### Create Color Duplicates

**Command**: `Sources - Duplicate with new color`
**Class**: `sc.fiji.bdvpg.scijava.command.source.ColorSourceCreatorCommand`

Creates duplicates of sources with a specified color. The original sources remain unchanged.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to duplicate |
| `color` | Color for the new sources |

:::{note}
This is useful when you want to display the same data with different colors for comparison, without modifying the original.
:::

---

## Look-Up Tables (LUTs)

### Apply a LUT to Sources

**Command**: `Sources - Apply LUT`
**Class**: `sc.fiji.bdvpg.scijava.command.source.LUTSourceCreatorCommand`

Creates duplicates of sources with a specific Look-Up Table applied. LUTs map intensity values to colors, allowing for enhanced visualization of specific intensity ranges.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to process |
| `choice` | LUT name (from available LUTs) |
| `table` | Alternative: direct LUT selection |

**Output**:
- `sacs_out`: New sources with the LUT applied

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Same source displayed with different LUTs (e.g., Fire, Viridis, Grays) -->

### Available LUTs

BigDataViewer Playground provides access to all LUTs available in Fiji. Common choices include:

| LUT | Use Case |
|-----|----------|
| **Grays** | Standard grayscale |
| **Fire** | Heat map visualization |
| **Ice** | Cool tones for contrast |
| **Green**, **Red**, **Cyan**, **Magenta** | Multi-channel fluorescence |
| **Viridis**, **Plasma** | Perceptually uniform, colorblind-friendly |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Grid showing common LUTs applied to the same data -->

:::{tip}
For scientific publications, consider using perceptually uniform LUTs like **Viridis** which are colorblind-friendly and reproduce well in grayscale.
:::

---

## Brightness and Contrast

### Set Brightness Range

**Command**: `Sources - Set brightness`
**Class**: `sc.fiji.bdvpg.scijava.command.source.BrightnessAdjusterCommand`

Sets the minimum and maximum display values for sources. Values below `min` appear as black, values above `max` appear at full intensity.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to adjust |
| `min` | Minimum display value |
| `max` | Maximum display value |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Before/after showing effect of brightness adjustment -->

:::{note}
This does not modify the underlying data - only how it is displayed. The original pixel values remain unchanged.
:::

---

### Interactive Brightness Adjustment

**Command**: `Sources - Interactive brightness adjustment`
**Class**: `sc.fiji.bdvpg.scijava.command.source.InteractiveBrightnessAdjusterCommand`

Opens an interactive dialog with sliders for real-time brightness and contrast adjustment. Changes are applied immediately, allowing you to see the effect as you adjust.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to adjust |
| `min`, `max` | Initial display range |
| `minslider`, `maxslider` | Relative slider positions |
| `customsourcelabel` | Label for the adjustment window |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Interactive brightness dialog with sliders -->

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script for batch brightness adjustment -->

:::{tip}
Use the interactive adjuster when exploring a new dataset. Once you've found good values, note them down for use in scripts with `BrightnessAdjusterCommand`.
:::

---

## Practical Examples

### Multi-channel Fluorescence Display

When working with multi-channel fluorescence data:

1. **Assign distinct colors** to each channel using `SourceColorChangerCommand`:
   - DAPI (nuclei): Blue
   - GFP: Green
   - RFP: Red/Magenta

2. **Adjust brightness** independently for each channel to balance intensities

3. **Consider LUTs** for specific applications (e.g., Fire LUT for intensity quantification)

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Multi-channel composite with different colors -->

### Creating a Figure-Ready Visualization

1. **Duplicate sources** using `ColorSourceCreatorCommand` to preserve originals
2. **Apply appropriate LUTs** (consider colorblind-friendly options)
3. **Fine-tune brightness** using the interactive adjuster
4. **Export** using the export commands (see [Import & Export](import_export.md))

<!-- TODO:MISSING_CONTENT: [type: script] - Complete workflow script for figure preparation -->

---

## Summary

| Command | Purpose |
|---------|---------|
| `SourceColorChangerCommand` | Change color of existing sources |
| `ColorSourceCreatorCommand` | Duplicate sources with new color |
| `LUTSourceCreatorCommand` | Duplicate sources with LUT applied |
| `BrightnessAdjusterCommand` | Set min/max display values |
| `InteractiveBrightnessAdjusterCommand` | Interactive brightness/contrast |
