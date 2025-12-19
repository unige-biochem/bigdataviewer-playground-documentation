# Synchronizing Multiple Viewers

When working with multiple BDV or BVV windows, it's often useful to synchronize them so that navigation in one window is reflected in the others. BigDataViewer Playground provides two types of synchronization.

## Types of Synchronization

| Type | What's Synchronized |
|------|---------------------|
| **View Sync** | Camera position, rotation, zoom, and optionally timepoint |
| **State Sync** | Source visibility, colors, and display settings |

---

## View Synchronization

### Synchronize Views

**Command**: `Viewers - Synchronize views`
**Class**: `sc.fiji.bdvpg.scijava.command.viewer.ViewSynchronizerCommand`

Links the viewing perspective of multiple BDV and/or BVV windows. When you navigate in one window, all synchronized windows follow.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to synchronize |
| `bvvhs` | BVV window(s) to synchronize |
| `synchronizetime` | Also synchronize timepoints across windows |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Two synchronized BDV windows showing the same view -->

### How It Works

1. Select the windows you want to synchronize
2. Run the command
3. A small control window appears
4. Navigate in any synchronized window - others follow
5. **Close the control window to stop synchronization**

### Use Cases

#### Side-by-side Comparison

Display the same dataset with different visualization settings:
- Window 1: Channel A with green LUT
- Window 2: Channel B with magenta LUT
- Synchronized navigation lets you compare both channels at the same location

#### Before/After Visualization

Compare two versions of the same data:
- Window 1: Original data
- Window 2: Processed/filtered data

#### Multi-modal Data

View different imaging modalities of the same sample:
- Window 1: Fluorescence
- Window 2: Brightfield

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Example of side-by-side synchronized comparison -->

### Timepoint Synchronization

When `synchronizetime` is enabled:
- Moving through time in one window advances all windows
- Useful for time-series comparisons

When disabled:
- Each window maintains its own timepoint
- Spatial navigation is still synchronized

:::{tip}
Disable timepoint synchronization when comparing the same sample at different timepoints side by side.
:::

---

## State Synchronization

### Synchronize State

**Command**: `Viewers - Synchronize state`
**Class**: `sc.fiji.bdvpg.scijava.command.viewer.StateSynchronizerCommand`

Links the display state of multiple viewers. Changes to source visibility, colors, or display settings in one window are applied to all synchronized windows.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `bdvhs` | BDV window(s) to synchronize |
| `bvvhs` | BVV window(s) to synchronize |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - State synchronization control window -->

### What Gets Synchronized

- **Source visibility**: Showing/hiding sources
- **Source grouping**: Group assignments
- **Display mode**: Fused vs. single source mode

### How It Works

1. Select windows to synchronize
2. Run the command
3. A control window appears
4. Changes in any window propagate to others
5. **Close the control window to stop synchronization**

:::{note}
State synchronization is separate from view synchronization. You can use both simultaneously for complete synchronization, or just one depending on your needs.
:::

---

## Combining View and State Sync

For full synchronization, run both commands on the same set of windows:

1. Run `ViewSynchronizerCommand` on your windows
2. Run `StateSynchronizerCommand` on the same windows
3. Now both navigation AND display settings are linked

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script setting up full synchronization -->

---

## Practical Examples

### Orthogonal Views Setup

When using [orthogonal BDV views](viewers.md#create-orthogonal-bdv-views), the views are automatically synchronized. However, you can manually set up similar configurations:

1. Create three BDV windows
2. Set each to a different viewing angle (XY, XZ, YZ)
3. Synchronize views with `ViewSynchronizerCommand`
4. Navigate in one window - all three update

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Custom orthogonal view setup -->

### Multi-Monitor Workflow

When using multiple monitors:

1. Open several BDV windows
2. Position each on a different monitor
3. Synchronize as needed
4. Use a large display for main navigation, secondary displays for detail views

### Comparing Registration Results

When evaluating registration quality:

1. Open two BDV windows
2. Add original data to Window 1
3. Add registered data to Window 2
4. Synchronize views
5. Navigate to check alignment at different locations

---

## Stopping Synchronization

To stop synchronization:
- **Close the synchronization control window** that appeared when you started
- The windows become independent again

:::{warning}
If you close a synchronized BDV window without closing the synchronization control window first, you may see error messages. Always close the control window first.
:::

---

## Performance Considerations

- **Many windows**: Synchronizing many windows may impact performance
- **Large data**: View sync with very large datasets may introduce slight lag
- **Mixed BDV/BVV**: Synchronizing BDV and BVV windows together works but may be slower

:::{tip}
For best performance, synchronize only the windows you actually need linked.
:::

---

## Summary

| Command | Purpose |
|---------|---------|
| `ViewSynchronizerCommand` | Link navigation across viewers |
| `StateSynchronizerCommand` | Link display settings across viewers |
